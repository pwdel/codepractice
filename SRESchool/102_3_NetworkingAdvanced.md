# Networking

### Networking Design

Networking design deals with how to set up a datacenter in such a way that different resources are segregated for different purposes.

### Definitions

#### Leaf switch (ToR)

This refers to the switch, where the servers connect to, in a DC. They are called by many names, like access switch, Top of the Rack switch, Leaf switch.

The term leaf switch comes from the Spine-leaf architecture, where the access switches are called leaf switches. Spine-leaf architecture is commonly used in large/hyper-scale data centres, which brings very high scalability options for the DC switching layer and is also more efficient in building and implementing these switches. Sometimes these are referred to as Clos architecture.

#### Spine switch

Spine switches are the aggregation point of several leaf switches, they provide the inter-leaf communication and also connect to the upper layer of DC infrastructure.

#### DC fabric

As the data centre grows, multiple Clos networks need to be interconnected, to support the scale, and fabric switches help to interconnect them.

#### Cabinet

This refers to the rack, where the servers and ToR are installed. One cabinet refers to the entire rack.

#### BGP

It is the Border Gateway Protocol, used to exchange routing information between routers and switches. This is one of the common protocols used in the Internet and as well Data Centers as well. Other protocols are also used in place of BGP, like OSPF.

#### VPN

A Virtual Private Network is a tunnel solution, where two private networks (like offices, datacentres, etc) can be interconnected over a public network (internet). These VPN tunnels encrypt the traffic before sending over the Internet, as a security measure.

#### NIC

Network Interface Card refers to the module in Servers, which consists of the Ethernet port and the interconnection to the system bus. It is used to connect to the switches (commonly ToR switches).

#### Flow

Flows refer to a traffic exchange between two nodes (could be servers, switches, routers, etc), which has common parameters like source/destination IP address, source/destination port number, IP Protocol number. This helps in traffic a particular traffic exchange session, between two nodes (like a file copy session, or an HTTP connection, etc).

#### ECMP

Equal Cost Multi-Path means, a switch/router can distribute the traffic to a destination, among multiple exit interfaces. The flow information is used to build a hash value and based on that, exit interfaces are selected. Once a flow is mapped to a particular exit interface, all the packets of that flow exit via the same interface only. This helps in preventing out of order delivery of packets.

#### RTT

This is a measure of the time it takes for a packet from the source to reach the destination and return to the source. This is most commonly used in measuring network performance and also troubleshooting.

#### TCP throughput

This is the measure of the data transfer rate achieved between two nodes. This is impacted by many parameters like RTT, packet size, window size, etc.

#### Unicast

This refers to the traffic flow between a single source to a single destination (i.e.) like ssh sessions, where there is one to one communication.

#### Anycast

This refers to one-to-one traffic flow as above, but endpoints could be multiple (i.e.) a single source can send traffic to any one of the destination hosts in that group. This is achieved by having the same IP address configured in multiple servers and every new traffic flow is mapped to one of the servers.

#### Multicast

This refers to one-to-many traffic flow (i.e.) a single source can send traffic to multiple destinations. To make it feasible, the network routers replicate the traffic to different hosts (which register as members of that particular multicast group).

### Security

Security is a rehash of security from the previous sections on security.

### Scale

Scale planning.

#### Failure Domains

* Hardware or software failures common.
##### Server Failures

* Power or NIC (Network Interface Card) or software bug.

##### ToR Failures

ToR will be covered later in the section. This can take down an entire cabinet, need to plan and prevent server failure.

### Resource Availability

* Analcast - two splines in parallel with connecting ToR's.
* Load Balancer - goes in parallel to a spline.

### RTT

> RTT is a measure of time, it takes for a packet to reach B from A, and return to A. It is measured in milliseconds. This measure plays a role in determining the performance of the services. Its impact is seen in calls made between different servers/services, to serve the user, as well as the TCP throughput that can be achieved.

Roughly inversely proportional to throughput (need to take into account packet loss).

### Infrastructure Services

Description of various hardware and software based infrastructure types.

ToR, Load Balancing, QoS (Quality of Service.)

> DNS based load balancer: Here the DNS servers keep a check of the health of the real servers and resolve the domain in such a way that the client can connect to different servers in that cluster. This part was explained in detail in the deployment at scale section.

> IPVS based load balancing: This is another means, where an IPVS server presents itself as the service endpoint to the clients. Upon incoming request, the IPVS directs the request to the real servers. The IPVS can be set up to do health for the real servers.

### Conclusion

This section was about literal datacenter management, not abstract SRE management in the cloud services methodology sense.


