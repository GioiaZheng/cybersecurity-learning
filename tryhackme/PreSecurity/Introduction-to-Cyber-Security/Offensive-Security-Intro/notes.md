# **Offensive Security Intro — Notes**

A foundational introduction to offensive security (ethical hacking), focusing on how attackers discover vulnerabilities and how ethical hackers use these techniques legally to help organisations improve security.

---

## **What This Page Covers**

* Definition and purpose of offensive security
* Key offensive concepts: reconnaissance, discovery, brute-force techniques
* Using command-line tools (e.g., dirb)
* Understanding hidden or misconfigured web pages
* The ethical hacking mindset and why offensive knowledge strengthens defence

---

## **1. What Is Offensive Security?**

Offensive security focuses on **identifying and exploiting vulnerabilities before real attackers do**.

Ethical hackers simulate attacks—legally and with permission—to:

* discover hidden weaknesses
* demonstrate realistic risks
* help organisations fix issues before they are exploited

The core principle is:

> **“To defend effectively, you must understand how attackers think.”**

---

## **2. Key Concepts Learned**

### **● Reconnaissance (Information Gathering)**

Every attack starts with reconnaissance.
Attackers explore a target website to find:

* hidden or unlinked pages
* admin or test pages
* misconfigurations
* input fields or behaviours that might expose weaknesses

Many vulnerabilities come from:

* predictable filenames
* leftover development pages
* forgotten admin routes

Understanding reconnaissance is essential because **attackers cannot exploit what they cannot find**.

---

### **● Brute-Force Discovery of Pages (dirb)**

One of the most useful techniques is brute-force discovery.

In this module, I used **dirb**, a tool that:

* takes a *wordlist* of common file and directory names
* tries each entry on the target server
* reports which URLs return valid responses (200/301/403, etc.)

This helps identify:

* hidden admin panels
* login pages
* test endpoints
* sensitive functions not linked in the UI

These pages often contain high-risk vulnerabilities.

---

### **● Using the Terminal**

Many offensive tools run through the command line.

In this exercise, I practiced:

* navigating directories
* running offensive tools (`dirb`)
* reading output and identifying useful results

Becoming comfortable with the terminal is essential for future offensive tasks such as exploitation, enumeration, scripting, and automation.

---

### **● Hidden Administrative Functions**

The lab demonstrated how attackers can find **secret admin pages** that are not shown to regular users.

If discovered, these hidden pages may allow:

* privileged actions (e.g., money deposit in the FakeBank scenario)
* account manipulation
* configuration changes
* full system compromise

This shows why **security by obscurity is not real security**.
Every endpoint must enforce proper authentication and access control.

---

### **● Ethical Hacking Mindset**

From this module, I learned the attack flow used by ethical hackers:

1. **Reconnaissance** — gather information
2. **Discovery** — find hidden or sensitive endpoints
3. **Automation** — use tools to expand coverage
4. **Exploitation** — test what is possible with the discovered pages

This mindset is essential before learning more advanced techniques such as SQL injection, authentication bypass, privilege escalation, etc.

---

## **3. Why Offensive Security Matters**

Learning offensive techniques strengthens security because it reveals:

* how attackers discover vulnerabilities
* why misconfigurations become dangerous
* how small oversights (like forgotten pages) lead to major risks
* the importance of access control and secure coding

Offensive knowledge is foundational for both red teaming and defensive roles like SOC analysis and incident response.

---

## **Key Takeaways**

* Attackers rely heavily on reconnaissance and discovery
* Tools like `dirb` reveal hidden pages that developers often forget
* Administrative pages must be protected with proper authentication
* The command line is an essential part of the offensive workflow
* Understanding attacks improves defensive strategies

---

## **Next Steps**

* Practice more enumeration tools (Gobuster, Nmap, ffuf)
* Explore web vulnerabilities (OWASP Top 10)
* Continue developing confidence with the terminal
* Begin learning basic scripting for automation
