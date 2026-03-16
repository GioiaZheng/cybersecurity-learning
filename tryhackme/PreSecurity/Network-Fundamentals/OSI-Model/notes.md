#  OSI Model — TryHackMe Notes

A clean and structured summary of the OSI Model learned from the TryHackMe room.  
✔️ No flags included  
✔️ Concept-first explanation  
✔️ Practical understanding through the **OSI Dungeon** game  

---

## One-Sentence Summary of the OSI Model
**Application → Presentation → Session → Transport → Network → Data Link → Physical**

From **what the user does**, to **how data is formatted**, to **maintaining the connection**, to  
**choosing reliable or fast delivery**, to **routing across networks**, to **local MAC delivery**, and finally **electrical signals**.

---

# OSI Model

Room: **OSI Model** on TryHackMe  
Module: **Pre Security → Network Fundamentals**

This folder contains my notes and reflections about the OSI model.  
I don't include any flags or exact task answers here – only the concepts I learned and how I understood them.

## Learning Goals

- Understand the **7 layers** of the OSI model and what each layer is responsible for.
- Be able to **name the layers in order** (top–down and bottom–up).
- Connect common **protocols and examples** to the correct layer.
- Practise thinking in layers with the little game **“OSI Dungeon”**.

## Personal Takeaways

- Thinking in **layers** makes complex networking much easier: each layer has a clear job.
- The names are not random – they describe **what happens to the data** at that step (physical signals → frames → packets → segments → sessions → format → user interaction).
- I should always be able to:
  - list the 7 layers **in order**
  - explain each layer in **one simple sentence**
  - give at least **one real-world example** for every layer

---

# OSI Model – Layer-by-Layer Notes

The OSI (Open Systems Interconnection) model is a **conceptual framework** that describes how data moves from one device to another over a network.  
It has **7 layers**. Each layer has its own responsibilities and talks to the layers directly above and below it.

---

## Overview – 7 Layers (top → bottom)

1. **Application**
2. **Presentation**
3. **Session**
4. **Transport**
5. **Network**
6. **Data Link**
7. **Physical**

A popular mnemonic (top → bottom):  
> **A**ll **P**eople **S**eem **T**o **N**eed **D**ata **P**rocessing

---

## Layer 7 – Application

- **What it is:** The layer closest to the user. It defines how software should interact with the network.
- **Main job:** Provide **network services to applications**.
- **Examples:** web browsers, email clients, file transfer clients.
- **Typical protocols:** HTTP/HTTPS, FTP, SMTP, DNS, etc.
- **My mental model:** “What does the user think they are doing?” – visiting a website, sending an email, downloading a file.

---

## Layer 6 – Presentation

- **What it is:** The “translator” layer between the Application and the rest of the network.
- **Main job:** 
  - Convert data formats (encoding/decoding, compression).
  - Handle **encryption/decryption** (for example HTTPS).
- **Examples:** data being turned into a standard format that both sides understand.
- **My mental model:** “Make sure we both speak the same language and apply security.”

---

## Layer 5 – Session

- **What it is:** The layer that manages **connections (sessions)** between two devices.
- **Main job:**
  - Create, maintain, and close sessions.
  - Can use checkpoints or recovery points.
- **Key idea:** While a session is active, data can flow back and forth. When it is not needed anymore, the session is closed.
- **My mental model:** “Start the conversation, keep it alive, and hang up when finished.”

---

## Layer 4 – Transport

- **What it is:** Responsible for the **reliable or unreliable** delivery of data between devices.
- **Main protocols:**
  - **TCP (Transmission Control Protocol)**
    - Reliable, connection-oriented.
    - Guarantees data order and checks for errors.
    - Used for emails, file downloads, web pages when accuracy matters.
  - **UDP (User Datagram Protocol)**
    - Faster, connectionless, “best effort”.
    - Does not guarantee delivery or order.
    - Used for streaming, online games, VoIP where speed is more important than perfection.
- **My mental model:** “Break the data into segments and choose between **reliability (TCP)** or **speed (UDP)**.”

---

## Layer 3 – Network

- **What it is:** Handles **routing** – deciding where packets should go across different networks.
- **Main job:**
  - Use **IP addresses** to identify devices across networks.
  - Choose the most appropriate path (shortest, most reliable, fastest).
