import re
from collections import defaultdict
from datetime import datetime

LOG_FILE = "sample_logs.txt"
FAILED_LOGIN_THRESHOLD = 4   # alert if a user/IP fails this many times or more
ALERTS = []

def parse_log_line(line):
    pattern = r"(\S+ \S+) (\w+) user=(\S+)(?: file=(\S+))? ip=(\S+)"
    match = re.match(pattern, line)
    if match:
        timestamp, event, user, file, ip = match.groups()
        return {
            "timestamp": timestamp,
            "event": event,
            "user": user,
            "file": file,
            "ip": ip
        }
    return None

def analyze_logs(filepath):
    failed_attempts = defaultdict(int)
    entries = []

    with open(filepath, "r") as f:
        for line in f:
            entry = parse_log_line(line.strip())
            if entry:
                entries.append(entry)

    # Rule 1: Repeated failed logins = possible brute force
    for entry in entries:
        if entry["event"] == "LOGIN_FAILED":
            key = (entry["user"], entry["ip"])
            failed_attempts[key] += 1

    for (user, ip), count in failed_attempts.items():
        if count >= FAILED_LOGIN_THRESHOLD:
            ALERTS.append(f"[HIGH] Possible brute-force attack: user='{user}' from ip={ip} "
                           f"had {count} failed login attempts.")

    # Rule 2: Same user accessing files from two different IPs = possible account compromise
    user_file_ips = defaultdict(set)
    for entry in entries:
        if entry["event"] == "FILE_ACCESS":
            user_file_ips[entry["user"]].add(entry["ip"])

    for user, ips in user_file_ips.items():
        if len(ips) > 1:
            ALERTS.append(f"[MEDIUM] User '{user}' accessed sensitive files from multiple "
                           f"IP addresses: {', '.join(ips)}. Possible compromised account.")

    return entries

def generate_report(entries):
    print("\n===== SECURITY MONITORING REPORT =====")
    print(f"Total log entries analyzed: {len(entries)}")
    print(f"Total alerts generated: {len(ALERTS)}\n")

    if not ALERTS:
        print("No suspicious activity detected.")
    else:
        for alert in ALERTS:
            print(alert)

    print("\n===== RECOMMENDATIONS =====")
    print("- Enable account lockout after 3-5 failed login attempts.")
    print("- Enable multi-factor authentication (MFA) for all accounts.")
    print("- Alert on file access from new/unrecognized IP addresses.")
    print("- Review and rotate credentials for accounts with brute-force attempts.")

if __name__ == "__main__":
    entries = analyze_logs(LOG_FILE)
    generate_report(entries)