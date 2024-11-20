# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the sentiment_analyzer function from the package created: TODO
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Recupera il testo da analizzare dagli argomenti della richiesta
    text_to_analyze = request.args.get('textToAnalyze')

    # Passa il testo alla funzione sentiment_analyzer e memorizza la risposta
    response = sentiment_analyzer(text_to_analyze)

    # Estrai l'etichetta e il punteggio dalla risposta
    label = response['label']
    score = response['score']

    # Controlla se la label è None, indicando un errore o un input non valido
    if label is None:
        return "Input non valido! Riprova."

    # Restituisci una stringa formattata con l'etichetta del sentimento e il punteggio
    return f"Il testo è stato identificato come {label.split('_')[1]} con punteggio di {score}."

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
