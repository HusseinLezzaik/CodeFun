## Strategy
- Gather System Requirements
- Plan
- Estimate
- Communicate
- Diagram

## Estimation Cheatsheet
### Units
- 1 kB = 1000 bytes
- 1 MB = 1000 kB
- 1 GB = 1000 MB
- 1 TB = 1000 GB
- 1 PB = 1000 TB

### Bandwidth
- Mobile Phone (4G): 1-3 MB/s
- Public Internet (home WiFi): 50-100 MB/s
- Within a data center: 5 GB/s

### Latency HTTP request
- Intra-continental: 50-150 ms
- Cross-continental: 200-500ms

### Storage Capacity
- 10TB disk space
- 256GB-1TB of RAM (1TB for really large/optimized machines)

### Storage Scale
- A Character: 1 byte
- Typical metadata for a thing excluding images (name, description, other attributes): 1-10 KB
- A high-quality 1920x1080p image: ~2MB (realistically can be lossy-compressed by 10-20x)
- 20 minutes of HD video: ~1GB

## 1 Client Server
- Client: machine/process that requests data or service from a server
- Server: machine/process that provides data or service for a client, usually by listetning for incoming network calls
- Client-Server Model
- IP Address: 127.0.0.1 (your own machine/localhost), 192.168.x.y (private network)
- Port: in order for multiple programs to listen for new network connections on the same machine without colliding, they pick a port to listen on. A port is an integer b/w 0 and 2^16. Typically ports 0-1023 are reserved for system port and 
shouldn't be used by user-level processes.
22: Secure Shell
53: DNS Lookup
80: HTTP
443: HTTPS
- DNS: Domain Name System, it describes the entities and protocols involved in the translation from domain names to IP Addresses.

## 2 Network Protocols
- IP (Internet Protocol). This network outlines how almost all machine-to-machine communications should happen in the world. Other protocols like TCP< UDP, and HTTP are built on top of IP.
- TCP network protocol built on top of the IP. Allows for ordered, reliable data delivery between machines over the public internet by creating a connection.
- HTTP (HyperText Transfer Protocol) is a very common network protocol implemented on top of TCP. Clients make HTTP requests, and servers respond with a response.
- IP Packet: is effectively the smallest unit used to describe data being sent over IP, asied from bytes.

## 3 Storage
- Databases: are programs that either use disk or memory to do 2 core things: record data and query data.
- Disk: usually refers to either HDD (Hard-disk Drive) or SSD (Solid State Drive). SSD is far faster than HDD, but more expensive.

## 4 Latency and Throughput
- The time it takes for a certain operation to complete in a system. Most often this measure is time duration like milliseconds or seconds.
- Reading 1 MB from RAM: 250 us (0.25 ms)
- Reading 1 MB from SSD: 1,000 us (1ms)
- Transfer 1 MB over Network: 10,000 us (10ms)
- Reading 1 MB from HDD: 20,000 us (20ms)
- Inter-Continental Round Trip: 150,000 us (150ms)
- Throughput: the number of operations that a system can handle properly per time unit. For instance, the throughput of a server can often be measured in requests per second (RPS or QPS).

## 5 Availability
- Availability: the odds of a particular server or service being up and running at any point in time, usually measured in percentages. A server that has 99% availability will be operational 99% of the time (this would be described as 
having two nines of availability).
- High Availability: typically 5 nines or more, sometimes abbreviated "HA".
- Nines: typically refers to percentage of uptime. For example, 5 nines (golden standard) of availability means an uptime of 99.999% of the time.
- 99% (two 9s): 87.7 hrs
- 99.9% (three 9s): 8.8 hrs
- 99.99%: 53.6 minutes
- 99.999%: 5.3 minutes 
- Redundancy: the process of replicating parts of a system in an effort to make it more reliable
- SLA: Service-level agreement
- SL: Service-level objective

## 6 Caching
- Cache: a piece of hardware or software that stores data, typically meant to retrieve that data faster than otherwise.
- Caches are often used to store responses to network requests as well as results of computationally-long operations.
- Cache hit: when requested data is found in cache
- Cache miss: when requested data could have been found in a cache but isn't. This is typically used to refer to a negative consequence of a system failure or of poor design choice.

