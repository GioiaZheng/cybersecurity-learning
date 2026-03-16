# **Packets & Frames —  Notes**

A structured summary of everything I learned from the **Packets & Frames** room on TryHackMe.
✔️ No flags included
✔️ Concept-focused
✔️ Simple explanations for quick revision

---

#  What Are Packets & Frames?

In networking, data is **not** sent as one huge message.
Instead, large data is broken down into many **small pieces** so that the network stays fast, stable, and efficient.

There are **two main units** of data:

## **Packet**

* Belongs to **OSI Layer 3 – Network Layer**
* Contains:

  * **IP header**
  * **Payload (data)**
* Uses **IP addresses** (Source IP, Destination IP)
* Used for routing across different networks

## **Frame**

* Belongs to **OSI Layer 2 – Data Link Layer**
* Contains:

  * MAC addresses
  * Additional Layer 2 information
* Used **only inside the same local network (LAN)**

**Simple analogy:**
Packet = the letter
Frame = the envelope used to deliver the letter to the next device

When the envelope is removed, what’s left is the packet.
This process is called **encapsulation → decapsulation**.

---

#  Why Break Data Into Packets?

* Prevents network congestion
* Helps recover lost data more easily
* Makes routing efficient
* Allows billions of devices to communicate at scale
* Works like downloading an image: small parts arrive, then reassemble into the full picture

---

#  Common Packet Headers

| Header                  | Meaning                                                                           |
| ----------------------- | --------------------------------------------------------------------------------- |
| **Time To Live (TTL)**  | Prevents packets from looping forever; expires packet after a set number of hops. |
| **Checksum**            | Ensures integrity — detects corruption.                                           |
| **Source Address**      | Sender’s IP.                                                                      |
| **Destination Address** | Receiver’s IP.                                                                    |

---

#  TCP/IP – How Packets Travel Reliably

TCP is a **connection-based** protocol. It requires a handshake before sending data.

##  Three-Way Handshake (Connection Setup)

1. **SYN** → Client asks to start a connection
2. **SYN/ACK** → Server confirms
3. **ACK** → Client final confirmation

Connection is now established ✔

##  Closing a Connection

1. **FIN**
2. **ACK**
3. **FIN**
4. **ACK**

TCP ensures:

* Data arrives in order
* No data is missing
* No corruption

---

#  UDP/IP – Fast but Unreliable

UDP is **stateless** and **connectionless**.

###  Advantages:

* Very fast
* Low overhead
* Perfect for video calls, streaming, games

###  Disadvantages:

* No guarantee the data arrives
* No ordering
* No connection management

Used when **speed > reliability**.

---

#  Ports — Identifying Applications on a Device

A **port** is a number between **0–65535** that identifies a network service.

Think of:

* IP address = building
* Port number = apartment number

###  Well-known Ports

| Protocol  | Port | Purpose               |
| --------- | ---- | --------------------- |
| **FTP**   | 21   | File transfers        |
| **SSH**   | 22   | Secure remote login   |
| **HTTP**  | 80   | Web traffic           |
| **HTTPS** | 443  | Encrypted web traffic |
| **SMB**   | 445  | File sharing on LAN   |
| **RDP**   | 3389 | Remote Desktop        |

---

#  Practical: Connecting to a Port

You can connect to an IP and port using:

```
nc <IP> <port>
```

Example:

```
nc 8.8.8.8 1234
```

---

#  Personal Takeaways

* I can now explain the difference between **packets (Layer 3)** and **frames (Layer 2)**
* I understand why small data pieces are used to make networks faster
* I can describe TCP vs UDP clearly and know when each is used
* I can identify common ports and what applications use them
* I learned how to connect to a specific port using `nc`
