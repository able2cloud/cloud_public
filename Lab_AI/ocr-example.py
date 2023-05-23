import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

# Configurações
subscription_key = "<chave>"
endpoint = "<ponto-de-extremidade>"
image_path = os.path.join(os.getcwd(), "texto.png")

# Criação do cliente do Serviço Cognitivo
credentials = CognitiveServicesCredentials(subscription_key)
client = ComputerVisionClient(endpoint, credentials)

# Executa o OCR na imagem
with open(image_path, "rb") as image_file:
    ocr_results = client.recognize_printed_text_in_stream(image_file)

# Exibe o texto extraído
for region in ocr_results.regions:
    for line in region.lines:
        for word in line.words:
            print(word.text)

