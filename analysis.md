# Phishing Email Analysis

## 1. Initial Observation
The email claims urgent account compromise and pressures the user to take immediate action.

## 2. Sender Analysis
- Domain: micros0ft-support.com
- Observation: Typosquatted domain (Microsoft impersonation)
- Risk: HIGH

## 3. Header Indicators (Simulated)
- SPF: FAIL
- DKIM: NOT VERIFIED
- Reply-To mismatch detected

## 4. URL Analysis
- http://micros0ft-security-login.com/verify
- Suspicious characteristics:
  - Lookalike domain
  - HTTP (not HTTPS)
  - Credential harvesting intent

## 5. Social Engineering Tactics
- Urgency (“30 minutes” deadline)
- Fear-based messaging (account suspension)
- Authority impersonation (Microsoft branding)

## 6. Attack Chain
Email → User click → Fake login page → Credential theft attempt

## 7. Risk Assessment
Severity: HIGH
Impact: Potential account takeover

## 8. MITRE ATT&CK Mapping
- T1566.002 (Spearphishing Link)
- T1110 (Credential Access - Brute Force potential after phishing)

## 9. Decision
Email classified as malicious phishing attempt and should be blocked at gateway level.

## 10. Recommendation
- Block domain
- Add URL to threat intelligence feed
- User awareness training required
