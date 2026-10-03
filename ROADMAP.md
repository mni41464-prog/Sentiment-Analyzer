# 🗺️ Sentiment Analyzer Roadmap / 项目路线图

This document records the ideas, limitations, and possible future directions of Sentiment Analyzer.

本文用于记录 Sentiment Analyzer 当前发现的问题，以及未来可能实现的功能和升级方向。

---

## 📌 Current Version / 当前版本

### v1.1.0 — Sentiment Flow

The current version can:

- Analyze web articles from URLs
- Analyze local TXT files
- Calculate overall sentiment polarity
- Analyze sentiment by text segment
- Handle long texts automatically
- Compress long-text results into approximately 50 visualization regions
- Preserve approximate character positions in the original text
- Visualize sentiment changes
- Highlight the most positive and negative regions

当前版本已经支持：

- 分析网页 URL 中的文章
- 分析本地 TXT 文本
- 计算全文整体情感倾向
- 对文本进行分段情感分析
- 自动处理长文本
- 将长文本分析结果压缩为约 50 个可视化区域
- 保留对应内容在原文中的大致字符位置
- 绘制全文情感变化趋势
- 标记最积极和最消极的情绪区域

---

# 🚀 Future Directions / 未来方向

## 1. 📈 Sentiment Change Detection / 情绪变化检测

The current version measures the sentiment level at different positions in the text.

当前版本主要回答：

> What is the sentiment at this position?  
> 这个位置的情绪是什么？

For example:

```text
Segment 1:  0.8
Segment 2:  0.8
Segment 3:  0.2
Segment 4: -0.6
```

A future version could also calculate the change between neighboring sentiment values:

未来可以进一步计算相邻区域之间的情绪变化：

```text
Sentiment Change = Current Sentiment - Previous Sentiment
情绪变化 = 当前情绪 - 上一位置情绪
```

For example:

```text
0.8 →  0.8    Change:  0.0   Stable / 持平
0.8 →  0.2    Change: -0.6   Falling / 下降
0.2 → -0.6    Change: -0.8   Sharp Drop / 剧烈下降
```

This would allow the program to distinguish between:

这可以让程序进一步区分：

> What is the current emotion?  
> 当前是什么情绪？

and:

> How is the emotion changing?  
> 情绪正在如何变化？

---

## 2. ⚡ Emotional Turning Point Detection / 情绪转折点检测

After calculating sentiment changes, the program could automatically detect regions where emotion changes dramatically.

在拥有情绪变化数据之后，可以进一步自动寻找全文中情绪变化最剧烈的位置。

For example:

```text
Positive / 积极
      ↓
Positive / 积极
      ↓
Neutral / 中性
      ↓
Negative / 消极   ← Emotional Turning Point / 情绪转折点
```

The current version identifies:

当前版本已经可以寻找：

```text
🟢 Most Positive Region / 最积极区域
🔴 Most Negative Region / 最消极区域
```

A future version could additionally identify:

未来还可以加入：

```text
🟡 Strongest Emotional Change / 情绪变化最剧烈区域
```

This would help locate not only emotional extremes, but also important transitions in the text.

这样不仅可以知道全文“哪里最积极、哪里最消极”，还可以知道“情绪在哪里发生了明显转折”。

---

## 3. 🧠 Context-Aware Sentiment Analysis / 上下文情感分析

The current TextBlob-based approach mainly analyzes lexical sentiment and has limited understanding of deeper context.

当前基于 TextBlob 的方法主要依赖词汇层面的情感信息，对复杂上下文的理解能力有限。

For example:

```text
"You are really smart."
```

may express genuine praise.

可能是真正的夸奖。

But:

```text
"You are really smart. You managed to break the easiest thing."
```

may express a completely different meaning depending on context.

但结合后面的语境，这句话可能表达完全不同的真实情绪。

A future version could use context-aware NLP models to analyze relationships between words, sentences, and surrounding context.