## 7 Proxies
- Forward Proxy: a server that sits between a client and servers and acts on behalf of the client, typically used to mask the client's identity (IP address). Forward proxies are often referred to as just proxies.
- Reverse Proxy: a server that sits between a clients and servers and acts on behalf of the servers, typically used for loggging, load balancing, or caching.
- [Nginx](https://www.nginx.com/) is a popular webserver thats often used as a reverse proxy and load balancer.

## 8 Load Balancers
- Load Balancer: type of reverse proxy, that distributes traffic across servers. Load balancers can be found in many parts of a system, from the DNS layer all the way to the database layer.
- Server selection strategy: how a load balancer chooses server when distributing traffic amongst multiple servers. Common used strategies include round-robin, random selection, performance-based selection (choosing the server with the 
best performance metrics, like the fastest response time or the least amount of traffic), and an IP-based routing.
- Hot Spot: when distributing a workload across a set of servers, that workload might be spread unevenly. This can happen if your sharding key or your hashing function are suboptimal, or if your workload is naturally skewed: some servers 
will receive a lot more traffic than others, thus creating a "hot-spot".
- [Nginx](https://www.nginx.com/) is a popular webserver thats often used as a reverse proxy and load balancer.

## 9 Hashing
- Consistent Hashing: a type of hashing that minimizes the number of keys that need to be remapped when hash tables gets resized. It's often used by load balancers to distribute traffic to servers; it minimizes the number of requests that 
get forwarded to different servers when new servers are added or when existing servers are brought down.
- Rendezvous HashingL a type of hashing also coined highest random weight hashing. Allows for minimal re-distribution of mappings when a server goes down.
- SHA: Secure Hash Algorithms, the SHA is a collection of cryptographic hash functions used in the industry. 

## 10 Relational Databases
- Relational Databaase: A type of structured database in which data is stored following a tabular format, often supports powerful querying using SQL.
- Non-relational database: NoSQL databases
- SQL: structured query language. Relational databases can be used using a derivative of SQL such as PostgreSQL.
- ACID (Atomicity, Consistency, Isolation, Durability), simple and intuitive operations.
- [Postgres](https://www.postgresql.org/):  a relational database that uses a dialect of SQL called PostgreSQL. Provides ACID transactions.

## 11 Key-Vaule Stores
- Is a flexible NoSQL database that's often used for caching and dynamic configuration. Popular options include DynamoDB, [Etcd](https://etcd.io/), [Redis](https://redis.io/), and [ZooKeeper](https://zookeeper.apache.org/).

## 12 Specialized Storage Paradigms
- Blob storage usually for unstructured data. Things like Amazon S3 or GCS from google.
- Time series Database
- Graph Database: stores data following the graph data model.
- Cypher: a graph query language
- [Google Cloud Storage](https://cloud.google.com/storage): GCS is a blob storage service provided by Google
- [S3](https://aws.amazon.com/s3/): is a blog storage service provided by Amazon thru AWS
- [InfluxDB](https://www.influxdata.com/): popular open-source time series database
- [Prometheus](https://prometheus.io/): popular open-source time series database, typically used for monitoring purposes
- [Neo4j](https://neo4j.com/): popular graph database that consists of nodes, relationships, properties, and labels

## 13 Replication and Sharding
- Replication: the act of duplicating the data from one database server to others. Increase Redundancy of your system, and tolerate regional failures for instance.
- Sharding: sometimes called data partitioning, sharding is the act of splitting a database into two or more pieces called shards & is typically done to increase the throughput of your database.

## 14 Leader Election
- Process by which nodes in a cluster elect a so called leader amongst them, responsible for the primary operations of the service that these nodes support.
- [Etcd](https://etcd.io/) is a strongly consistent, highly available key-value store. It's often used to perform leader election.
- [ZooKeeper](https://zookeeper.apache.org/) is a strongly consistent, highly available key-value store. It's often used to store important configs or to perform leader election.

## 15 Peer-To-Peer Networks 
- Collection of machines referred to as peers that divide a workload b/w themselves to premusably complete the workload faster than would otherwise be possible.

## 16 Polling and Streaming
- Polling: act of fetching a resource or piece of data regularly at an interval to make sure your data is not too stale
- Streaming: usually refers to the act of continuously getting a feed of info from a server by keeping an open connection b/w the two machines/processes.

## 17 Configuration
- JSON, YAML
- Static or Dynamic configs

## 18 Rate Limiting
- Act of limiting the number of requests sent to or from a system.
- [Redis](https://redis.io/): an in-memory key-value store.

## 19 Logging and Monitoring
- Logging
- Monitoring
- Alerting

## 20 Publish/Subscribe Pattern
- Apache Kafka: distributed messaging system created by LinkedIn. Very useful when using the streaming paradigm as opposed to polling.
- [Cloud Pub/Sub](https://cloud.google.com/pubsub/): highly-scalable messaging service created by Google.

## 21 MapReduce
- Popular framework for processing very large datasets in a distributed setting efficiently, quickly, and in a fault-tolerant manner.
- Distributed File System is an abstraction over a (usually large) cluster of machines that allows them to act like one large file system. 
- The two most popular implementations of a DFS are the Google File System (GFS) and the Hadoop Distributed File System (HDFS).
- Hadoop: framework that supports MapReduce jobs and other data-processing pipelines.

## 22 Security and HTTPS
- Man-in-the-Middle Attack
- Symmetric Encryption
- Asymmetric Encryption
- AES
- HTTPS
- SSL Certificate

## 23 API Design
- Pagination
- CRUD Operations (Create, Read, Update, Delete)
