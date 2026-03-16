# **Offensive Security Intro — Practice Notes**

A practical introduction to offensive security techniques, focusing on reconnaissance, hidden-page discovery, and interacting with insecure functionalities inside a simulated banking application.
These tasks reinforced the attacker mindset: **discover → analyse → exploit → validate**.

---

## **What This Page Covers**

* Understanding the purpose of offensive security
* Using reconnaissance and enumeration tools (dirb)
* Identifying hidden or sensitive endpoints
* Interacting with insecure functionality to simulate exploitation
* Key lessons about why web applications must enforce proper access control

---

## **1. Task 1 — Understanding Offensive Security**

I reviewed the core idea of offensive security:
**ethical hackers simulate real attacker behaviour to find vulnerabilities before criminals do.**

Offensive security emphasizes:

* thinking like an attacker
* identifying weak points
* demonstrating real-world risk
* helping organisations strengthen defences

This task established the mindset needed for the rest of the lab.

---

## **2. Task 2 — Starting the Lab Environment**

I launched the TryHackMe virtual machine, which loaded the **FakeBank** application.
The dashboard included:

* account balance
* account number
* recent transaction history

This familiarisation step ensured I understood the normal user interface before attempting to discover hidden functionality.

---

## **3. Task 3 — Discovering Hidden Pages Using `dirb`**

The goal was to uncover unlinked or hidden pages in the FakeBank web app.

### **Steps Performed**

1. Opened the terminal in the VM
2. Ran the command:

   ```
   dirb http://MACHINE_IP
   ```
3. Observed how **dirb** iterated through the wordlist
4. Identified which paths responded with valid HTTP status codes

### **Key Insights**

* `dirb` brute-forces URLs by testing thousands of common filenames
* Hidden pages often expose forgotten or sensitive functionality
* Reconnaissance is always the **first step** in an attack chain

I omitted the specific discovered URLs to avoid including room-specific answers.

---

## **4. Task 4 — Interacting With a Sensitive Page**

After discovering a restricted administrative endpoint, I accessed it manually.

The page exposed privileged banking actions that should **never** be publicly accessible.
This demonstrated how insecure design can allow attackers to perform unauthorized operations.

### **Actions Completed**

* Navigated to the hidden admin page
* Interacted with the form following room instructions
* Observed the application response
* Returned to the account dashboard to confirm the change

### **What I Learned**

* Hidden URLs are **not** a security mechanism
* All sensitive functions require authentication & authorization
* Attackers can exploit predictable or discoverable endpoints
* Offensive security highlights how small design flaws create major vulnerabilities

The pop-up confirmation message (omitted here) validated that the exploitation succeeded.

---

## **Overall Skills Practiced**

This lab strengthened my understanding of the offensive workflow:

* thinking like an attacker while exploring a target
* using automated tools for reconnaissance
* identifying hidden and sensitive endpoints
* analysing insecure functionality
* validating the impact of exploitation

These exercises highlight why secure access control, least privilege, and proper endpoint protection are essential in real-world applications.
