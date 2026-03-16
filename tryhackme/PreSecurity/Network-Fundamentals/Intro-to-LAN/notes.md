# Intro to LAN — Notes

A focused introduction to Local Area Networks (LANs), common network topologies, and the core protocols that let devices talk to each other inside a network.

---

## Task 1 — LAN Topologies

### 1. Star Topology
All devices are connected to a **central device** (switch or hub).

**Pros**
- Easy to add/remove devices
- Simple to troubleshoot (issues usually local to one cable/device)
- Scales well for modern networks

**Cons**
- Requires more cabling and hardware → more expensive
- **Single point of failure**: if the central device dies, the whole network is down

---

### 2. Bus Topology
All devices share **one main cable** (the “backbone”).

**Pros**
- Cheap to build (less cabling, minimal hardware)
- Simple layout

**Cons**
- All data travels over the same cable → easily **bottlenecked**
- Hard to troubleshoot when something goes wrong
- Another single point of failure: if the backbone cable breaks, the whole network fails

---

### 3. Ring Topology
Each device is connected to **two neighbours**, forming a loop. Data travels around the ring until it reaches the destination.

**Pros**
- Less chance of congestion than a bus (traffic flows in one direction)
- Easier to predict data paths

**Cons**
- If **one cable or device breaks, the whole ring is broken**
- Data may need to pass through many devices before reaching the target → less efficient

---

### 4. Hubs, Switches, Routers (Quick Overview)

- **Hub**
  - Very basic device
  - Forwards incoming packets to **all** ports (no intelligence)
  - Causes a lot of unnecessary traffic

- **Switch**
  - Understands **MAC addresses**
  - Learns which device is on which port and only sends frames to the correct destination
  - Much more efficient than a hub

- **Router**
  - Connects **different networks** together (e.g. home network ↔ Internet)
  - Uses **IP addresses** and routing tables to decide where to send traffic

---

### Practical Lab — “Topology Flaws”

The interactive lab showed typical weaknesses:

- **Ring topology**
  - Cutting a single cable stops packets from travelling around the ring
  - Result: no device can talk to any other

- **Bus topology**
  - All devices share one cable
  - Sending lots of packets very quickly can **overload** the backbone and take the network down

Main lesson:  
> Different designs have different failure points. Good network design tries to reduce single points of failure and bottlenecks.

---

## Task 2 — A Primer on Subnetting

**Subnetting** = splitting a larger network into **smaller logical networks** (subnets).

### Subnet Mask & IP Basics
- Both an IP address and a subnet mask are made of **4 octets** (32 bits total)
- An octet in a subnet mask ranges from **0–255**
- The subnet mask is used to decide:
  - **Network address** (which network)
  - **Host address** (which device inside that network)
  - **Default gateway** (where to send traffic that is leaving the network)

| Type             | Purpose                                      | Example         |
|------------------|----------------------------------------------|-----------------|
| Network Address  | Identifies the start of the network          | 192.168.1.0     |
| Host Address     | Identifies an individual device on the subnet| 192.168.1.100   |
| Default Gateway  | Device that forwards traffic to other networks| 192.168.1.254   |

### Why subnet?
- **Efficiency** – better organisation of many devices
- **Security** – separate guest users from internal staff, etc.
- **Control** – different rules for different departments (HR, Finance, etc.)

---

## Task 3 — ARP (Address Resolution Protocol)

Devices use two kinds of identifiers:

- **IP address** → logical identifier (where on the network)
- **MAC address** → physical identifier (hardware interface)

ARP links these two together.

### How ARP Works

1. **ARP Request**
   - A device broadcasts:  
     *“Who has IP address X.X.X.X? Tell me your MAC address.”*

2. **ARP Reply**
   - The device with that IP responds with its **MAC address**.
   - The requester stores the mapping in its **ARP cache** for future use.

Key ideas:
- ARP lets devices find the **MAC address** that matches a known **IP address**.
- MAC address = **physical identifier**  
- IP address = **logical identifier**

---

## Task 4 — DHCP (Dynamic Host Configuration Protocol)

Instead of manually configuring IP addresses on every device, we can use **DHCP** to assign them automatically.

### The DORA Process

1. **Discover**  
   New device broadcasts: “Is there any DHCP server? I need an IP!”

2. **Offer**  
   DHCP server replies with an offered IP address (e.g. 192.168.1.10).

3. **Request**  
   Device replies: “I’d like to use that IP address, please.”

4. **ACK (Acknowledgement)**  
   Server confirms: “OK, you can use this IP for a certain time (lease).”

After the ACK, the device can start using its IP address on the network.

---

## Task 5 — Next Step: OSI Model

The room ends by directing you to the **OSI Model** room.  
From here, the goal is to understand *how* data actually travels between devices, layer by layer.

---

## Key Takeaways

- LAN topologies (star, bus, ring) all have different strengths and failure points.
- A **switch** is smarter than a hub and reduces unnecessary traffic.
- **Routers** connect different networks and use IP addresses for routing.
- **Subnetting** organises and secures networks using subnet masks, network addresses, host addresses, and default gateways.
- **ARP** maps IP addresses to MAC addresses so data can be delivered to the correct physical device.
- **DHCP** automatically hands out IP configuration using the Discover → Offer → Request → ACK sequence.
