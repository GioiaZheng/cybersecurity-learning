#  **Defensive Security Intro — Notes**

*A foundational overview of blue teaming, focusing on monitoring, detection, incident response, threat intelligence, and the core roles that protect organisations from cyber threats.*

---

## **What This Page Covers**

* Definition and purpose of defensive security
* Core responsibilities: monitoring, detection, IR, threat intelligence, vulnerabilities
* Key defensive tools (e.g., SIEM)
* Blue team roles in organisations
* Defence-in-Depth & SOC operations

---

# **1. What Is Defensive Security?**

**Defensive security (blue teaming)** focuses on protecting systems, networks, and data from attackers.
While offensive security *simulates* attacks, defensive security works in real time to:

* **Detect** suspicious activity
* **Prevent** attacks
* **Respond** and recover from incidents

Poor defensive posture can cause:

* Data breaches
* Ransomware outbreaks
* Regulatory penalties
* Financial & reputational loss

Good defensive security ensures business continuity and resilience.

---

# **2. Core Responsibilities of Defensive Security**

---

## **● Monitoring & Detection**

Continuous observation of system and network behaviour to identify anomalies.

Examples of suspicious indicators:

* Impossible travel logins
* Sudden privilege escalation
* Unusual outbound traffic
* Repeated failed logins

**Primary Tool:**
➡ **SIEM (Security Information & Event Management)** — correlates logs and detects threats.

**Goal:** Detect threats **as early as possible**.

---

## **● Incident Response (IR)**

A structured process activated when malicious activity is confirmed.

**Incident Response Lifecycle:**

1. **Identify** indicators of compromise (IoCs)
2. **Contain** the threat to prevent spread
3. **Eradicate** malicious components
4. **Recover** systems & validate integrity
5. **Lessons Learned** — update policies & defences

**Goal:** minimise impact and restore operations quickly.

---

## **● Threat Intelligence**

Understanding attackers by analysing:

* Tactics, techniques, and procedures (TTPs)
* Motivations & target industries
* Global attack trends

Threat intel helps anticipate attack patterns and strengthen defences.

---

## **● Vulnerability Management**

Finding and fixing weaknesses before attackers exploit them.

**Steps:**

1. **Scanning**
2. **Assessment & Prioritisation**
3. **Remediation** (patching, config changes)
4. **Re-testing**

**Common Tools:**

* Nessus
* OpenVAS
* Qualys

**Goal:** reduce overall attack surface.

---

## **● Investigation & Analysis**

Blue team members analyse logs, alerts, and behaviours to determine:

* valid events
* false positives
* true malicious activity

This requires correlation, pattern recognition, and analytical thinking.

---

# **3. Defensive Security Roles**

### **● SOC Analyst (Tier 1 / Tier 2)**

* Monitors alerts
* Investigates suspicious events
* Escalates confirmed incidents

### **● Incident Responder**

* Contains and mitigates attacks
* Coordinates eradication and recovery

### **● Security Engineer**

* Builds and maintains defensive tools (SIEM, EDR, firewalls)
* Automates detection & response

### **● Digital Forensics Specialist**

* Preserves and analyses digital evidence
* Reconstructs how incidents occurred

These roles collectively maintain an organisation’s defensive posture.

---

# **4. Defensive Security in Practice**

Organisations rely on **Defence in Depth**, meaning layered security controls.

If one fails, others continue protecting the system.

Examples:

* Security awareness training
* Firewalls & IDS/IPS
* Endpoint protection (EDR)
* Network segmentation
* Strict access control policies

Security is strongest when controls overlap.

---

# **5. Security Operations Centre (SOC)**

The SOC is the **command centre** of defensive security.

A SOC analyst typically:

* reviews SIEM alerts
* investigates anomalies
* coordinates incident response
* provides 24/7 monitoring

SOC work requires strong communication, teamwork, and continuous learning.

---

# **6. SIEM — The Core of Defensive Detection**

A **SIEM** collects logs from across an organisation and provides:

* centralised visibility
* correlation of events
* anomaly detection
* automated alerting
* prioritised investigations

**Common SIEM Platforms:**

* Splunk
* Elastic Stack
* Microsoft Sentinel
* IBM QRadar

SIEMs function like the **radar system** for defenders.

---

# **Key Takeaways**

* Defensive security protects organisations from real-world threats
* Blue teams focus on detection, investigation, and response
* Tools like SIEM, IR frameworks, and vulnerability scanners are essential
* Defence-in-Depth creates stronger layered protection
* SOC analysts, IR responders, engineers, and forensics specialists form the defence ecosystem

---

# **Next Steps**

* Study MITRE ATT&CK to understand attacker behaviour
* Practice analysing logs and SIEM alerts
* Continue the Pre-Security pathway modules
* Explore SOC Level 1 learning routes on TryHackMe
