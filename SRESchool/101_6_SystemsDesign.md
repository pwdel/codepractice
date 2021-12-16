# Systems Design Introduction

Even learning how to design systems is complex.

* The example we go through is a monolithic app designed to share photos, media and items can be liked by friends. (With a database service)

## Scalability

* What does scalability mean?
* Each component and service of a system must be tackled seperately.
* Scalability means increased performance as resources are added.
* Always-on services means facilitating redundancy which does not reduce performance.

### AKF Scale Cube

* Model for defining microservices, scaling products.
* Creates a common language for teams to discuss scale relateed options.

#### Horizontal Scaling

* Cloning an application or service such that work can be distributed across instances with absolutely no bias.
* Example given - database scaled seperately from the application. Each component's scaling capabilities can be different.

* Faster to implement, low cost from a developer effort perspective, can scale transaction volumes nicely. However, tends to be higher cost from the perspective of operational cost of data, added storage cost.

#### Load Balancing

* Improves distribution of workloads across multiple computing resources - processors, network links, disk drives, etc.
* Optimizes resource use, maximizes throughput, minimizes response time, avoids overload of any single resource.

##### LB Tasks

* Service Discovery
* Health Checking
* Load Balancing

##### LB Methods

* Least Connection Method - traffic goes to fewest active connections.
* Least Response Time Method - traffic to fewest active connections and lowest response time.
* Round Robin Method - directs traffic to the first available server and moves that server to the bottom of the queue.
* IP Hash - IP address of client determines which server recieves the request.

#### CDN's

* CDN's added closer to client's location.
* Static data, images, javascript, CSS, which don't change very often can be cached.
* Use CDN's to offload traffic from your site.
* Speed improvements
* Use DNS to serve content on sites' behalf, so there may need to be DNS changes.
* Offloads traffic spikes and is economical.

#### Microservices

* App sets for different applications - login, content upload, newsfeed, content interaction, managing friends, etc.
* DB Leader and Follower
8 Scale through services or resources, scaling and splitting data sets, transactions and engineering teams along verb (services) and noun (resources) boundries.
* Very large datasets where relations between data are not necessary, large complex systems where scaling engineering resources requires specialization.
* Split up actions using verbs, or resources using nouns, or use a mix. Split the services and data along lines defined by the noun-verb approach.
* Takeaways: allow efficient scaling of transactions.

#### Sharding

* Splitting Services based upon attributes that are looked up or determined at the time of the transaction, implemented as splits by a requestor, customer or client.
* Deterministic algorithm written for these types of splits.
* Sharing aids in scaling transaction growth, scaling intstruction sets, decreasing processing time. This is more effective at scaling growth in customers or clients. Aids with disaster recovery efforts.

Database is split and served to clients directed to a data center based upon thier geography. Helps improve performance. For example - video sharing / YouTube.

## Availability

Availabilty is expressed as a number of nines.

* 99% (two nines) - 3.65 days of downtime per year, etc.
* 99.5 (two and a half) - 1.83 days of downtime per year.
* 99.9 (three nines) - 8.77 hours per year

#### HA - Availability Serial Components

* System with components is operating in series if the failure of a part leads to the combination being inoperable.
#### HA - Availability Parallel Components

* Failure of a part leads to another system taking over the operation of said part.
#### HA - Core Principles

* Elimination of single points of failure
* Reliable crossover
* Detection of failures as they occur
#### HA - SPOF

* Never implement and always eliminate single points of failure
* Do during architecture reviews and new designs
* Identify single instances on architectural diagrams
* Maximize availability through multiple instances
#### HA - Relieable Crossover

* Ensure when system components failover they do so reliably.

#### Applications in SRE Role

* SRE works done deciding acceptable SLA and makes ssure is able to achieve it.
* Architecture design from building the data center to making sure the site is not effectved by a network switch, hardware, power or software failures.
* SRE runs mock drills of failures to see how the system behaves in uncharted territory and comes up with a plan to improve availability if there are misses.
## Fault Tolerance

* Murphy's kaw

* MTTR - Mean time to Repair
* MTBF - Between Failures, Average Operational Time
* MTTF - To Failures (Average Time Before Failure)
* MTTD - Before Detected
* MTTI - Before Investigated
* MTRS - Before Service Restored
* MTBSI - Between Service Incidents
* Failure Rate

#### Fault Tolerance - fault isolation terms.

Systems should have a short circuit. In our imaginary system, if "notifications," is not working, the site should gracefully handle failure by removing the functionality instead of taking the whole site down.

* "Swimlane," is a commonly used fault isolation methodology. Adds a barrier to the service from another service so that failure on either of them won't affect the other.

Basically, "Swimlanes," are the dividing line. Different aspects of the service may be seperated not only by different silos within the microservices paradigm, but also by, "swimlanes," of organization, where storage, applications and load balancers may all live across different swimlanes.

There are different approaches to swimlanes:

1. Swimlane the Money Making Application. Never allow the cash register to be comprimised by ohter systems.
2. Swimlane the biggest sources of incidents. Identify the recurring caues of pain and isolate them.
3. Swimlane natural barriers, customer boundaries make good swim lanes (Public vs. Enterprise customers for example).

## Conclusion

Some of this may be over-engineering, but reducing bottlenecks and eliminating single points of failure, or introducing replicas are standard stuff.