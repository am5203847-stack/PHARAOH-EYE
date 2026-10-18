import requests
print("""
  ___ _  _   _   ___   _   _   _ 
 | _ \ || | /_\ | _ \ /_\ | | | |
 |  _/ __ / _ \|   // _ \| |_| |
 |_| |_||_/_/ \_\_|_\/_/ \_\___/
  PHARAOH-EYE v1.2 - Giza, Egypt
""")
t=input("Enter URL: ")
if not t.startswith("http"): t="https://"+t
r=requests.get(t,timeout=10)
print(f"Status: {r.status_code}")
print(f"Server: {r.headers.get('Server','Unknown')}")
