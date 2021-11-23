# Security

## What We Cover

* Fundamentals
* Network Security
* Threats, Attacks, Defense
* Writing Secure Code
## Fundamentals

* SRE and Security Engineering are responsible with keeping a system usable.
* Broken releases, capacity shortages, misconfigurations can make systems unusable.
* Privacy incidents which break the trust of users in a system make a system, "unusable."
* System security should be top of mind for SRE.

* Notes on Generals of Security:

* Full System Lifecycle - thnk abouve security within the context of the full system lifecycle.
* Confidentiality - only allow data access to those who are permitted.
* Integrity - ensure data is not tampered or altered by unathorized users.
* Availability - ensure systems are only available to authorized users.

When Starting a new application or re-factoring an existing application, consier each functional feature:

* Is the process surrounding this feature as safe as possible?
* If I were evil, how would I abuse this feature?
* Is the feature required to be on by default?
* [Security Principles by OWASP](https://owasp.org/www-project-web-security-testing-guide/stable/)

* Minimize Attack Surface Area
- Any form, button, anything that a user can access is a risk. The more that the user has closer access to a database, the worse.
* Establish Secure Defaults
- Experience should be secure by default and it should be up to the user to reduce their security, if they are allowed.
* Principle of Least Privledge
- Accounts should have the least privledge required to perform their business process.
* Principle of Defense in Depth
- Controls, when used in depth can make severe vulnerabilities difficult to exploit and unlikely to occur.
- A flawed admin interface is unlikely to be vulnerable if it correctly gates access to production management networks, checks of user authorization, logs all access.

* Don't Trust Services
- Third party partners may have different security policies and posture than you. You can't control third parties.
* Implicit trust of third party systems is not warranted.

* Seperation of Duties
- Key to fraud control.
- Someone who requests a computer cannot also sign for it, not should they directly recieve the computer.
- Different roles have different levels of trust than normal users.

* Security by Obscurity is a weak control
- Avoid it
- Security of application should not rely upon knowledge of the source code being kept secret.
- Linux is open source yet highly secure

* Keep it simple

* Fix issues correctly, once an issue has been identified, develop a test for it and understand the root cause. When design patterns are used, the security issue is likely widespread.

### Authorization vs. Authentication

* Authentication is the act of validating who the user is.
* Authorization is giving a user permission to access a specific resource.

### OpenID / OAuth

* OpenID is an auth protocol that allows us to authenticate users without using a local auth system. Users must be registered with an OpenID provider and said provider should be registered in the flow youf your application.
* Oauth is an authorization mechanism that allows your application user to access a provider (Gmail/FB/Instagram/etc.) - once there is a successful response, the application gets a token allowing the application to access API's on behalf of the user. OAuth2.0 can be used for pseudo authentication.

### Cryptography

* The science of hiding any text in such a way that the intended person sees it.

* Ciphers - the mathematical way of decoding cryptography

#### Stream Ciphers

* Message is broken into characters or bits and enciphered with a key or keystream.
* Should be random, scheme unbreakable unless keystream aquired.

#### Block Ciphers

* Processes messages in blocks, each of which is then encrypted or decrypted.
* 64 or 128 bits long. Blocks of plaintext are treated as a whole and used to produce ciphertext blocks.

#### Encryption

* DES - 1975, 56 bits, still works, but susceptible to brute force attacks.
* Triple DES - uses 3 of the above
* AES - replaced DES and 3DES, 3DES too slow, DES too weak.

AES, being from the year 2000 is younger than DES, the older algorithm is more trusted.

* RSA - flexible, up to 2048 bits, years of analysis, based upon the difficulty of factoring very large numbers. If an easy method of factoring large numbers is found, RSA destroyed.
* MD5 -one-way function, compute the hash from input data.
* SHA-1, similar to MD5, slower than MD5, takes over for weaknesses of Md5

* Digital Certificates - used for authentication.
* PKI - higherarchical framework, CA (Certificate Authority) public or private, known, such as VeriSign, Entrust, or a private one within organization.

* Syemtric key system - Alice put a secret message in a box and padlocks the box using a lock to which she has the key. Then sends the box to Bob through mail. When Bob gets the box, he uses an identical key to open the box and read the message.
* Asymetric key systems - instead of opening the box when he recieves it, he adds his own lock to the box and returns the box to Alice, who users her key to remove her lock and returns the box to Bob, who uses his key to open the box.

The critical advantage of Asymetric is that Alice (A) never needs to send their key out in the open to the reciever (B). Basically no key ever needs to be sent because of the back and fourth passing of the box.

* Diffie-Hellman - two system parameters, g and p. Both are public and may be used by everybody. Math used, asymetric algorithm.
#### Login Security

* SSH - know what it is already. Automatic encryption. Uses public key (Asymetric) encryption. It's not a shell, but rather a channel with end-to-end encryption. Can be configured with different cipher systems, including AES, Blowfish, 3DES, CAST128, and Arcfour.

* Kerberos - network authentication protocol and the default authentication technology used by Microsoft Active Directory to authenticate to services within a LAN. Symetric-key cryptography and requires thid-party authentication to verify user identities.

* Certificate Chain - the first part of the OpenSSL command shows 3 certificates numberd 0, 1 and 2. This is the, "chain of trust." On a high level, each part of the chain of trust references the previous in one direction, while a verify signature is sent in the other direction. Three different certificates - End, Intermediate and Root.

* TLS Handshake - client sends a HELLO, server says HELLO back, cipher suite supports key exchange, session key used to encrypt data sent through the connection. Basically both sides encrypt the data throughout the connection.

* Perfect Forward Secrecy - should be called, "Forward Secrecy."  Non-emphemeral key exchange, client sends the pre-master key to the server by encrypting it with the server's public key.

## Network Security

### Intro

* TCP/IP is the dominant networking technology today, has five layers, Application, Transport (TCP), Network (IP), Data Link, Physical. OSI Network model used to represent non-TCP-IP technologies.

* Application Layer - the interface between applications and network programs. Supports logins, file transfer, email, web browsing.
* Presentation Layer - helps form data. Allows application layer programs residing on different side of a communication channel to understand the data, it's a translator.
* Session layer is responsible for the connection.
* Transport layer is responsible for providing reliable transport, packet sequencing, traffic control, latency, etc.
* Network Layer is for routing data packets from one hop to the next hop.
* Data-link is for data packets to device dependent data frames.
* Physical layer - transmits device dependent frames through physical media.

### Public Key Infrastructure

* Public Key cryptography can be used to distribute keys.
* Issue keys upon user requests, storethem, prevent from denying signatures, etc.

### IPSec 

* Major security protocol at the network layer.
* Provides platform for constructing VPN's
* Deploying on the network layer encrypts IP packets (either the payloads or the entire packets)
* Also specifies how to exchange keys.

### PGP +& S/MIME - Email

* There are different security protocols at the application layer. (Email/Web/etc.)
* SMTP (used for sending and delivering from client to server on port 25). POP allows user to pick up the message and download it to their inbox, it's the incoming server, uses port 110, used since 1996.

#### PGP

* implements all major cryptographic algorithms, ZIP compression, base64 encoding.
* Used to authenticate a message, encrypt a message, or both.
* Authentication, ZIP, Encryption, Base64 Encoding.

#### GPG or GnuPG

* GnuPG is another free encryption standard, based upon OpenPGP.
* Nuances from PGP - compatability between certain algorithms, due to patent issues.

#### S/MIME

* SMTP - can only handle 7-bit ASCII text messages (UTF-8 plugins alliviates limitations). POP can handle 
* Multipurpose Internet Mail Extension Protocol - MIME ... designed to support sending an receiving email messages in different formats.
* IMAP - Internet Mail Access Protocol, operated on TCP Port 143, stores incoming email messages in the mail server until the user deletes them deliberately.

#### SSL/TLS

* SSL uses PKI to decide if a server's public key is trustworthy by requiring servers to use a security certificate signed by a trusted CA.
* With Netscape Navigator 1.0, there was one source - RSA Data Security Corporation, single source security credentials.
* Netscape had intended to train users to differentiate secure communications from insecure ones, with lock/unlock icon.
* After SSL2.0, Netfixed fixed some issues and restarted with SSL3.0. Deprecated in 2015, but modified SSL 3.0 is used today, along with the Transport Security Layer (TLS)

### Network Perimeter Security

#### General Firewall Framework

* Firewalls are needed because encryption algorithms cannot stop malicious packets from getting into an edge network.
* IP packets, can always be forwarded into an edge network.
* First developed in 1990s, may be a hardware device, software package or both.
* Packets flowing from outside of a network should be evaluated before allowed to enter. Firewall should have an ability to example packets without a negitive impact on speed.
* Carried out by firewalls, done in different ways, either a filter, gateway circuitry, application gateway or dynamic packet filter.

#### Packet Filters

* Inspects ingress packets.
* Only inspects IP headers and TCP headers, not the payloads.
* Stateless - treats each packet as an indepdenent object.
* Stateful - filtering, referred to as connection-state filtering,, keeps track of connections between internal host and external host.

#### Circuit Gateways

* Operated at transport layer
* Evaluate info of the IP address and port numbers to determine whether to allow or disallow.

#### Application Gateways (ALG)

* Proxy Servers
* ALG is a proxy for internal hosts, processing service requests from external clients.
* Performs deep inspections on each packet (ingress or egress).
* Inspects if in right format, MIME, or SQL, examines whether payload permitted.

#### Trusted Systems and Bastion Hosts

* A TOS is an operating system that meets a particular set of security requirements. Whether it can be trusted depends upon several elements.
* System design contains no defects
* No software loopholes
* Configured properly
* Management is appropriate
* Bastion hosts - strong defense mechanisms, serve as host computers for implementing application gateways, operated on a trusted operating system that must not containe unnecessary functionalities or programs.
* Bastion hosts used as controlled ingress points.
## Common Techniques and Scannings, Packet Capturing

#### Scanning Ports with Nmap

* NMap is a free an open source utility.
* Used to determine alive hosts in a network.

Usage example [here](https://github.com/pwdelbloomboard/devopstools/blob/main/commandline-examples/nmap.md).

Basically used to determine if an IP is being used by a legitimate service or an attacker.

Scan your server to simulate the processes a hacker would use to attack your site.

#### OpenVAS

* Full-featured vulnerability scanner.
* Framework of services and tools that provides a comprehensive and powerful vulnerability scanning and management package.

#### WireShark

* Protocol analyzer.
* Designed to decode not only packet bits and bytes but also relations between packets and protocols.
* Understands protocol sequences.

1. Capture only udp packets
2. Capture filter = "udp"

#### DumpCap

* DumpCap is a network traffic dumping tool.
* Captures packet data from a live network and writes packets to a file. pcapng
* Can be used to capture LAN traffic over an extended period of time.
* Wireshark can also be used, but DumpCap is lower memory.
#### DaemonLogger

* Logging system specifically for Network and Systems Management (NMS) environments.
#### NetSniff-NG

* High performance packet capture utility
* Specify input and output, the network interface, and output will be a file or folder on a disk.

* Example:

```
netsniff-ng –i eth1 –o data.pcap
```
#### Netflow

* Introduced on Cisco Routers, collects IP Traffic as it enters or exits a device.
* Analyzing data provided by NetFlow, a network admin can determine such things as the source and destination of the traffic, class of service, causes of congestions.
* Basically collects statistics on supportd routers

#### IDS

* Detects security related events but does not block them.
* Host/Network IDS - run on a server with a minimum overhead to monitor operating system. Embedded in a networking device, standalone appliance.
* Signature based IDS - sends alarm if known attack pattern detected.
* Has been the bread and butter for over a decade.
* Policy based IDS - when a configured policy is triggered, sends alert
* Anomoly, -  looks for traffic that deviates from the normal.
* Host based IDS, distributed agent residing on server
* Honeypot - attract intruder attention away from machine.

## Chinks in the Armour

### IP Spoofing

* Attacker replaces the IP address of the sender, or the destination, with a different address.
* Used to exploit a target host, or used to start a DoS attack.
#### Detection

* TTL Probes
* Send a packet to a suspected IP spoof host, which triggers a reply, and compares the TTL with the suspect packet, if the TTL is not the same as the packet being checked, it is a spoofed packet.
* Technique is successful when the attacker is different subnet from the victim.
### Covert Channel

* Pipe or communication channel between two entities that can be exploited by a process or application transferring info in a way that violates the system's security specifications.
* In TCP/IP, covert channels are established, and data can be secretly passed between two end systems.
* ICMP resides at the internet layer, they get configured to contain data in the, "payload," which is 56 bytes (header is 8 bytes). The ICMP packets are altered to carry secret (confidential) data in the payload.
* C&C Tools, such as Loki, can be used t establish encrypted interactive sessions.
* Deep packet inspection is a way, can help detect ICMP tunnelling - IDS/IPS tools can be used for this.

### IP Fragmentation Attack

* On the TCP/IP protocol suite, specifically IP - allows fragmentation of packets.
* IP fragmentation offset is used to keep track of different parts of the datagram.
* Information in the offset used to re-assemble the packets.
* Some routers and firewalls do not perform packet reassembly. IP fragments do not overlap, but attackers can create artificially fragmented packets to mislead the routers or firewalls. These packets are small and almost impractical for end systems because the data and computational overhead.
* "Ping of Death" attack - sends fragements that when reassembled at the end station, create a larger packet than the maximum permissible length.

#### TCP Flags

* Data exchange on TCP does not take place until the three-way handshake takes place.
* 6 flag bits - * Urgent Pointer (URG), * Acknowledgement (ACK), Push (PSH), Reset (RST), Synchronize (SYN), Finished (FIN).
* Abuse of the normal operation of settings of these flags can be used by attackers to launch DoS attacks. 
* Create illegal combinations of code

##### SYN Flood

* 3-way handshake used and exploited by attackers to disable services.
* Step 2 of three-way handshake, no limit is set on the time to wait after receiving a SYN.
* Timers on 3-way handshake are exploited.

##### FIN Attack

* TCP Fin flag indicates no more data will be transmitted.
* Four-way handshake mechanism.
* Spoofed FIN packet is constructed. Has correct sequence number, so packets are seen as valid by the targeted host.
* Authorized user sends HTTP requests over a TCP session.
* Web server accepts packets.
* Employee continues to send packets with incorrect SEQ/ACK numbers, so data from employee is disguarded by server. Attacker pretending to be Employee X is using corrected numbers. This results in the cracker highjacking the connection, whereby Employee X is confused.

#### Buffer Overflow

* Buffer is temporary data storage are used to store program code and data. When a program or process tries to store more data is retrieved than can be stored in a buffer location.

##### Mechanism

* Buffer overflow vulnerabilities exist in different types. The overall goal for all buffer overflow attacks is to take over the control of the privlideged program, and if possible, the host.
* Inject code in the right address space or by using the existing code and modifying certain parameters slightly.

* Countermeasure: most important approach is to have a concerted focus on writing correct code.
* Another measure is to make the memory locations on the address space of the code non-executable. This type of address space makes it impossible to execute code, which might be infiltrated in the program's buffers during an attack.

#### More Spoofing

* Address Resolution Protocol Spoofing

- Resolve, or map a known IP address to a MAC sublayer address.
- The cracker can exploit this hardware address by spoofing the hardware address of Host B.

* DNS Spoofing

- Method whereby hacker convinces target machine that the system it wants to connect to is the machine of the cracker.
- cracker modifies some records so that the name entries of hosts corresponds to attacker's IP address.
- Reverse lookup detects these attacks.
## Threats, Attacks and Defenses

### DNS Protection

#### Cache Poisoning Attack

* DNS responses are cached, including DNS negative queries, mispelt words, and all cached data periodically times out. Cahce poisoning is known as, "pharming."
* Website is redirected to a bogus website through DNS server.
* Eventually cache is cleaned, but may be a couple of hours.

#### DNSSEC (Security Extension)

* Long-term solution to DNS problems is authentication. If a resolver can't distinguish between valid and invalid data, then add source authentication to verify that the data received in response is equal to the data entered by the zone admin.
* DNS Security Extensions protects against data spoofing.

#### BGP

* Border gateway protocol.
* Autonomous system is a collection of routers or networks with the same network policy usually under single admin control.


## Writing Secure Code