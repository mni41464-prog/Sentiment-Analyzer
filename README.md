# Article Sentiment Analyzer

A simple NLP tool that analyzes the sentiment of web articles or local text files.

一个简单的 NLP 情感分析工具，支持分析网页文章和本地 TXT 文本。

## Features / 功能

- Extract article content from a URL / 从 URL 获取文章内容
- Generate article summaries / 自动生成文章摘要
- Read local TXT files / 读取本地 TXT 文件
- Perform sentiment analysis / 文本情感分析
- Return a sentiment polarity score / 输出情感倾向分数

## Technologies

- Python
- Newspaper3k
- NLTK
- TextBlob

## Installation / 安装

Install the required packages:

```bash
pip install -r requirements.txt
```

Download the required NLTK data:

```bash
python -m nltk.downloader punkt_tab
```

## Usage / 使用

Run the program:

```bash
python main.py
```

Choose the input type:

```text
url
```

or:

```text
txt
```

Then enter an article URL or a local TXT file name.

选择 `url` 可以分析网页文章，选择 `txt` 可以分析本地文本文件。

## Sentiment Score / 情感分数

The polarity score indicates the sentiment of the text:

- `< 0` → Negative / 负面
- `0` → Neutral / 中性
- `> 0` → Positive / 正面