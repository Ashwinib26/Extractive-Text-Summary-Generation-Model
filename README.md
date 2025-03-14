# 📝 Extractive Text Summarization Web App  
A simple **web-based extractive text summarization tool** that allows users to input text and instantly generate a summarized version by extracting key sentences. Built using **Flask (backend) and HTML/CSS (frontend).**  

---

## 🚀 Features  
✔️ **Takes text input from users** via a web page.  
✔️ **Uses Extractive Summarization** based on **word frequency scoring**.  
✔️ **Displays the summarized output instantly** on the same webpage.  
✔️ **Built with Flask (Backend) & HTML/CSS (Frontend)** for a simple and clean UI.  

---

## 📜 How the Extractive Summarization Model Works  
The extractive summarization model follows these **NLP-based steps** to extract the most important sentences:

### **1️⃣ Preprocessing the Text**  
- Tokenizes the input text into sentences.  
- Removes **stopwords** (e.g., "the", "is", "and") and punctuation.  

### **2️⃣ Assigning Importance Scores**  
- Calculates **word frequency** for all non-stopwords.  
- Normalizes frequencies (scaling between 0 and 1).  
- Scores each sentence based on the **sum of its word frequencies**.  

### **3️⃣ Selecting Key Sentences**  
- **Sorts sentences** by their scores in descending order.  
- Extracts **top-ranked sentences** (based on a predefined percentage).  
- Returns the selected sentences as the **final summary**.  

---

## 🛠️ Technologies Used  
- **Python** (Flask, spaCy, NLTK)  
- **Natural Language Processing (NLP)** (Tokenization, Stopword Removal, Sentence Scoring)  
- **Frontend** (HTML, CSS for styling)  
- **Web Framework** (Flask for backend)  

---

## 📁 Project Structure  
```
Extractive-Summary/
│── static/
│   ├── styles.css         # Styles for the web page
│── templates/
│   ├── index.html         # Webpage UI
│── summarizer.ipynb       # Jupyter Notebook (original summarization logic)
│── app.py                 # Flask backend
│── requirements.txt       # Dependencies
│── README.md              # Documentation
```

---

## 🖥️ How It Works  
1️⃣ **User enters text** in the input box.  
2️⃣ **Clicks "Summarize"** → The system extracts the most important sentences.  
3️⃣ **Summary is displayed** on the same webpage instantly.  

---

## 🔹 Future Enhancements  
✅ Add **Abstractive Summarization** (T5, BART, GPT).  
✅ Integrate **Image Caption Generation** for multi-modal summarization.  
✅ Improve UI with a **better frontend framework (React, Bootstrap)**.  

---

## 💬 Feedback & Contributions  
We welcome suggestions, discussions, and contributions! Feel free to **open an issue** in the repository. 🚀  

