
```markdown
Kafka, ZooKeeper, InfluxDB Integration with Python Generator and Worker

This project sets up Kafka, ZooKeeper, and InfluxDB in a Docker container, and uses Python scripts for generating and consuming messages to InfluxDB via Kafka.

Prerequisites

- Docker and Docker Compose installed
- Python 3.x installed
- Necessary Python libraries (`kafka-python`, `influxdb-client`, etc.)

Setup Instructions

1. Start the Docker Containers
To start the Kafka, ZooKeeper, and InfluxDB containers in the background, use the following command in the terminal:

```bash
docker compose up -d
```

This will start all services as defined in the `docker-compose.yml` file.

2. Configure InfluxDB
- Open the InfluxDB UI in your browser.
- Create an admin user in the UI.
- Update your local environment with the credentials you created in the InfluxDB UI.
- Create a new token for API access.
- Update `worker.py` with the newly generated token and any other settings (organization, bucket) as configured in the InfluxDB UI.

3. Run the Data Generator

Open a new terminal and run the data generator script to start producing messages to Kafka:

```bash
python datagenerator.py
```

This script will begin generating Kafka messages.

 4. Run the Worker

Open another terminal and run the worker script to consume messages from Kafka and insert data into InfluxDB:

```bash
python worker.py
```
5. Verify Data in InfluxDB

- Open the InfluxDB UI and check if the data is being inserted into the InfluxDB.
- You can run **Flux queries** to verify the data being inserted.

Troubleshooting

- If you encounter issues with InfluxDB token or credentials, double-check the credentials in both the InfluxDB UI and `worker.py`.
- Ensure that all services are running by checking the status of the Docker containers:
  ```bash
  docker compose ps
  ```
