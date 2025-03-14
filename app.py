from flask import Flask, render_template, request
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

app = Flask(__name__)

nlp = spacy.load("en_core_web_sm")

def extractive_summary(text, percentage=0.3):
    doc = nlp(text)
    word_frequencies = {}

    for word in doc:
        if word.text.lower() not in STOP_WORDS and word.text not in punctuation:
            word_frequencies[word.text] = word_frequencies.get(word.text, 0) + 1

    max_freq = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] /= max_freq

    sentence_scores = {}
    for sent in doc.sents:
        for word in sent:
            if word.text in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word.text]

    
    sorted_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    select_length = int(len(sorted_sentences) * percentage)

    return " ".join([str(sent) for sent in sorted_sentences[:select_length]])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/summarize", methods=["POST"])
def summarize():
    if request.method == "POST":
        text = request.form["input_text"]
        summary = extractive_summary(text)  
        return render_template("index.html", summary=summary, input_text=text)

if __name__ == "__main__":
    app.run(debug=True)
