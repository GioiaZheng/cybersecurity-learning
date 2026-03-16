# **Defensive Security Intro — Practice Notes**

## **Task 1 — Understanding Defensive Security**

In this task, I explored the meaning of defensive security (blue teaming) and reviewed real-world examples of major data breaches.

These incidents demonstrated that poor defensive measures can lead to:

* data loss
* financial penalties
* reputational damage
* business disruption

This reinforced the importance of proactive, continuous defence.

---

## **Task 2 — Responsibilities of Defensive Security**

I reviewed the five fundamental responsibilities of defensive teams:

* **Monitoring & Detection** — identifying unusual logins, privilege changes, or suspicious behaviour
* **Incident Response (IR)** — containing, eradicating, and recovering from active threats
* **Threat Intelligence** — understanding attacker motivations, tools, and behaviour
* **Vulnerability Management** — reducing attack surface through scanning and remediation
* **Investigation & Analysis** — validating alerts, analysing logs, and distinguishing benign from malicious activity

This task also introduced key SOC roles such as:

* SOC Analysts
* Incident Responders
* Security Engineers
* Digital Forensics Specialists

---

## **Task 3 — Defensive Security in Practice**

I learned how organisations use **Defence in Depth**, implementing layered security controls so that if one defence fails, another continues protecting the system.

Examples explored:

* Employee cybersecurity awareness
* IDS monitoring network activity
* Firewalls filtering inbound and outbound traffic
* Security policies defining acceptable behaviour

This task also explained how a **SOC** operates and how **SIEM** platforms aggregate logs and alerts for efficient investigation.

---

## **Task 4 — Practical: Investigating a Web Discovery Attack**

In this hands-on simulation, I acted as a SOC Analyst responding to a **Web Discovery Attack** alert within the FakeBank environment.

### **1. Reviewing the Alert**

The SIEM generated an alert indicating directory enumeration against admin URLs.

Information included:

* attacker IP
* geolocation
* ASN and threat reputation
* attempted paths
* timestamps
* overall risk score

This helped assess the nature and urgency of the attack.

---

### **2. Analysing the Attack Summary**

The SIEM provided structured details:

* number of URLs scanned
* HTTP response codes (200 / 403 / 404)
* attack duration
* classification as automated scanning

This revealed a common directory enumeration pattern and highlighted risks posed by predictable admin paths.

---

### **3. Understanding Threat Intelligence**

Threat intelligence enriched the alert with:

* attacker reputation (malicious)
* known past incidents
* behavioural indicators
* regional threat context

This demonstrated how threat intel guides analysts in understanding attacker intent and risk level.

---

### **4. Taking Defensive Actions**

Following the guided steps, I implemented realistic defensive controls used in SOC operations:

#### **● Blocking the Source IP**

Prevents further scans or malicious requests.

#### **● Implementing Rate Limiting**

Mitigates automated scanning by restricting request frequency.

#### **● Updating WAF Rules**

Strengthens defences against repeated probing or suspicious patterns.

These actions reflect standard, real-world mitigation steps.

---

### **5. Closing the Investigation**

After applying defensive controls, I moved through the typical SOC workflow:

* changing alert status from *Unassigned → Investigating → Resolved*
* documenting all actions taken
* reviewing the event timeline to understand attack progression
* confirming containment and mitigation

The scenario ended with a summary confirming the incident was properly handled.

---

## **Key Lessons Learned**

* SIEM platforms provide central visibility for fast and structured investigations
* Attacks often follow detectable patterns, especially automated ones
* Defensive controls must be layered—no single measure is sufficient
* Rate limiting and WAF rules significantly slow or block repeated scans
* SOC workflows rely on consistent documentation and playbook execution
* Threat intelligence adds critical context to alerts and helps prioritise responses

This exercise provided hands-on insight into how Security Analysts investigate alerts and reinforced the analytical mindset required for blue team operations.
