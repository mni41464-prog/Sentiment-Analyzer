# 🧠 Sentiment Analyzer

> A simple NLP tool for article and text sentiment analysis.

一个简单的 NLP 文本情感分析工具，支持网页文章和本地 TXT 文件。

---

## ✨ Features

- 🌐 Extract text from article URLs
- 📝 Generate article summaries
- 📄 Read local TXT files
- ❤️ Analyze sentiment polarity

## 🛠 Tech Stack

`Python` `NLTK` `TextBlob` `Newspaper3k`

## 🚀 Quick Start

Install dependencies:

```bash
pip install -r requirements.txt
```

Download NLTK data:

```bash
python -m nltk.downloader punkt_tab
```

Run the program:

```bash
python main.py
```

Choose:

```text
url
```

or:

```text
txt
```

## 📊 Sentiment Score

| Score | Sentiment |
|---|---|
| `< 0` | Negative 😞 |
| `0` | Neutral 😐 |
| `> 0` | Positive 😊 |

## 📁 Project Structure

```text
Sentiment-Analyzer/
├── main.py
├── test.txt
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📌 Notes

TextBlob works best with English text.  
Complex expressions, metaphors, and sarcasm may not always be interpreted accurately.