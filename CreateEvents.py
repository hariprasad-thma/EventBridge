import boto3

client = boto3.client("events")

details = '{"name":"happy"}'
response = client.put_events(
    Entries = [
        {
            "Source":"happy-event",
            "DetailType":"happy-details",
            "Detail":details,
            "EventBusName":"happy-event-bus"
        }]
)

print(response)