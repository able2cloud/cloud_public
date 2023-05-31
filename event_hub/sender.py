from azure.eventhub import EventHubProducerClient, EventData

# Obtenha a string de conexão do namespace. Substitua com suas próprias informações.
connection_str = 'Endpoint=sb://testcasanamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=<YourPrimaryKey>;EntityPath=testcasaeventhub'

producer = EventHubProducerClient.from_connection_string(conn_str=connection_str)

# Envie uma única mensagem
event_data = EventData("Hello, Azure Event Hubs!")
with producer:
    producer.send(event_data)

