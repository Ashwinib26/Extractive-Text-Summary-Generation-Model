
# **Extractive Text Summary Generation Model**
A simple web-based extractive text summarization tool that takes user input text and extracts key sentences to generate a summary.

## **🚀 Features**
- Takes **text input** from users.
- Uses **Extractive Summarization** based on **word frequency scoring**.
- Displays the summarized output **instantly on the same webpage**.
- Built with **Flask (Backend) & HTML/CSS/JavaScript (Frontend)**.

---

## 📜 How the Extractive Summarization Model Works
The extractive summarization model follows these **NLP-based steps** to extract the most important sentences:

### **1️⃣ Preprocessing the Text**
- Tokenizes the input text into sentences.
- Removes **stopwords** (e.g., "the", "is", "and") and **punctuation**.

### **2️⃣ Assigning Importance Scores**
- Calculates **word frequency** for all non-stopwords.
- Normalizes frequencies (scaling between 0 and 1).
- Scores each sentence based on the **sum of its word frequencies**.

### **3️⃣ Selecting Key Sentences**
- **Sorts sentences** by their scores in descending order.
- Extracts **top-ranked sentences** (based on a predefined percentage).
- Returns the selected sentences as the **final summary**.
  
---

## **🛠️ Technologies Used**
- **Python** (Flask, spaCy, NLTK)
- **NLP Techniques** (Tokenization, Stopword Removal, Sentence Scoring)
- **Frontend** (HTML, CSS, JavaScript, jQuery)

---

## **🖥️ How It Works**
1. **User enters text** in the input box.
2. **Chooses "Extractive Summarization"** from the dropdown.
3. **Clicks Summarize** → The system extracts the most important sentences.
4. **Summary is displayed** on the same webpage.

---

## **🔹 Future Enhancements**
✅ Add **Abstractive Summarization (T5, BART, GPT)**  
✅ Integrate **Image Caption Generation** 

---

Let me know if you need any modifications or additions! 🚀