未来可以尝试使用能够理解上下文的 NLP 模型，而不仅仅根据单独的情感词汇进行判断。

---

## 4. 🎭 Sarcasm & Irony Detection / 反讽与阴阳怪气识别

Sarcasm is a difficult problem for traditional sentiment analysis.

反讽是传统情感分析中比较困难的问题之一。

For example:

```text
"Great. My computer crashed again."
```

The word:

```text
"Great"
```

looks positive.

单独看是一个明显的正面表达。

But:

```text
"My computer crashed again."
```

provides negative context.

但后面的“电脑又崩溃了”明显是负面事件。

The combination may indicate sarcasm:

两者结合起来可能形成反讽：

```text
Positive Expression / 正面表达
            +
Negative Context / 负面语境
            ↓
Possible Sarcasm / 可能存在反讽
```

Future versions could explore models specifically designed to understand contextual contradiction, sarcasm, and irony.

未来可以进一步研究上下文矛盾、反讽以及阴阳怪气等更加复杂的语义现象。

---

## 5. 🤖 Deep Learning NLP Model / 深度学习 NLP 模型

A future major version could replace or complement TextBlob with a modern neural NLP model.

未来的大版本可以尝试使用现代深度学习 NLP 模型替代或补充 TextBlob。

Possible evolution:

可能的发展路线：

```text
TextBlob
   ↓
Lexical Sentiment Analysis
词汇情感分析
   ↓
Context-Aware NLP
上下文 NLP
   ↓
Transformer / BERT
   ↓
Deep Learning Sentiment Model
深度学习情感模型
```

This would also connect the project with PyTorch and modern deep learning.

这也可以让项目进一步与 PyTorch 和现代深度学习结合。

Possible topics include:

可能涉及：

- Tokenization / 文本分词与 Token 化
- Embeddings / 词向量与文本表示
- Neural Networks / 神经网络
- Loss Functions / 损失函数
- Model Training / 模型训练
- Transformers
- BERT-based Sentiment Classification / 基于 BERT 的情感分类

This could become the foundation of a future **v2.0**.

这可以作为未来 **v2.0** 的主要升级方向。

---

## 6. 🌏 Multilingual Sentiment Analysis / 多语言情感分析

The current version mainly targets English text because TextBlob is much more suitable for English sentiment analysis.

当前版本主要面向英文文本，因为 TextBlob 更适合英文情感分析。

A future version could explore multilingual models capable of analyzing:

未来可以尝试支持：

```text
English / 英文
Chinese / 中文
Multilingual Text / 多语言文本
```

This would allow the analyzer to work with a much wider range of text sources.

这样可以让项目真正扩展到更加广泛的文本内容。

---

# 🎯 Long-Term Goal / 长期目标

The current project mainly answers:

当前项目主要回答：

> **What is the sentiment of this text?**  
> **这段文本是什么情绪？**

The next step could be:

下一步可以进一步回答：

> **How does the emotion change throughout the text?**  
> **情绪在全文中是如何变化的？**

And eventually:

最终希望逐渐探索：

> **What does the author actually mean in context?**  
> **结合上下文，作者真正想表达什么？**

The long-term goal is to gradually move from:

长期方向是从：

```text
Sentiment Score
情感打分

      ↓

Sentiment Flow
情感趋势

      ↓

Sentiment Change
情绪变化

      ↓

Context Understanding
上下文理解

      ↓

Sarcasm & Deeper Semantic Understanding
反讽与更深层语义理解
```

The goal is not simply to add more features, but to gradually explore deeper levels of natural language understanding.

项目未来的目标并不只是不断增加功能，而是逐渐从简单的情感打分，深入到对文本情绪变化、上下文以及真实语义的理解。

---

<div align="center">

### From Sentiment Scores to Context Understanding

### 从情感打分，到上下文理解

**Sentiment Analyzer Roadmap**

</div>