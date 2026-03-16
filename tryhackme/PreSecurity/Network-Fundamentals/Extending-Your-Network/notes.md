# Extending Your Network — Notes

This module introduces key technologies used to extend, segment, and secure networks. Topics include port forwarding, firewalls, VPNs, routers, switches, and VLANs. Understanding these components is essential for modern network design and secure communication.

---

## 1. Port Forwarding

Port forwarding allows external users on the Internet to reach devices inside a private network.

### Purpose

Internal devices use **private IP addresses**, which are not reachable from the public Internet. The router has the only **public IP**.
Port forwarding tells the router:

> “When traffic arrives on this public port, forward it to this internal device and port.”

Example:
Public `82.62.51.70:80` → Internal server `192.168.1.10:80`

### How It Works

1. A client connects to the router’s public IP + port.
2. The router checks NAT and port-forwarding rules.
3. The packet is forwarded to the appropriate internal host.
4. The response is translated and returned to the client.

### Port Forwarding vs Firewall

| Feature   | Port Forwarding            | Firewall                           |
| --------- | -------------------------- | ---------------------------------- |
| Purpose   | Expose an internal service | Control/secure traffic             |
| Mechanism | NAT rule                   | Rule-based packet filtering        |
| Effect    | Makes services reachable   | Determines allowed/blocked traffic |

### Key Points

* Configured on the router
* Common when hosting web servers, game servers, SSH access, etc.
* Works together with firewall rules

---

## 2. Firewalls 101

A firewall determines which traffic may enter or leave a network. It acts as a filtering checkpoint.

Firewall decisions may rely on:

* Source and destination IP
* Port
* Protocol (TCP, UDP)

### Types of Firewalls

#### Stateful Firewall

* Tracks full connection context
* Understands TCP handshakes
* More secure but uses more resources

#### Stateless Firewall

* Evaluates each packet individually
* Uses static rules
* Faster but less intelligent
* Useful for high-volume filtering (e.g., DDoS mitigation)

### OSI Layers

Firewalls usually operate at:

* Layer 3 (Network – IP)
* Layer 4 (Transport – TCP/UDP ports)

### Key Points

* Port forwarding exposes services; the firewall decides whether to allow them
* Stateful = context-aware
* Stateless = packet-by-packet

---

## 3. VPN (Virtual Private Network)

A VPN creates an encrypted tunnel across the Internet, allowing devices to behave as if they are on the same private network.

### Why Use a VPN?

| Benefit                 | Description                                      |
| ----------------------- | ------------------------------------------------ |
| Connect remote networks | Links multiple offices or remote workers         |
| Privacy                 | Encrypted traffic protects against sniffing      |
| Anonymity               | ISPs and attackers cannot easily see activity    |
| Secure access           | Used by TryHackMe to reach isolated lab machines |

### VPN Technologies

#### PPP (Point-to-Point Protocol)

* Provides authentication and encryption
* Uses key pairs
* Not routable by itself

#### PPTP

* Encapsulates PPP so it can cross networks
* Simple but weak encryption

#### IPSec

* Encrypts at the IP layer
* Strong and widely supported
* More complex configuration

### Key Points

* VPNs secure data over untrusted networks
* IPSec is the strongest option
* Used for privacy, enterprise networking, and secure remote access

---

## 4. LAN Networking Devices

This section covers routers, switches, and VLANs—core elements in LAN architecture.

### Router

A router connects different networks and forwards packets based on IP routing.

* Operates at OSI Layer 3
* Uses routing tables and network metrics
* Chooses optimal paths between networks

### Switch

#### Layer 2 Switch

* Operates using MAC addresses
* Forwards frames within a LAN
* Does not perform routing

#### Layer 3 Switch

* Adds IP-level routing capabilities
* Combines switch performance with limited routing features

### VLAN (Virtual Local Area Network)

VLANs logically separate one physical network into multiple isolated segments.

Benefits:

* Improved security
* Reduced broadcast traffic
* Departmental separation (e.g., HR, Finance)

Example:

* VLAN 10 → 192.168.10.x
* VLAN 20 → 192.168.20.x

Different VLANs require routing to communicate.

### Key Points

* Routers connect networks; switches connect devices
* Layer 3 switches perform limited routing
* VLANs provide segmentation, organization, and security

---

## 5. Network Simulator — Understanding TCP Steps

The simulator demonstrates how traffic flows through networks and how protocols interact.

### ARP

Used to map an IP address to a MAC address before sending frames on a LAN.

### Routing

Traffic destined for another network is sent to the **default gateway** (router).

### TCP Three-Way Handshake

1. SYN
2. SYN/ACK
3. ACK

This establishes a reliable connection.

### Packet Flow Visualization

The simulator illustrates interactions between:

* Computers
* Switches
* Router
* ARP broadcasts/replies
* TCP packets and ACKs

Useful for understanding how networking components cooperate.

---

## Final Summary

This module covers essential network-extension and network-security mechanisms:

* Port forwarding makes internal services reachable from outside
* Firewalls filter and control network traffic
* VPNs create secure encrypted tunnels
* Routers and switches define how networks communicate
* VLANs segment networks for organization and security
* Simulated TCP and ARP flows help visualize real network behavior

Mastering these concepts builds a strong foundation for cybersecurity, networking, and penetration testing.
