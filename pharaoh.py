import socket, requests
from datetime import datetime

print("""
  👁️ PHARAOH-EYE v1.1 by CYBER PHARAOH 👁️

  Creator: adel.mahmoud.eg.89
  Level: 7 ROOT - GIZA

""")

target = input(" [+] Enter domain (ex: google.com): ")
try:
    ip = socket.gethostbyname(target)
    print(f"\n [✓] IP: {ip}")
    r = requests.get(f"https://{target}", timeout=5)
    print(f" [✓] Server: {r.headers.get('Server','Hidden')}")
    print(f" [✓] Date: {datetime.now()}")
    print("\n [👑] PHARAOH-EYE - Made in GIZA!")
except Exception as e:
    print(f" [!] Error: {e}")
