from azure.eventhub import EventHubConsumerClient

# Substitua com suas próprias informações
# Use a string de conexão fornecida
connection_str = 'Endpoint=sb://testcasanamespace.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=jbtvWnANxVyvQF4ZD3eWF1+k9ZXEJ4rlo+AEhJqgLP0='
consumer_group = '$Default'

client = EventHubConsumerClient.from_connection_string(connection_str, consumer_group)

def on_event(partition_context, event):
    # Imprima a mensagem recebida
    print("Received event from partition: {}.".format(partition_context.partition_id))
    print("Message: ", event.body_as_str())

    # Marque a mensagem como consumida
    partition_context.update_checkpoint(event)

with client:
    client.receive(on_event=on_event)