- **Example protocols:** OSPF (Open Shortest Path First), RIP (Routing Information Protocol).
- **Devices:** Routers (Layer 3 devices).
- **My mental model:** “Find a path from A to B across many networks using IP addresses.”

---

## Layer 2 – Data Link

- **What it is:** Focuses on the **physical addressing** and local delivery on the same network.
- **Main job:**
  - Use **MAC addresses** to identify devices on the local network.
  - Package data into **frames**.
- **Devices:** Switches, Network Interface Cards (NICs).
- **Key concepts:** 
  - Each NIC has a unique MAC address burned in by the manufacturer.
  - Frames are delivered from one MAC address to another.
- **My mental model:** “On this local network, who exactly should receive this frame?”

---

## Layer 1 – Physical

- **What it is:** The lowest layer, dealing with the **actual physical components**.
- **Main job:**
  - Transmit raw bits (0s and 1s) using electrical/optical/radio signals.
- **Examples:** Ethernet cables, fibre, Wi-Fi radio, hubs, connectors.
- **My mental model:** “Convert bits into signals on a real medium.”

---

## Quick Summary Table

| Layer | Name         | Key Focus                 | Typical Examples                          |
|------:|--------------|---------------------------|-------------------------------------------|
| 7     | Application  | User network services     | HTTP, FTP, SMTP, DNS, browsers, email    |
| 6     | Presentation | Translation, encryption   | SSL/TLS, data formats, compression       |
| 5     | Session      | Sessions, start/close     | Session management in apps               |
| 4     | Transport    | Segments, reliability     | TCP, UDP                                  |
| 3     | Network      | Routing, IP addressing    | IP, OSPF, RIP, routers                   |
| 2     | Data Link    | MAC addressing, frames    | Switches, NICs, Ethernet                 |
| 1     | Physical     | Signals, media, hardware  | Cables, hubs, Wi-Fi radio                |


## TCP/IP vs OSI Model — Comparison Table

| OSI Layer | Function | TCP/IP Layer | Notes |
|-----------|----------|--------------|-------|
| 7. Application | User network services | Application | Merged (includes OSI 5–7) |
| 6. Presentation | Formatting, encryption | Application | - |
| 5. Session | Connection management | Application | - |
| 4. Transport | TCP/UDP reliability | Transport | Same |
| 3. Network | Routing (IP) | Internet | Same role |
| 2. Data Link | MAC/frame delivery | Link | Merged with Physical |
| 1. Physical | Signals, hardware | Link | Merged with Data Link |

### Memory Trick
**TCP/IP = 7 layers → 4 layers (3 merged, 2 merged)**    
Application = OSI 7/6/5  
Transport = OSI 4  
Internet = OSI 3  
Link = OSI 2/1

---

## Things I want to be able to answer quickly

- List all 7 layers in order (top ↓ bottom and bottom ↑ top).
- For each layer:
  - one **short sentence** to describe its job,
  - at least **one protocol or example**.
- Decide if a problem is likely at Layer 1–2 (cables, switch, MAC) or 3–4 (IP, routing, TCP/UDP) or 5–7 (apps, format, sessions).

---

# OSI Dungeon – Game Notes

The room also contains a small retro game called **OSI Dungeon**.  
The idea is to escape a dungeon by choosing the correct door on each floor.

Each door is labelled with one OSI layer.  
To escape, I have to move through the layers **in the correct OSI order**.

## What I had to do

- Use the arrow keys to move left and right.
- Press the jump key (space bar) to enter a door.
- On each floor, choose the door corresponding to the **next OSI layer** in the sequence.

Order from top (Layer 7) to bottom (Layer 1):

1. Application  
2. Presentation  
3. Session  
4. Transport  
5. Network  
6. Data Link  
7. Physical  

I am **not** writing the final flag here on purpose – this file is only for learning, not for storing answers.

## What the game reinforces

- I need to **remember the order** of the OSI layers without looking.
- I must recognise the **names** quickly (e.g., not confusing “Presentation” and “Session”).
- It gives me a physical feeling of "going down" the stack from Application to Physical.

## Reflection

After playing the game I can:

- recite the 7 layers from memory (both directions),
- group real protocols into the right layer,
- and visualise data going down the stack when leaving my device and up the stack when arriving at the destination.
