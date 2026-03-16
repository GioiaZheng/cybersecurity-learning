# DNS in Detail — Notes

A structured overview of how the Domain Name System works, including hierarchy, record types, and the full request/lookup process.

---

## Task 1 — What Is DNS?

DNS (Domain Name System) translates human-friendly domain names into IP addresses.
Instead of remembering `104.26.10.229`, users can simply type `tryhackme.com`.

Every device on the internet has a unique IP address. DNS provides the mechanism to map names → addresses.

---

## Task 2 — Domain Hierarchy

DNS naming follows a strict hierarchy:

```
Root (.)
 ├── Top-Level Domain (TLD)
 │      .com, .edu, .gov, .mil, .uk
 │
 ├── Second-Level Domain (SLD)
 │      tryhackme, google, nasa
 │
 └── Subdomain
        admin.tryhackme.com
```

### TLD (Top-Level Domain)

* The rightmost part of a domain, e.g., `.com`
* Two types:

  * **gTLD** (Generic TLD): `.com`, `.org`, `.edu`
  * **ccTLD** (Country Code TLD): `.uk`, `.ca`, `.it`

### Second-Level Domain

* The name registered under the TLD
  Example: in `tryhackme.com`, the SLD = `tryhackme`

* Limit: **63 characters**

* Allowed characters: `a–z`, `0–9`, hyphens
  (cannot start/end with hyphens, no consecutive hyphens)

### Subdomains

* Appear to the **left** of the SLD
  Example: `admin.tryhackme.com`

* Same rules as SLD

* Entire domain length cannot exceed **253 characters**

---

## Task 3 — DNS Record Types

Different DNS records provide different types of information.

### A Record

* Maps a hostname to an IPv4 address
  Example: `104.26.10.229`

### AAAA Record

* Maps a hostname to an IPv6 address

### CNAME Record

* Provides an alias to another domain name
  Example:
  `shop.website.thm` → `shops.myshopify.com`

### MX Record (Mail Exchange)

* Specifies mail servers for a domain
* Includes a **priority value** (lower = higher priority)

### TXT Record

* Stores arbitrary text
* Common uses:

  * Domain ownership verification
  * Email authentication (SPF, DKIM, DMARC)

---

## Task 4 — Making a DNS Request

DNS lookups involve multiple servers and caching layers. The typical recursive flow:

1. **Local Cache Check**
   The operating system checks if the requested domain is already cached.

2. **Recursive DNS Server**
   Usually provided by the ISP.

   * Has its own cache
   * If found, returns the result immediately

3. **Root DNS Server**
   If not cached, the recursive server asks the root server for the appropriate TLD server.

4. **TLD Server**
   Points to the domain’s **authoritative name server**.

5. **Authoritative DNS Server**

   * Holds the official DNS records
   * Returns A, AAAA, MX, CNAME, TXT, etc.
   * Includes a **TTL** (Time To Live) value for caching

The recursive server caches the response for the duration of the TTL before returning it to the client.

---

## Task 5 — Practical Lookup (nslookup)

The lab introduced basic DNS commands using `nslookup`.

### Query a CNAME

```
nslookup --type=CNAME shop.website.thm
```

### Query a TXT record

```
nslookup --type=TXT website.thm
```

### Query an MX record

```
nslookup --type=MX website.thm
```

### Query an A record

```
nslookup --type=A www.website.thm
```

### Key Observations

* CNAMEs reveal underlying service providers
  (e.g., Shopify hosting for shop domains)
* TXT records store verification and security metadata
* MX records always include a priority value
* A and AAAA records store IPv4 / IPv6 addresses

---

## Summary — Key Takeaways

* DNS maps human-readable names to IP addresses.
* Domain hierarchy: Root → TLD → SLD → Subdomain.
* Important record types:

  * A (IPv4), AAAA (IPv6)
  * CNAME (alias)
  * MX (mail servers + priority)
  * TXT (metadata and verification)
* Recursive DNS servers perform multi-step lookups:
  local cache → recursive → root → TLD → authoritative.
* TTL determines how long a result stays cached.
* `nslookup` allows investigation of any DNS record type.
