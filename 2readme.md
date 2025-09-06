# Chase the Flag

Welcome to the challenge! This repository contains five unique labs designed to test your skills in web security and problem solving. Each lab runs on a separate endpoint and port.

---

## Rules

- There are five challenges, each running on its own port.
- The nature of each challenge will become apparent as you explore.
- Your objective is to obtain the “flag”.
- Do not attempt to attack infrastructure outside of the provided endpoints.

---

## Challenge Endpoints & Hints

Each lab is accessible at a different port.  
Below are the example endpoints and a single cryptic hint for each:

---

## Important Points

**- The server cannot be accessed from the UBS wifi. Please connect using your personal mobile data or hotspot.**

---

### Challenge 1

**Endpoint:**
http://40.65.179.25:3001/

**Hint:**  
*What you see may not always be what you get.*

---

### Challenge 2

**Endpoint:**
http://40.65.179.25:3002/

**Hint:**  
*Even trusted mechanisms can have overlooked details.*

---

### Challenge 3

**Endpoint:**
http://40.65.179.25:3003/

**Hint:**  
*Headers can carry more than just information.*

---

### Challenge 4

**Endpoint:**
http://40.65.179.25:3004/

**Hint:**  
*Sometimes, the key is simpler than you think.*

---

### Challenge 5

**Endpoint:**
http://40.65.179.25:3005/

**Hint:**  
*Some flaws hide in plain sight. Look closely.*

---

## Getting Started

1. Each lab is accessible at the endpoint and port listed above.
2. Explore the endpoints, review any available hints, and start hacking!
3. Standard tools and automation are allowed.
4. AI and code generation tools are permitted and encouraged.

---

## Connecting Your Solution

- Run a web server that exposes a **POST** endpoint at `/chasetheflag` (e.g., `http://<your-ip>/chasetheflag`).
- Accept incoming POST requests (no request body required).
- Respond with this JSON format:

    ```json
    {
      "challenge1": "your_flag_1",
      "challenge2": "your_flag_2",
      "challenge3": "your_flag_3",
      "challenge4": "your_flag_4",
      "challenge5": "your_flag_5"
    }
    ```

- Make sure the server is accessible at the endpoint and port you register.
- If you have not solved a challenge, leave its value as an empty or dummy string.

---
## Questions?

Feel free to visit this [link](https://teams.microsoft.com/l/meetup-join/19%3ameeting_ZDUyNDE0NmQtM2Q4MS00YmY5LWI4YWItMTExODhjMjE1OTY5%40thread.v2/0?context=%7b%22Tid%22%3a%22fb6ea403-7cf1-4905-810a-fe5547e98204%22%2c%22Oid%22%3a%22fd3f50c9-56c1-4a3f-b2ca-463e61077e37%22%7d) to join the teams chat to ask

---
## Tips (Spoilers Alert)

<details>
  <summary>Step 1</summary>
  Find the endpoint to call (Same for all challenges)
</details>

---

## Disclaimer

These challenges are for hackathon use only.  
Do not use any discovered techniques or vulnerabilities against any systems except these labs.

---

Good luck, and have fun!
