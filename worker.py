import time
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import json
from kafka import KafkaConsumer

client = InfluxDBClient(
    url="http://localhost:8086",
    token="X0s2EQiwogPLfhsOyfaxot-WOeosJhK6v5CUUZ_o0GSKml1UZQ_xjnl5ynvRzvwkIkG-R8IRCx5escLT2NPWmg==",
    org="D"
)

bucket = "B1"
write_api = client.write_api(write_options=SYNCHRONOUS)

consumer = KafkaConsumer('color-topic', bootstrap_servers='localhost:9092')

color_data = {}

for message in consumer:
    data = json.loads(message.value.decode('utf-8'))
    color = data['color']
    value = data['value']


    if color in color_data:

        color_data[color]["count"] += 1
        color_data[color]["sum"] += value
    else:
       
        color_data[color] = {"count": 1, "sum": value,}

    data_point = Point("color") \
        .tag("color", color) \
        .field("value", value) \
        .field("count", color_data[color]["count"]) \
        .field("sum", color_data[color]["sum"])
    print(data_point.to_line_protocol())
    write_api.write(bucket=bucket, org="D", record=data_point)

client.close()
