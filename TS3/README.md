# Incident Report — Simulated Security Monitoring

## Summary
A log analysis script was run against simulated system logs to detect suspicious activity.
The alerts were generated.

## Incident 1: Possible Brute-Force Attack
- **Detected:** Repeated failed login attempts for user 'admin' from IP 192.168.1.50
  (5 failures within seconds), followed by a successful login.
- **Risk:** High — indicates a password-guessing attack that succeeded.
- **Recommended action:** Force password reset for 'admin', enable account lockout
  after 3-5 failed attempts, enable MFA.

## Incident 2: Possible Account Compromise
- **Detected:** User 'jsmith' accessed the same sensitive file (payroll.xlsx) from two
  different IP addresses, one at an unusual time (3:15 AM).
- **Risk:** Medium — may indicate stolen credentials being used from a new location.
- **Recommended action:** Verify with the user whether this access was legitimate,
  monitor the second IP, consider forcing re-authentication for sensitive file access.

## Overall Recommendations
- Implement account lockout policies.
- Enable MFA across all accounts.
- Set up real-time alerting for repeated failed logins.
- Monitor file access patterns for anomalies (new IPs, odd hours).

## Tools/Technologies Used
- Python 3 (re, collections, datetime)
- Simulated log data