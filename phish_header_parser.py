# Phishing Email Header Analyzer - Developed by Umutcan Korkmaz

def analyze_email(sender, spf_status, dkim_status):
    print(f"[*] Analyzing email from: {sender}")
    risk_score = 0
    
    if spf_status != "pass": risk_score += 40
    if dkim_status != "pass": risk_score += 40
    
    if risk_score >= 80:
        print("[RESULT] HIGH RISK: Potential Email Spoofing detected.")
    elif risk_score >= 40:
        print("[RESULT] MEDIUM RISK: Suspicious email, quarantine recommended.")
    else:
        print("[RESULT] CLEAN: Email passed security checks.")

analyze_email("ceo@yourbank-secure.com", "fail", "fail")
