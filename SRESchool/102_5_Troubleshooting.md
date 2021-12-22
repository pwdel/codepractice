# Troubleshooting

* Troubleshooting flow chart.

## Important Tools

* For logs parsing -: grep, sed, awk, cut, tail, head
* For network checks -: nc, netstat, traceroute/6, mtr, ping/6, route, tcpdump, ss, ip
* For DNS -: dig, host, nslookup
* For tracing system call -: strace
* For parallel executions over ssh -: gnu parallel, xargs + ssh.
* For http/s checks -: curl, wget
* For list of open files -: lsof
* For modifying attributes of the system kernel -: sysctl

### Clustering / Parallel Tools

In case of distributed systems, some good third party tools can help to execute commands/instructions on many hosts at once, like:

#### SSH based tools
ClusterSSH: Cluster ssh can help you run a command in parallel on many hosts at once.
Ansible: It allows you to write ansible playbooks which you can run on hundreds/thousands of hosts at the same time.
Agent Based tools
Saltstack: Is a configuration, state and remote execution framework, provides a wide variety of flexibility to users to execute modules on large numbers of hosts at once.
Puppet: Is an automated administrative engine for your Linux, Unix, and Windows systems, performs administrative tasks.

### Log analysis tools
These can help in writing SQL type queries for parsing, analysing logs and provide an easy UI interface to create dashboards which can render various types of charts based on defined queries.

ELK: Elasticsearch, Logstash and Kibana, provide package of tools and services to allow, parse logs, index logs and analyse logs easily and quickly. Once logs/data is parsed/filtered through logstash and indexed in elasticsearch, one can create dynamic dashboards in Kibana in a matter of minutes. Such provides easy analysis and correlation on application errors/exceptions/warnings.
Azure kusto: Azure kusto is a cloud based service similar to Elasticsearch and Kibana, it allows easy indexing of heavy logs, provides SQL type interface for writing queries, and an interface to create dynamic dashboards.

### Performance analysis commands
Most of these commands are a must to know for doing performance analysis of a system or service.

top -: shows real-time view of running system, processes, threads etc.
htop -: Similar to top command, but a bit more interactive then it.
iotop -: An interactive disk I/O monitoring tool.
vmstat -: Virtual memory statistics explorer.
iostat -: Monitoring tool for input/output statistics for devices and partitions.
free -: Tell info about physical memory and swap memory.
sar -: System activity report, reports diff metrics such as cpu, disk, mem, network, etc.
mpstat -: Display info about CPU utilization and performance.
lsof -: Provides info about the list of open files, opened by which processes.
perf -: Performance analysing tool.


### Profiling tools

Profiling is an important part of performance analysis of the service. There are various profiler tools available, which can help figure most frequent code-paths, debugging, memory profiling, etc. These can generate the heatmap to understand the code performance when under load.

FlameGraph: Flame graphs are a visualization of profiled software, allowing the most frequent code-paths to be identified quickly and accurately.
Valgrind: It is a programming tool for memory debugging, memory leak detection, and profiling.
Gprof: GNU profiler tool uses a hybrid of instrumentation and sampling. Instrumentation is used to collect function call information, and sampling is used to gather runtime profiling information.
To know how LinkedIn performs On-Demand Profiling on its services, Read LinkedIn blog ODP: An Infrastructure for On-Demand Service Profiling

### Benchmarking

It is a process of measuring the best performance of the service. Like how much QPS service can handle, its latency when load is increasing, host resource utilization, loadavg etc etc. The regression testing (i.e load testing) is a must before deploying the service to production.

Some of known tools -:

Apache Benchmark Tool, ab:, It simulate a high load on webapp and gather data for analysis
Httperf: It sends requests to the web server at a specified rate and gathers stats. Increase till one finds the saturation point.
Apache JMeter: It is a popular open-source tool to measure web application performance. JMeter is a java based application and not only a web server, but you can use it against PHP, Java, REST, etc.
Wrk: It is another modern performance measurement tool to put a load on your web server and give you latency, request per second, transfer per second, etc. details.
Locust: Easy to use, scriptable and scalable performance testing tool.
Limitation -:

Above tools help in synthetic load or stress testing, but such does not measure actual end user experience, It can’t see how end user resources will affect application performance, it is due to lack of memory, CPU, or poor connectivity to the internet.

To know how LinkedIn performs load testing across its fleet. Read : Eliminating toil with fully automated load testing

And to know how LinkedIn makes use of Real Time Monitoring (RUM) data to overcome the limitations of load testing, and help improve overall experience for end users. Read : Monitor and Improve Web Performance Using RUM Data Visualization

### Scaling

System designed optimally can perform up to a certain limit only, based on availability of resources. Continuous optimization is always needed to ensure optimum use of resources at its peak. With increasing QPS, Systems need to scale up. We can either scale vertically or horizontally. Vertical scalability has its limits as one can increase cpu, memory, disk, GPU and other specifications to certain limit only, whereas horizontal scalability can grow easily and infinitely given limitations imposed by application design and environment attributes.

Scaling a web application will require some or all of the following -:

Ease the server load by adding more hosts.
Distributing the traffic across servers by using Load Balancers.
Scale up DB by sharding the data and increasing read replicas.

## Example

* Goes through memory leak example.