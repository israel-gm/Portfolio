# Streaming with Apache Kafka

Streaming ML project with Kafka and Python consumers/producers to get feed from the Metropolitan Transportation Authority (MTA)

GTFS Feeds

The General Transit Feed Specification (GTFS) is a standard data format for public transportation schedules and related geographical information. It's an open standard used worldwide by transit agencies.

Static Data: The core GTFS feed is often called "GTFS Static" and is a collection of comma-separated value (CSV) files zipped together. This data includes:

- Scheduled information: bus and subway schedules, including holiday services.
- Geographic information: locations of stations and bus stops.
- Route information: details on train lines and bus routes.

Real-time Data: The GTFS-Realtime extension provides up-to-the-minute updates. It's often used in conjunction with the static feed to provide real-time information to the public and developers. This data includes:

- Trip updates: delays, cancellations, and changes to routes.
- Service alerts: notifications about unforeseen events affecting stations, routes, or the entire network.
- Vehicle positions: the current location of buses and trains.
