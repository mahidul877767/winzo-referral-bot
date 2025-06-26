import requests, random, time, uuid

REFERRAL_URL = "https://winzo.onelink.me/gu8K/7xm60uuy"

user_agents = [
    "Dalvik/2.1.0 (Linux; Android 10; Redmi Note 8)",
    "Mozilla/5.0 (Linux; Android 11; vivo 1901)",
    "Mozilla/5.0 (Linux; Android 9; SM-J610F)"
]

def get_fake_headers():
    return {
        "User-Agent": random.choice(user_agents),
        "X-Device-ID": str(uuid.uuid4()),
        "Accept": "text/html",
        "Connection": "keep-alive"
    }

def simulate_referral():
    headers = get_fake_headers()
    try:
        res = requests.get(REFERRAL_URL, headers=headers, timeout=10)
        print(f"[✓] Hit {res.status_code} | UA: {headers['User-Agent']}")
    except Exception as e:
        print(f"[!] Failed: {e}")

if __name__ == "__main__":
    for _ in range(5):
        simulate_referral()
        time.sleep(random.randint(10, 30))
