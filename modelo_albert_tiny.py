# -*- coding: utf-8 -*-
"""modelo_albert-tiny.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FzTCfJoMIYaTsOGqeS9sBtxPD5CbML6I
"""

import pandas as pd
from transformers import AutoTokenizer, AutoModelForTokenClassification
import requests

tokenizer = AutoTokenizer.from_pretrained("dccuchile/albert-tiny-spanish-finetuned-ner")
model = AutoModelForTokenClassification.from_pretrained("dccuchile/albert-tiny-spanish-finetuned-ner")

import requests

API_URL = "https://api-inference.huggingface.co/models/dccuchile/albert-tiny-spanish-finetuned-ner"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

# Carga el archivo csv
df = pd.read_csv('/content/drive/MyDrive/ecuPrueba.csv')
# Itera sobre cada fila del dataframe
for index, row in df.iterrows():
    # Realiza la consulta
    output = query({"inputs": row['ATA_TEXTO']})

   # Imprime el ID de la llamada una vez
    print(f"ID LLAMADA: {row['TRA_ID']}")

 # Procesa la salida
    for entity in output:
        # Filtra por tipo 'LABEL_0'
        if entity['entity_group'] != 'LABEL_0':
            print(f"Entidad: {entity['word']}, Tipo: {entity['entity_group']}, Confianza: {entity['score']}")

"""de forma emprica, estadistica, ver en 2 docker, en una maquina 3 contenedor(1 modelo en cada uno), y ver si de otra forma."""



"""hacer uns estadistica empirico primero contando cada modelo cuantas entidades reconoce el  modelo y luego escojer 20 modelos al azar y ver por frases cual es el mejor y ver cuantas acierta(4/5)"""