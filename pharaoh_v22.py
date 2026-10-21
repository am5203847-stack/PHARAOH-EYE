import requests, concurrent.futures, json
from datetime import datetime

# الوان
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
W = "\033[0m"

SITES = {
    "TikTok": {"url": "https://www.tiktok.com/@{}", "err": "Couldn't find this account"},
    "Instagram": {"url": "https://www.instagram.com/{}/", "err": "Sorry, this page isn't available"},
    "Facebook": {"url": "https://www.facebook.com/{}/", "err": "This page isn't available"},
    "YouTube": {"url": "https://www.youtube.com/@{}", "err": "This channel doesn't exist"},
    "GitHub": {"url": "https://github.com/{}", "err": "Page not found"},
    "Reddit": {"url": "https://www.reddit.com/user/{}/", "err": "Sorry, nobody on Reddit goes by that name"},
    "Twitter": {"url": "https://twitter.com/{}", "err": "This account doesn't exist"},
    "Twitch": {"url": "https://www.twitch.tv/{}", "err": "This channel does not exist"},
    "Pinterest": {"url": "https://www.pinterest.com/{}/", "err": "Oops! That page doesn't exist"},
    "Steam": {"url": "https://steamcommunity.com/id/{}", "err": "The specified profile could not be found"},
    "Telegram": {"url": "https://t.me/{}", "err": "If you have Telegram, you can contact"},
    "Spotify": {"url": "https://open.spotify.com/user/{}", "err": "Page not found"},
    "Medium": {"url": "https://medium.com/@{}", "err": "404"},
    "Trello": {"url": "https://trello.com/{}/", "err": "board not found"},
    "Duolingo": {"url": "https://www.duolingo.com/profile/{}", "err": "404"},
    "Kik": {"url": "https://kik.me/{}", "err": "The page you requested was not found"},
    "Tinder": {"url": "https://tinder.com/@{}", "err": "Looking for Someone?"},
    "TikTok2": {"url": "https://www.tiktok.com/@{}", "err": "Couldn't find this account"},
    "LinkedIn": {"url": "https://www.linkedin.com/in/{}/", "err": "This page doesn't exist"},
    "SoundCloud": {"url": "https://soundcloud.com/{}", "err": "We can't find that page"},
    "Vimeo": {"url": "https://vimeo.com/{}", "err": "Sorry, we couldn't find that page"},
    "Behance": {"url": "https://www.behance.net/{}", "err": "Oops! We can't find that page"},
    "Dribbble": {"url": "https://dribbble.com/{}", "err": "Whoops, that page is gone"},
    "Patreon": {"url": "https://www.patreon.com/{}", "err": "404"},
    "DeviantArt": {"url": "https://{}.deviantart.com", "err": "This page cannot be found"},
    "Keybase": {"url": "https://keybase.io/{}", "err": "404"},
    "Roblox": {"url": "https://www.roblox.com/user.aspx?username={}", "err": "Page cannot be found"},
    "GitLab": {"url": "https://gitlab.com/{}", "err": "404"},
    "HackerNews": {"url": "https://news.ycombinator.com/user?id={}", "err": "No such user"},
    "Wattpad": {"url": "https://www.wattpad.com/user/{}", "err": "Page not found"},
    "Flickr": {"url": "https://www.flickr.com/people/{}/", "err": "Page not found"},
    "500px": {"url": "https://500px.com/p/{}", "err": "No such user"},
    "AboutMe": {"url": "https://about.me/{}", "err": "page not found"},
    "CodePen": {"url": "https://codepen.io/{}", "err": "404"},
    "Replit": {"url": "https://replit.com/@{}", "err": "404"},
    "Kaggle": {"url": "https://www.kaggle.com/{}", "err": "404"},
    "BuyMeACoffee": {"url": "https://www.buymeacoffee.com/{}", "err": "404"},
    "Gravatar": {"url": "https://en.gravatar.com/{}", "err": "Profile not found"},
    "Pastebin": {"url": "https://pastebin.com/u/{}", "err": "Not Found"},
    "Imgur": {"url": "https://imgur.com/user/{}", "err": "Couldn't find that account"},
    "Wikipedia": {"url": "https://en.wikipedia.org/wiki/User:{}", "err": "Wikipedia does not have a user page"},
    "Slack": {"url": "https://{}.slack.com", "err": "404"},
    "Discord": {"url": "https://discord.com/users/{}", "err": "404"},
    "Notion": {"url": "https://www.notion.so/{}", "err": "404"},
    "ProductHunt": {"url": "https://www.producthunt.com/@{}", "err": "Page not found"},
    "VK": {"url": "https://vk.com/{}", "err": "404"},
    "Odysee": {"url": "https://odysee.com/@{}:f", "err": "404"},
    "Rumble": {"url": "https://rumble.com/user/{}", "err": "404"},
    "CashApp": {"url": "https://cash.app/${}", "err": "404"},
    "Chess": {"url": "https://www.chess.com/member/{}", "err": "404"}
}

def check(site, data, username):
    url = data["url"].format(username)
    try:
        r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=12)
        if r.status_code == 200 and data["err"].lower() not in r.text.lower():
            print(f"{G}[FOUND] {site} => {url}{W}")
            return (site, url, True)
        else:
            print(f"{R}[NOT FOUND] {site}{W}")
            return (site, url, False)
    except:
        print(f"{Y}[ERROR] {site}{W}")
        return (site, url, False)


print(f"{Y}{'='*45}")
print(" PHARAOH EYE V22 GOD MODE - 50 SITES")
print(f"{'='*45}{W}")
user = input(f"\n{Y}[+]{W} Enter Username: ").strip()
print(f"\n{Y}[*] Scanning {user} on {len(SITES)} sites...{W}\n")

found = []
with concurrent.futures.ThreadPoolExecutor(max_workers=15) as ex:
    tasks = {ex.submit(check, s, d, user): s for s, d in SITES.items()}
    for t in concurrent.futures.as_completed(tasks):
        site, url, ok = t.result()
        if ok:
            found.append((site, url))

print(f"\n{Y}{'='*45}")
print(f" Done! Found {len(found)}/50")
print(f"{'='*45}{W}")

filename_txt = f"PHARAOH-V22-{user}.txt"
filename_json = f"PHARAOH-V22-{user}.json"

with open(filename_txt, "w", encoding="utf-8") as f:
    f.write(f"PHARAOH EYE V22 GOD MODE\nUsername: {user}\nFound: {len(found)}/50\n\n")
    for s, u in found:
        f.write(f"{s}: {u}\n")

with open(filename_json, "w", encoding="utf-8") as f:
    json.dump(found, f, indent=2)

print(f"\n{G}[+] TXT: {filename_txt}")
print(f"[+] JSON: {filename_json}{W}")
