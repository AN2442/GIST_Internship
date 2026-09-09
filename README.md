# GIST_Internship
Cyber Security Internship | Global Institute of Science &amp; Technology | Sep'26 - Oct'26

## Tasks Selected

- Task 1 - Basic: Cybersecurity Awareness & Security Audit
- Task 2 - Intermediate: Password Security System
- Task 3 - Advanced+: Security Monitoring & Incident Response

# Cybersecurity Internship — Task Summary

## Task 1: Security Audit Report
Conducted a basic security audit of a local system using PowerShell. 

The audit examined four key areas: 
- system update status
- password hygiene
- open network ports
- firewall and accounts

The goal was to identify realistic, common weaknesses and propose practical fixes to reduce the overall attack surface.

## Task 2: Secure Password Management Demo

Developed a command-line Python application to demonstrate secure password management practices from scratch. 

- enforces password strength rules (minimum length, mix of uppercase, lowercase, numbers, and special characters)
- instead of storing raw passwords, it generates a unique random salt per user using Python's `secrets` module
- hashes the salted password with SHA-256
- login input is hidden from the screen using `getpass`
- authentication works by re-hashing the entered password with the stored salt and comparing it to the saved hash 

## Task 3: Simulated Security Monitoring & Incident Report
Simulated a basic security monitoring workflow by writing a Python script (using `re`, `collections`, and `datetime`) to analyze sample system logs and flag suspicious behavior. The script detected two notable incidents: a likely brute-force attack, where an admin account had multiple failed login attempts in quick succession followed by a successful login from the same IP; and a possible account compromise, where a user's credentials were used to access a sensitive payroll file from two different IP addresses, including one at an unusual hour. Each incident was documented with its risk level and recommended response — such as enforcing account lockout policies, enabling multi-factor authentication, and setting up real-time alerts for failed logins and anomalous file access patterns.
