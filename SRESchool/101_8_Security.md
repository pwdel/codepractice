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
* 

## Threats, Attacks, Defense

## Writing Secure Code
