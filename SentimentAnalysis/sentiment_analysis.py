import requests
import json

def sentiment_analyzer(text_to_analyse):
    # URL del servizio di analisi del sentiment
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Costruzione del payload della richiesta nel formato atteso
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Intestazione personalizzata che specifica l'ID del modello per il servizio di analisi del sentiment
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Inviando una richiesta POST all'API di analisi del sentiment
    response = requests.post(url, json=myobj, headers=header)

    # Parsing della risposta JSON dall'API
    formatted_response = json.loads(response.text)

    # Se il codice di stato della risposta è 200, estrai label e score dalla risposta
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # Se il codice di stato della risposta è 500, imposta label e score su None
    elif response.status_code == 500:
        label = None
        score = None

    # Restituzione di un dizionario contenente i risultati dell'analisi del sentiment
    return {'label': label, 'score': score}