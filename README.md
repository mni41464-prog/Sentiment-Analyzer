<div align="center">

# 🧠 Sentiment Analyzer

### Article & Long-Text Sentiment Analysis with Visualized Emotional Flow

### 网页文章 · 本地文本 · 长文本情感趋势分析与可视化

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![TextBlob](https://img.shields.io/badge/TextBlob-Sentiment-orange)
![Newspaper3k](https://img.shields.io/badge/Newspaper3k-Article-lightgrey)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue)
![Version](https://img.shields.io/badge/Version-v1.1.0-purple)

A lightweight NLP tool that analyzes sentiment from web articles and local text files,
tracks emotional changes throughout the text, and visualizes the overall sentiment flow.

一个轻量级 NLP 情感分析工具，支持网页文章和本地文本，
不仅能够计算全文情感倾向，还能够分析文本内部的情绪变化并进行可视化。

</div>

---

## ✨ Overview / 项目简介

Traditional sentiment analysis often returns only one final score for an entire text.

For example:

```text
Sentiment Score: 0.13
```

While useful, a single score cannot explain **where positive or negative emotions appear inside the text**.

Sentiment Analyzer extends this idea by analyzing the internal emotional structure of the text.

Instead of only asking:

> Is this text positive or negative?

the program can also explore:

> How does sentiment change throughout the text?

---

传统的文本情感分析通常只返回一个最终分数，例如：

```text
Sentiment Score: 0.13
```

这个结果可以描述全文的整体情感倾向，但无法告诉我们：

**文本中的情绪究竟在哪里发生变化？**

因此，本项目在整体情感分析的基础上进一步加入文本分段分析和趋势可视化。

除了回答：

> 这篇文本整体偏正面还是负面？

还可以进一步观察：

> 情绪在全文中是如何变化的？

---

## 🚀 Key Features / 核心功能

### 🌐 Web Article Analysis / 网页文章分析

Enter an article URL and the program automatically extracts the main article text using Newspaper3k.

输入网页 URL 后，程序会自动提取网页中的文章正文并进行情感分析。

```text
Choose input type (url/txt): url
Enter article URL: ...
```

---

### 📄 Local TXT Analysis / 本地文本分析

Local `.txt` files are also supported.

This makes it possible to analyze:

- Articles
- Essays
- Reviews
- Speeches
- Literary excerpts
- Long-form text

同时支持读取本地 `.txt` 文件，因此不仅可以分析网页文章，也可以分析已经保存到本地的文本内容。

```text
Choose input type (url/txt): txt
Enter txt file name: test.txt
```

---

### ❤️ Overall Sentiment Analysis / 全文情感分析

The complete text is analyzed using TextBlob to calculate an overall polarity score.

程序首先使用 TextBlob 对全文进行整体情感分析。

The polarity score generally ranges from:

```text
-1.0  ←────────  0  ────────→  +1.0

Negative        Neutral        Positive
```

| Score / 分数 | Sentiment / 情感 |
|---|---|
| `< 0` | 😞 Negative / 负面 |
| `0` | 😐 Neutral / 中性 |
| `> 0` | 😊 Positive / 正面 |

---

## 🔍 Segment-Level Sentiment Analysis / 文本分段情感分析

Instead of analyzing only the entire document, the program divides the text into smaller segments.

Each segment is analyzed independently:

```text
Full Text
   ↓
Segment 1 → Sentiment Score
Segment 2 → Sentiment Score
Segment 3 → Sentiment Score
Segment 4 → Sentiment Score
   ...
```

This makes it possible to observe emotional changes that would otherwise disappear inside a single overall score.

---

程序不会只分析全文。

文本会被划分为多个片段，并分别计算情感分数：

```text
全文
 ↓
文本片段 1 → 情感分数
文本片段 2 → 情感分数
文本片段 3 → 情感分数
文本片段 4 → 情感分数
 ...
```

因此可以观察到全文平均分数背后更加细致的情绪变化。

---

## 📚 Adaptive Long-Text Processing / 长文本自适应处理

One of the main features of the project is its handling of long texts.

一项核心功能是对较长文本进行自动处理。

### The Problem / 问题

A short paragraph may contain only a few sentiment points.

But a long article or book can contain:

```text
1000+
2000+
3000+
```

text segments.

Displaying thousands of sentiment points directly creates an extremely dense chart that is difficult to interpret.

如果直接把数千个情感分析结果全部绘制在一张图上，会导致图表非常密集，难以观察真正的情绪趋势。

### The Solution / 解决方案

The program first analyzes **every text segment**.

It does **not randomly sample only 50 pieces of the text**.

程序首先会分析 **全文所有文本片段**。

并不是简单地从长文本中随机抽取 50 个片段。

For example:

```text
Long Text
   ↓
1000 Text Segments
   ↓
Analyze ALL 1000 Segments
   ↓
1000 Sentiment Scores
```

When the number of sentiment scores becomes too large for clear visualization, the program groups them into approximately **50 regions**.

```text
1000 Sentiment Scores
        ↓
Divide into ~50 Regions
        ↓
~20 Scores per Region
        ↓
Calculate Average Sentiment
        ↓
~50 Visualization Points
```

也就是说：

```text
1000 个文本片段
        ↓
1000 个全部进行情感分析
        ↓
得到 1000 个情感分数
        ↓
按照文本顺序划分为约 50 个区间
        ↓
计算每个区间的平均情感
        ↓
最终显示约 50 个趋势点
```

This preserves information from the **entire text** while keeping the visualization readable.

这样既不会忽略长文本的大部分内容，又能够避免数千个数据点同时出现导致图表失去可读性。

---

## 📈 Sentiment Flow Visualization / 情感趋势可视化

Matplotlib is used to visualize sentiment changes throughout the text.

程序使用 Matplotlib 绘制全文情感变化趋势。

The visualization includes:

- 🔵 **Blue line** — sentiment trend
- 🟢 **Green background** — positive sentiment region
- 🔴 **Red background** — negative sentiment region
- 🟢 **Green highlighted point** — most positive region
- 🔴 **Red highlighted point** — most negative region
- 📍 **X-axis** — approximate character position in the original text
- 📊 **Y-axis** — sentiment polarity score

---

图表中的不同元素分别表示：

- 🔵 **蓝色曲线** —— 全文情感变化趋势
- 🟢 **绿色背景区域** —— 正面情感范围
- 🔴 **红色背景区域** —— 负面情感范围
- 🟢 **绿色突出点** —— 情绪最积极的区域
- 🔴 **红色突出点** —— 情绪最消极的区域
- 📍 **横坐标** —— 对应内容在原文中的字符位置
- 📊 **纵坐标** —— 情感极性分数

---

## 🟢 Most Positive & 🔴 Most Negative Regions

The program automatically identifies the highest and lowest values in the displayed sentiment trend.

For long texts, these points represent the regions with the:

```text
Highest Average Sentiment
          🟢

Lowest Average Sentiment
          🔴
```

Rather than simply identifying one isolated emotional word or sentence, grouped long-text analysis helps reveal areas where the **overall local sentiment** is particularly positive or negative.

---

程序还会自动识别情感趋势中的最高点和最低点。

对于经过分组处理的长文本：

```text
🟢 Most Positive
```

表示平均情感最积极的文本区域。

```text
🔴 Most Negative
```

表示平均情感最消极的文本区域。

因此，长文本中的最高点和最低点并不只是某一个孤立单词产生的极端分数，而更接近某一段文本整体表现出的情绪倾向。

---

## 📍 Character Position Tracking / 原文位置定位

Reducing thousands of sentiment scores to approximately 50 visualization points creates another problem:

```text
Point 1
Point 2
Point 3
...
Point 50
```

These numbers alone do not tell us where the corresponding content appears in the original text.

Therefore, the program preserves the approximate **character position** of each analyzed region.

Instead of showing only:

```text
1    2    3    4    5 ... 50
```

the X-axis corresponds to positions in the original text:

```text
0      5000      10000      15000      20000
                 Character Position
```

This makes the sentiment chart easier to connect back to the original document.

---

将大量数据压缩成约 50 个趋势点之后，如果横坐标只显示：

```text
1、2、3、4……50
```

实际上很难知道这些点对应原文的哪个位置。

因此，本项目保留文本片段在原文中的字符位置。

横坐标可以直接表示该情绪区域大约出现在全文的什么位置，从而帮助用户根据图表重新定位到原文内容。

---

## 🧩 Short Text vs Long Text / 短文本与长文本

The analyzer automatically uses different visualization strategies depending on text length.

### Short Text

For short texts:

```text
Text
 ↓
Segment Analysis
 ↓
Individual Sentiment Scores
 ↓
Direct Visualization
```

Detailed sentiment changes are preserved.

### Long Text

For long texts:

```text
Text
 ↓
All Segments Analyzed
 ↓
Large Number of Sentiment Scores
 ↓
Grouped into ~50 Regions
 ↓
Average Sentiment per Region
 ↓
Trend Visualization
```

This creates a balance between **detail** and **readability**.

---

程序会根据文本长度采用不同的展示方式。

**短文本：**

保留更加细致的文本片段情感结果。

**长文本：**

仍然分析全文，但将大量分析结果按顺序分组并计算平均值，用于观察整体趋势。

因此可以在：

```text
分析细节  ←────────→  图表可读性
```

之间取得平衡。

---

## ⚙️ How It Works / 工作流程

```text
                    URL
                     │
                     │
Local TXT ───────→ Full Text
                     │
                     ▼
              Text Segmentation
                     │
                     ▼
          Analyze Every Text Segment
                     │
                     ▼
              Sentiment Scores
                     │
             ┌───────┴───────┐
             │               │
        Short Text        Long Text
             │               │
             │               ▼
             │       Group into ~50 Regions
             │               │
             │               ▼
             │       Calculate Group Average
             │               │
             └───────┬───────┘
                     │
                     ▼
          Character Position Mapping
                     │
                     ▼
            Sentiment Visualization
                     │
              ┌──────┴──────┐
              │             │
              ▼             ▼
       Most Positive   Most Negative
             🟢             🔴
```

---

## 🛠️ Tech Stack / 技术栈

| Technology | Usage |
|---|---|
| **Python** | Main programming language |
| **TextBlob** | Sentiment polarity analysis |
| **Newspaper3k** | Web article extraction |
| **Matplotlib** | Sentiment visualization |
| **Regular Expressions** | Text segmentation |

---

## 🚀 Quick Start / 快速开始

### 1. Clone the repository

```bash
git clone <repository-url>
cd Sentiment-Analyzer
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the program

```bash
python main.py
```

---

## 💻 Usage / 使用方法

After starting the program:

```text
Choose input type (url/txt):
```

### Analyze a Web Article

```text
Choose input type (url/txt): url
Enter article URL: https://example.com/article
```

### Analyze a Local TXT File

```text
Choose input type (url/txt): txt
Enter txt file name: test.txt
```

The program will output:

```text
Original Text
Overall Sentiment Score
Segment Sentiment Scores
Number of Original Analysis Points
Number of Visualization Points
Sentiment Flow Chart
Most Positive Region
Most Negative Region
```

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

## ⚠️ Limitations / 局限性

### English-focused Sentiment Analysis

TextBlob works primarily with English text.

TextBlob 主要适用于英文情感分析。

Chinese text is not reliably analyzed by the current implementation.

当前版本暂时无法可靠地分析中文文本的情感倾向。

### Complex Language

Sentiment analysis is based largely on lexical information.

Therefore, complex language such as:

- Sarcasm
- Irony
- Metaphor
- Literary expressions
- Context-dependent emotions

may not always be interpreted correctly.

例如文学作品中的隐喻、反讽以及依赖上下文才能理解的情绪表达，可能无法被 TextBlob 准确识别。

### Sentiment Scores Are Estimates

The visualization should be interpreted as an approximate representation of lexical sentiment rather than an exact measurement of human emotion.

情感分数更适合被理解为一种文本情感倾向的近似分析，而不是对真实人类情绪的精确测量。

---

## 🏷️ Version

### v1.1.0 — Sentiment Flow Update

New features:

- 📈 Added sentiment flow visualization
- 🔍 Added segment-level sentiment analysis
- 📚 Added automatic long-text handling
- 📊 Added grouped sentiment averages for long documents
- 📍 Added original character-position tracking
- 🟢 Added most positive region detection
- 🔴 Added most negative region detection
- 🌐 Supports web articles
- 📄 Supports local TXT files

---

## 🔮 Possible Future Improvements / 未来方向

Possible future extensions include:

- More advanced NLP sentiment models
- Better multilingual sentiment analysis
- Interactive visualization
- Web interface
- More detailed text-region inspection

未来可以进一步尝试更加先进的 NLP 模型、多语言情感分析以及交互式可视化。

---

<div align="center">

### 🧠 Analyze the Text. Visualize the Emotion.

**Built with Python · TextBlob · Newspaper3k · Matplotlib**

**Version 1.1.0**

</div>