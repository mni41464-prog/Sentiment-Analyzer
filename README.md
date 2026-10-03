# 📊 Sentiment Analyzer

> **Visualize how sentiment flows, changes, and shifts throughout a text.**  
> **不只判断一篇文章是“积极还是消极”，而是观察情绪如何在文本中流动与变化。**

A Python sentiment analysis project built with **TextBlob**, **Newspaper3k**, and **Matplotlib**.

一个基于 Python 的文本情感分析项目，支持网页文章与本地文本分析、长文本情感趋势可视化以及关键情绪变化定位。

---

## ✨ Features / 功能

### 🌐 Flexible Text Input / 灵活的文本输入

- Analyze online articles from a **URL**
- Analyze local **TXT files**
- Automatically extract article text with Newspaper3k

支持网页 URL 与本地 TXT 文件，并可自动提取网页正文。

### 💬 Sentiment Analysis / 情感分析

- Calculate the **overall sentiment score**
- Analyze sentiment at the **segment level**
- Polarity ranges approximately from `-1` to `1`

不仅计算全文情感分数，还会进一步分析文本内部不同区域的情感倾向。

### 📈 Sentiment Flow / 情感走势

Instead of reducing an entire text to a single score, the analyzer tracks sentiment throughout the text.

不同于只输出一个总分，本项目会追踪情感在整篇文本中的变化过程。

```text
Text
 │
 ├── Segment 1  →  Sentiment Score
 ├── Segment 2  →  Sentiment Score
 ├── Segment 3  →  Sentiment Score
 │
 ▼
Sentiment Flow
```

The most positive and negative regions are automatically highlighted.

同时自动标记：

- 🟢 **Most Positive Region / 最积极区域**
- 🔴 **Most Negative Region / 最消极区域**

### ⚡ Sentiment Change / 情绪变化

The project also measures the difference between consecutive sentiment regions:

```text
Sentiment Change = Current Score - Previous Score
```

通过比较相邻区域的情感分数，可以进一步发现：

- ▲ **Strongest Rise / 最大情绪上升**
- ▼ **Strongest Drop / 最大情绪下降**
- ⚡ **Most Dramatic Change / 最剧烈情绪变化**

### 🔎 Before & After Context / 变化前后原文定位

For the most dramatic sentiment shift, the analyzer displays:

```text
Most Dramatic Sentiment Change
------------------------------
Position: ...
Change: ...

Before:
Position: ... - ...
Original text...

After:
Position: ... - ...
Original text...
```

不仅告诉你“哪里变化最大”，还会定位到原文，并显示变化前后的文本内容。

---

## 📚 Long-Text Analysis / 长文本分析

Long texts can contain hundreds or thousands of sentiment segments.

Displaying every point directly would make the graph difficult to read.

长篇文章或书籍可能产生大量情感数据点，如果全部直接绘制，图表会非常拥挤。

This project therefore:

```text
Full Text Analysis
        ↓
All Segments Receive Sentiment Scores
        ↓
Automatic Grouping
        ↓
Average Sentiment per Group
        ↓
Readable Visualization
```

**The full text is still analyzed.**

The project does **not** randomly sample only a few sections.  
Instead, sentiment results are automatically grouped for visualization while preserving their relationship with the original text.

**全文仍然参与情感分析。**

长文本只是在可视化阶段进行自动分组和平均，从而减少图表中的显示点数量，而不是随机丢弃文本。

---

## 📍 Character Position Mapping / 字符位置映射

Each analyzed region keeps track of its position in the original text.

每个分析区域都会保存其在原文中的字符位置：

```text
Original Text
0 ------------------------------------------> N

        ↑
   Sentiment Region
   Start Position
   End Position
```

This makes it possible to connect visualization results back to the exact original content.

因此，当程序发现关键情绪区域或剧烈变化时，可以重新定位到对应原文，而不仅仅得到一个抽象的分数。

---

## 🔄 How It Works / 工作流程

```text
URL / TXT
    │
    ▼
Text Loading
文本加载
    │
    ▼
Text Segmentation
文本分段
    │
    ▼
Segment Sentiment Analysis
分段情感分析
    │
    ▼
Long-Text Aggregation
长文本显示聚合
    │
    ▼
Sentiment Flow
情感走势
    │
    ▼
Sentiment Change Analysis
情绪变化分析
    │
    ▼
Key Change Detection
关键变化检测
    │
    ▼
Before / After Context
变化前后原文定位
    │
    ▼
Visualization
可视化
```

---

## 🧩 Code Structure / 代码结构

The analysis pipeline has been separated into reusable functions:

```python
load_text()
split_text()
analyze_sentiment()
prepare_display_data()
calculate_changes()
find_key_changes()
print_dramatic_changes()
plot_results()
```

Each function is responsible for one stage of the pipeline.

经过重构后，不同功能被拆分到独立函数中，使主流程更加清晰，也方便后续继续扩展。

---

## 🛠️ Tech Stack / 技术栈

| Technology | Purpose / 用途 |
|---|---|
| Python | Core programming language / 核心开发语言 |
| TextBlob | Sentiment polarity analysis / 情感极性分析 |
| Newspaper3k | Article extraction from URLs / 网页文章提取 |
| Matplotlib | Sentiment visualization / 情感可视化 |
| Regex | Text segmentation and position tracking / 文本分段与位置追踪 |

---

## 🚀 Installation / 安装

Clone the repository and install the dependencies:

克隆项目并安装依赖：

```bash
pip install -r requirements.txt
```

NLTK data may also be required:

```bash
python -m nltk.downloader punkt_tab
```

---

## ▶️ Usage / 使用方法

Run:

```bash
python main.py
```

Then choose the input type:

```text
Choose input type (url/txt):
```

For an online article:

```text
url
```

For a local text file:

```text
txt
```

The program will analyze the text and display the sentiment results and visualizations.

程序会自动完成文本分析，并输出关键情绪变化与可视化结果。

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

## 📌 Version / 当前版本

### v1.2.0

**Sentiment Change & Code Refactoring**

- Added sentiment change visualization  
  新增情绪变化可视化

- Added strongest rise and drop detection  
  新增最大情绪上升与下降检测

- Added most dramatic sentiment change detection  
  新增最剧烈情绪变化检测

- Added exact Before / After text context  
  新增变化前后原文定位

- Improved long-text position tracking  
  优化长文本字符位置追踪

- Refactored the analysis pipeline into reusable functions  
  将分析流程重构为多个独立函数

---

## 🗺️ Roadmap / 后续计划

Possible future improvements:

未来可以继续探索：

- Turning-point detection / 情绪转折点检测
- Context-aware sentiment analysis / 上下文情感分析
- Sarcasm and irony detection / 反讽与讽刺识别
- Multilingual sentiment analysis / 多语言情感分析
- Transformer / BERT based models
- PyTorch-based deep learning sentiment model

---

## ⚠️ Limitations / 当前局限

The current version primarily relies on **TextBlob**, which works best with English text and lexicon-based sentiment patterns.

当前版本主要基于 TextBlob，因此更适合英文文本。对于中文、复杂上下文、文学表达、反讽和讽刺等情况，分析结果可能存在明显局限。

This project should therefore be viewed as an **exploratory sentiment analysis and visualization tool**, rather than a system that perfectly understands human emotion.

因此，本项目更适合作为一个**情感分析与文本情绪可视化工具**，而不是能够完全理解人类情绪的系统。

---

## 📄 License

This project is intended for learning, experimentation, and further development.

本项目主要用于学习、实验与后续开发。