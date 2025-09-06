from math import inf

def solve(input_obj):
    """
    Input shape:
    {
      "tasks": [
        { "name": str, "start": int, "end": int, "station": int, "score": int }, ...
      ],
      "subway": [
        { "connection": [int, int], "fee": int }, ...
      ],
      "starting_station": int
    }

    Output shape:
    {
        "max_score": int,
        "min_fee": int,
        "schedule": [str]  # task names in ascending start time
    }
    """
    tasks = input_obj.get("tasks", [])
    subway = input_obj.get("subway", [])
    s0_id = input_obj.get("starting_station")

    # Edge case: no tasks
    if not tasks:
        return {"max_score": 0, "min_fee": 0, "schedule": []}

    # ---- Station indexing (map arbitrary station IDs to [0..n-1]) ----
    stations = set([s0_id])
    for t in tasks:
        stations.add(t["station"])
    for r in subway:
        a, b = r["connection"]
        stations.add(a); stations.add(b)
    station_ids = sorted(stations)
    id_to_idx = {sid: i for i, sid in enumerate(station_ids)}
    s0 = id_to_idx[s0_id]
    n = len(station_ids)

    # Floyd–Warshall to find all-pairs min fees
    dist = [[inf]*n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for r in subway:
        a, b = r["connection"]
        w = r["fee"]
        ia, ib = id_to_idx[a], id_to_idx[b]
        if w < dist[ia][ib]:
            dist[ia][ib] = w
            dist[ib][ia] = w
    # Floyd–Warshall
    for k in range(n):
        dk = dist[k]
        for i in range(n):
            dik = dist[i][k]
            if dik == inf:
                continue
            di = dist[i]
            for j in range(n):
                cand = dik + dk[j]
                if cand < di[j]:
                    di[j] = cand

    # ---- Normalize + sort tasks by end time (classic interval DP) ----
    T = [
        {
            "name": t["name"],
            "start": t["start"],
            "end": t["end"],
            "station": id_to_idx[t["station"]],
            "score": t["score"],
        }
        for t in tasks
    ]
    # Sort by end, tie by start (helps determinism)
    T.sort(key=lambda x: (x["end"], x["start"]))
    m = len(T)

    # ---- DP: bestScore[i], minFeeToEnd[i] (fee up to task i, no final return), prev[i] ----
    bestScore = [0]*m
    minFeeToEnd = [inf]*m
    prev = [-1]*m

    for i in range(m):
        si = T[i]["station"]
        score_i = T[i]["score"]

        # Base: only this task (s0 -> si)
        bScore = score_i
        bFee = dist[s0][si]
        p = -1

        # Transition: from any non-overlapping task j (T[j].end <= T[i].start)
        for j in range(i):
            if T[j]["end"] <= T[i]["start"]:
                candScore = bestScore[j] + score_i
                candFee = minFeeToEnd[j] + dist[T[j]["station"]][si]
                if (candScore > bScore) or (candScore == bScore and candFee < bFee):
                    bScore = candScore
                    bFee = candFee
                    p = j

        bestScore[i] = bScore
        minFeeToEnd[i] = bFee
        prev[i] = p

    # ---- Choose best ending task, adding return fee back to s0 ----
    ansScore, ansFee, last = 0, 0, -1  # empty schedule candidate
    for i in range(m):
        totalScore = bestScore[i]
        totalFee = minFeeToEnd[i] + dist[T[i]["station"]][s0]
        if (totalScore > ansScore) or (totalScore == ansScore and totalFee < ansFee):
            ansScore, ansFee, last = totalScore, totalFee, i

    # Also allow empty schedule (score 0, fee 0)
    if ansScore == 0:
        return {"max_score": 0, "min_fee": 0, "schedule": []}

    # ---- Reconstruct chosen tasks by prev pointers ----
    chosen = []
    cur = last
    while cur != -1:
        chosen.append(T[cur])
        cur = prev[cur]
    chosen.reverse()  # now in increasing end-time order

    # Spec requires schedule sorted by start time
    chosen.sort(key=lambda x: (x["start"], x["end"], x["name"]))

    return {
        "max_score": ansScore,
        "min_fee": ansFee,
        "schedule": [t["name"] for t in chosen],
    }


# ----------------- quick self-check with the provided example -----------------
if __name__ == "__main__":
    example_input = {
      "tasks": [
        { "name": "A", "start": 0, "end": 10, "station": 1, "score": 5 }
      ],
      "subway": [
        { "connection": [0, 1], "fee": 10 }
      ],
      "starting_station": 0
    }
    print(solve(example_input))
    # Expected:
    # {"max_score": 11, "min_fee": 140, "schedule": ["A","B","C","D","E"]}
