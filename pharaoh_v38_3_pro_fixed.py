# PHARAOH V38.3 FIXED FINAL
import socket, time
from concurrent.futures import ThreadPoolExecutor

class DNSFixer:
    def fix(self):
        content = "nameserver 8.8.8.8\nnameserver 1.1.1.1\n"
        paths = ["/data/data/com.termux/files/usr/etc/resolv.conf", "/etc/resolv.conf"]
        log = "=== DNS PROOF " + time.ctime() + " ===\n"
        for p in paths:
            try:
                open(p, "w").write(content)
                v = open(p, "r").read()
                log += "[OK] " + p + " -> " + v + "\n"
                print("[OK] " + p)
            except Exception as e:
                log += "[FAIL] " + p + ": " + str(e) + "\n"
                print("[FAIL] " + p)
        try:
            ip = socket.gethostbyname("google.com")
            log += "RESOLVE google.com -> " + ip + "\n"
        except Exception as e:
            log += "RESOLVE FAIL " + str(e) + "\n"
        open("pharaoh_dns_proof.log", "w").write(log)
        print(log)

class PharaohEngine:
    TIMEOUT = 5
    def whois_real(self, domain):
        def q(srv, d):
            s = socket.socket()
            s.settimeout(5)
            s.connect((srv, 43))
            s.send((d + "\r\n").encode())
            data = b""
            while True:
                c = s.recv(4096)
                if not c:
                    break
                data += c
            s.close()
            return data.decode(errors="ignore")
        r1 = q("whois.iana.org", domain)
        ref = None
        for line in r1.splitlines():
            if "whois:" in line.lower():
                for w in line.split():
                    if "whois." in w and "iana" not in w:
                        ref = w.strip(", ")
        if ref:
            print("Referral -> " + ref)
            r2 = q(ref, domain)
            final = None
            for line in r2.splitlines():
                if "Registrar WHOIS Server:" in line:
                    final = line.split(":")[1].strip()
            if final:
                print("Final -> " + final)
                return q(final, domain)
            return r2
        return r1

    def port_scan_full(self, target):
        ports = list(range(1, 1025))
        print("Scanning " + str(len(ports)) + " ports on " + target)
        opens = []
        def scan(p):
            try:
                s = socket.socket()
                s.settimeout(0.8)
                s.connect((target, p))
                s.close()
                print("[OPEN] " + str(p))
                return p
            except:
                return None
        with ThreadPoolExecutor(max_workers=50) as ex:
            for r in ex.map(scan, ports):
                if r:
                    opens.append(r)
        print("DONE: " + str(opens))
        return opens

    def cors_check_fixed(self, url):
        import requests
        try:
            h = {"Origin": "https://evil.com"}
            r = requests.get(url, headers=h, timeout=5)
            acao = r.headers.get("Access-Control-Allow-Origin", "")
            print("CORS ACAO: " + acao)
            if "evil.com" in acao or acao == "*":
                print("[VULN] CORS")
                return True
            print("[SAFE]")
            return False
        except Exception as e:
            print(str(e))
            return False

if __name__ == "__main__":
    print("PHARAOH V38.3 FIXED READY")
    DNSFixer().fix()
