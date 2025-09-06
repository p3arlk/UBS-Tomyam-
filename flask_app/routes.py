# flask_app/routes.py
from flask import Blueprint, request, jsonify
from math import hypot

api_bp = Blueprint('api', __name__)

VIP_POINTS = 100
CARD_POINTS = 50

def latency_points(d: float) -> int:
    if d <= 2.0: return 30
    if d <= 4.0: return 20
    return 0

@api_bp.route('/ticketing-agent', methods=['POST'])
def ticketing_agent():
    if request.content_type != 'application/json':
        return jsonify({"error": "Content-Type must be application/json"}), 400
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON body"}), 400

    customers = data.get("customers", [])
    concerts = data.get("concerts", [])
    priority = data.get("priority", {})

    # Pre-process concerts (preserve order)
    clist = []
    for c in concerts:
        name = c["name"]
        x, y = c["booking_center_location"]
        clist.append((name, float(x), float(y)))

    out = {}
    for cust in customers:
        cname = cust["name"]
        vip = bool(cust["vip_status"])
        cx, cy = map(float, cust["location"])
        card = cust["credit_card"]

        best_name, best_score = None, float("-inf")
        for (n, x, y) in clist:
            score = (VIP_POINTS if vip else 0)
            if priority.get(card) == n:
                score += CARD_POINTS
            d = hypot(cx - x, cy - y)
            score += latency_points(d)
            if score > best_score:
                best_score, best_name = score, n
        out[cname] = best_name or ""

    resp = jsonify(out)
    resp.headers["Content-Type"] = "application/json"
    return resp
