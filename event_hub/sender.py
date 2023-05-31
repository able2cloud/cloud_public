from azure.eventhub import EventHubProducerClient, EventData

# Use a string de conexão fornecida
connection_str = 'Endpoint=sb://testcasanamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=jbtvWnANxVyvQF4ZD3eWF1+k9ZXEJ4rlo+AEhJqgLP0='

producer = EventHubProducerClient.from_connection_string(conn_str=connection_str)

# Envie uma única mensagem
event_data = EventData("Hello, Azure Event Hubs!")
with producer:
    producer.send(event_data)

