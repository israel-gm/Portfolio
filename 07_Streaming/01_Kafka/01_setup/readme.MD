# Setup and running

## 📌 Producer (producer.py)

The Producer is like a data collector.

- It connects to the Metropolitan Transportation Authority (MTA) feed, which publishes real-time subway and bus updates in New York City.
- Every 30 seconds, it fetches the latest information about trains, vehicles, or service alerts.
- This information is then packaged and sent into Kafka, our data pipeline system.

👉 Think of it as someone standing at a station, writing down the latest train arrivals, and dropping that information into a mailbox (Kafka) so others can pick it up.


## 📌 Consumer (consumer.py)

The Consumer is like a data reader and analyzer.

- It listens to the messages coming out of the Kafka “mailbox.”
- Each message is turned into structured information that we can work with.
- As the data accumulates, it uses basic analytics (via Pandas, a data tool) to summarize the information.

👉 For example, every 50 messages it receives, it produces a small “snapshot report” that shows general patterns in the data (like message sizes, frequency, or distribution).


## 🚂 How They Work Together

- The Producer brings in live transit updates from the MTA.
- The Consumer listens to those updates and provides summaries.

Together, they create a real-time data flow: one side collects, the other side analyzes. This setup is the foundation for building more advanced applications such as dashboards, alerts, or even machine learning models that predict delays or travel times.
