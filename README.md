<div align="center">

# 🧠 Sentiment Analyzer

### Article & Text Sentiment Analysis Tool  
### 网页文章与文本情感分析工具

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green)
![TextBlob](https://img.shields.io/badge/TextBlob-Sentiment-orange)
![Newspaper3k](https://img.shields.io/badge/Newspaper3k-Article-lightgrey)

A lightweight NLP tool for analyzing sentiment from web articles and local text files.

一个简单的 NLP 情感分析工具，支持网页文章和本地 TXT 文本。

</div>

---

## ✨ Features / 功能

- 🌐 Extract article content from URLs / 从 URL 获取文章内容
- 📝 Generate article summaries / 自动生成文章摘要
- 📄 Read local TXT files / 读取本地 TXT 文件
- ❤️ Analyze sentiment polarity / 分析文本情感倾向
- 📊 Return sentiment scores / 输出情感分数

---

## 🛠️ Tech Stack / 技术栈

`Python` · `NLTK` · `TextBlob` · `Newspaper3k`

---

## 🚀 Quick Start / 快速开始

### 1. Install dependencies / 安装依赖

```bash
pip install -r requirements.txt
```

### 2. Download NLTK data / 下载 NLTK 数据

```bash
python -m nltk.downloader punkt_tab
```

### 3. Run / 运行

```bash
python main.py
```

---

## 💻 Usage / 使用方法

Choose the input type:

选择输入类型：

```text
Choose input type (url/txt):
```

### 🌐 URL Mode / 网页模式

```text
url
```

Enter an article URL.  
输入文章网址后，程序会提取文章内容、生成摘要并进行情感分析。

### 📄 TXT Mode / 文本模式

```text
txt
```

Enter the name of a local `.txt` file.  
输入本地 TXT 文件名，程序会读取文本并进行情感分析。

---

## 📊 Sentiment Score / 情感分数

TextBlob returns a polarity score:

TextBlob 会返回一个情感倾向分数：

| Score / 分数 | Sentiment / 情感 |
|---|---|
| `< 0` | 😞 Negative / 负面 |
| `0` | 😐 Neutral / 中性 |
| `> 0` | 😊 Positive / 正面 |

The polarity score generally ranges from **-1 to +1**.

情感分数通常位于 **-1 到 +1** 之间。

---

## 📁 Project Structure / 项目结构

```text
Sentiment-Analyzer/
│
├── main.py
├── test.txt
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚠️ Notes / 注意事项

TextBlob works best with English text.

TextBlob 对英文文本的情感分析效果更好。

Complex expressions such as metaphors, irony, and sarcasm may not always be interpreted correctly.

对于隐喻、反讽等复杂表达，分析结果可能无法准确反映真实语义。

---

<div align="center">

### 🧠 Simple NLP. Simple Sentiment Analysis.

**Built with Python**

</div>