# Introduction

* Monitoring is integral to SRE.

Covered here:

* What needs to be measured
* How the etrics gathered can be used to improve business decisions
* Proactive monitoring
* Log processing and its importance
* Observability
* Distributed tracing
* Logs
* Metrics

## Four Golden Signals of Monitoring

* Traffic - gives a better understanding of service demand. QPS (Queries per second)
* Latency - Measure of time taken by the service to process an incoming request.
* Error - measure of failed client requests, 5xx errors.
* Saturation - measure of resource utilization by a service. This signal you state of the service resource how full they are.

These metrics help you understand system performance and bottlenecks, and to create better end-user experience. 

If you can only measure four metrics, focus on these four.

## Importance of Monitoring

* Reduction in time to resolve issues
* Business decisions
* Resource planning

## Basic Terminologies

* Metric - quantitive measurement of attribute
* Node or Host - physical server, virtual machine or container where application is running.
* QPS - Queries per Second, measure of traffic served by service per second.
* Latency - time interval between user action and response from the server.
* Error Rate - number of errors observed over a particular time period.
* Graph - representation of one or more values of metrics collected over time.
* Dashboard - collection of graphs showing health
* Incident - event that disrupts normal system operation
* MTTD - mean time to detect - interval between beginning of service failure and detection of such failure.
* MTTR - Mean time to Resolve - time spent to fix a service failure and bring back.

Monitoring Infrastructure - can be graphed.

* Host Metrics Agent - process running on the host that collects performance stats for host subsystems such as memory, CPU, network, etc.
* Metric Aggregator - process running on the host.
* Metrics Collector - collects all the metrics from metric aggregators running on multiple hosts. Collector takes care of decoding and stores data on the database.
* Storage - time-series database stores all of these metrics - OpenTSDB, Whisper, InfluxDB.
* Metrics Server - can be as basic as a web server taht graphically renders metric data.
* Alert Manager - regularly polls metric data available and, if ther are any anomalies detected, notifies you.

## Command Line Tools

* Most linux distributions come with command line tools to monitor system performance.

* ps/top
* -p ... information about processes
* -a ... displays info about user's processes
* -x includes processes that do not have controlling terminal

* ss ... sockst statistics command, with -t (TCP), -l (listening sockets), -n (service names)
* free - memory usage stats
* df - disk usage
* sar
* iftop
* tcpdump



To run an example, I quickly signed into a docker debian and installed htop. Top was not available for debian.

```
apt install htop
```

To get the commands used:

```
htop -h
(C) 2004-2019 Hisham Muhammad. (C) 2020 htop dev team.
Released under the GNU GPLv2.

-C --no-color                   Use a monochrome color scheme
-d --delay=DELAY                Set the delay between updates, in tenths of seconds
-F --filter=FILTER              Show only the commands matching the given filter
-h --help                       Print this help screen
-H --highlight-changes[=DELAY]  Highlight new and old processes
-M --no-mouse                   Disable the mouse
-p --pid=PID[,PID,PID...]       Show only the given PIDs
-s --sort-key=COLUMN            Sort by COLUMN in list view (try --sort-key=help for a list)
-t --tree                       Show the tree view (can be combined with -s)
-u --user[=USERNAME]            Show only processes for a given user (or $USER)
-U --no-unicode                 Do not use unicode but plain ASCII
-V --version                    Print version info

Long options may be passed with a single dash.

Press F1 inside htop for online help.
See 'man htop' for more information.
```

##### Debian Substitutes

* top -> htop
* ss -> netstat
* df - disk usage (works on debian)
* sar -> apt-get install sysstat  (then use sar command)
* iftop
* tcpdump (works on debian)

### Third Party Monitoring

* Datadog, monitoring as a service
* User experience - catchpoint, pingdom
* Catchpoint Global Monitoring Network
#### Generate Synthetic Traffic

* There are native linux tools which can be used to generate synthetic traffic.

### Proactive Monitoring with Alerts

* Data gives us a better idea of how systems are performing.
* Alerts are used to intervene and notify stakeholders, along with the MTTR metric.
* Most monitoring systems today provide an alert mechanism.

### Best Practices

* Pick the right metric types - Gauge, Timer, Counter.
* Avoid Over-Monitoring
* Prevent Alert Fatigue
* Have a Runbook for Alerts

### Observability

* Derived from Control Theory
* How well internal states of a system can be inferred from knowledge of external outputs
* Service infrastructures are becoming more complex, proactive monitoring alone is not sufficient to quickly resolve issues.
* With simple infrastructure, past failures can be prevented, but complex infrastructure and unknown factors can cause potential problems.
* Making the service observable, providing highly granular insights to implicit failure modes make it more hypothetically fixable.

Three Pillars of Observability:

* Metrics

(Covered above)

* Logs

Record of events and activities performed by a service during runtime, with corresponding timestamp. Basically, your basic logs that you would see using various, "log" commands or looking on a SaaS output.

ELK, the ELK stack involves, Elasticsearch, Logstash, Kibana...which provides centralized processing, Beats is a collection of lightweight data shippers taht can audit data from a network.

Storing logs is expensive, because extensive logging of every single event is a lot of data and takes up storage space, so the cost increases proportionally to the services.

* Traces

While metrics give an abstract view of the system, and logging gives a record of events that occured... tracing deals with complex distributed systems with multiple microservices where a user request goes from one service to another.

A trace is a series of spans, each span is a record of events performed by different microservice to serve the client's request. It's a log of client-request serving derived from various microservices.

Each microservice can be set up to run and collect as well as store traces, and accessing tracing. Basically, there is a, "trace storage," which sits seperately from the microservices, as well as a trace collector, which might be a microservice itself.

#### Popular Tracing Programs

OpenTelemetry: Observability framework for cloud-native software

Jaeger: Open-source distributed tracing solution

Zipkin: Open-source distributed tracing solution

