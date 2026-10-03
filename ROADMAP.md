# 🗺️ Sentiment Analyzer Roadmap

> **From sentiment scoring to understanding emotional structure.**  
> **从“判断情绪”逐渐走向“理解情绪为什么发生变化”。**

The current version can analyze sentiment flow, detect major emotional changes, and map those changes back to the original text.

当前版本已经可以分析情感走势、检测关键情绪变化，并将变化重新定位到原文。

The long-term goal is to make the system understand not only **what the emotion is**, but also:

> **Where did it change? Why did it change? What caused it? What may happen next?**

未来希望它不只是告诉我们“情绪是什么”，而是进一步理解：

> **情绪在哪里发生变化？为什么变化？什么内容导致了变化？接下来可能如何发展？**

---

## 🧠 Phase 1 — Smarter Sentiment Understanding
## 更智能的情绪理解

### Context-Aware Sentiment / 上下文情感分析

Current sentiment analysis mainly evaluates individual text regions.

Future versions could consider surrounding context:

```text
Previous Context
       ↓
Current Sentence
       ↓
Following Context
       ↓
Context-Aware Sentiment
```

不再孤立地判断一句话，而是结合前后文理解它真正表达的情绪。

---

### 🎭 Sarcasm & Irony Detection / 反讽与讽刺识别

Example:

```text
"Oh great, another three-hour meeting."
```

A simple sentiment model may interpret **"great"** as positive.

A smarter model should recognize that the actual meaning may be negative.

未来希望模型能够识别：

- Sarcasm / 讽刺
- Irony / 反讽
- Hidden negativity / 隐性负面表达
- Emotional contradiction / 表面情绪与真实语义冲突

---

### 🌍 Multilingual Sentiment / 多语言情感分析

Extend the project beyond English:

```text
English
Chinese
Japanese
...
   ↓
Unified Sentiment Analysis
```

未来希望支持真正的多语言情感分析，而不是简单依赖英文词典。

---

## ⚡ Phase 2 — Emotional Turning Points
## 情绪转折点

Not every sentiment change is equally important.

The analyzer could automatically identify meaningful emotional turning points:

```text
Stable
Stable
Stable
   ↓
Sudden Drop  ← Turning Point
   ↓
Negative
Negative
   ↓
Recovery     ← Turning Point
```

未来不仅寻找最大变化，还可以检测：

- Sudden emotional shifts / 突然的情绪变化
- Emotional recovery / 情绪恢复
- Long negative periods / 持续低情绪区域
- Emotional peaks / 情绪高潮
- Repeated emotional oscillation / 反复情绪波动

---

## 🔍 Phase 3 — Why Did the Emotion Change?
## 为什么情绪发生变化？

This is one of the most interesting future directions.

Instead of only reporting:

```text
Sentiment dropped by -0.72
```

the system could attempt to explain:

```text
Strong Negative Shift Detected

Possible Trigger:
"The company announced that 2,000 employees
would lose their jobs."

Before:
Neutral discussion

After:
Strong negative sentiment

Possible reason:
Job-loss announcement
```

也就是说，从：

> **“这里情绪下降了。”**

进一步发展到：

> **“这里情绪下降，可能是因为文本中发生了这件事。”**

This would move the project from **sentiment detection** toward **event-aware emotional analysis**.

---

## 🧩 Phase 4 — Emotion Categories
## 从正负情绪到具体情绪

Positive / negative scores are very limited.

Future versions could recognize richer emotions:

```text
Joy        😄
Sadness    😢
Anger      😠
Fear       😨
Surprise   😮
Disgust    🤢
Neutral    😐
```

Then the visualization could become an **emotional timeline** rather than only a polarity curve.

未来可以从单纯的：

```text
Positive ←→ Negative
```

升级为：

```text
Joy → Surprise → Fear → Sadness → Hope
```

这样会更接近真正的“文本情绪结构”。

---

## 🧠 Phase 5 — Deep Learning Upgrade
## 深度学习升级

Replace or complement the current TextBlob-based analyzer with modern NLP models.

Possible directions:

- PyTorch
- Transformers
- BERT / RoBERTa
- Sentence Transformers
- Fine-tuned sentiment models
- Emotion classification models

Possible architecture:

```text
Text
 ↓
Tokenizer
 ↓
Transformer
 ↓
Context Representation
 ↓
Sentiment / Emotion Model
 ↓
Visualization & Interpretation
```

这一步会把项目从基于词典的情感分析逐渐升级到真正的上下文 NLP 模型。

---

## 📖 Phase 6 — Narrative Intelligence
## 故事与文章的“情绪结构”

For long-form text such as novels, news articles, speeches, or stories, the analyzer could attempt to discover larger emotional structures.

For example:

```text
Beginning
   ↓
Hope
   ↓
Conflict
   ↓
Emotional Decline
   ↓
Lowest Point
   ↓
Recovery
   ↓
Ending
```

Possible features:

- Detect emotional arcs / 自动识别情绪弧线
- Compare chapters / 比较章节情绪
- Detect climax / 寻找情绪高潮
- Detect emotional resolution / 判断情绪是否得到缓解
- Compare characters or topics / 比较人物或主题的情绪变化

---

## 🧭 Phase 7 — Topic × Emotion
## “什么事情”对应“什么情绪”

A future version could combine topic detection with sentiment analysis.

Instead of:

```text
Position 3200 → Sentiment -0.68
```

it could produce:

```text
Topic: Employment
Sentiment: Negative

Topic: Technology
Sentiment: Positive

Topic: Economy
Sentiment: Mixed
```

This could be especially useful for:

- News analysis / 新闻分析
- Reviews / 评论分析
- Speeches / 演讲分析
- Reports / 报告分析
- Social text / 社交文本分析

---

## 🔗 Phase 8 — Emotional Cause Graph
## 情绪因果关系图

A more experimental idea:

Instead of representing a document only as a line chart, represent important events and emotional changes as a graph.

```text
Event A
  │
  ▼
Concern
  │
  ▼
Event B ─────→ Strong Negative Shift
                 │
                 ▼
              Event C
                 │
                 ▼
              Recovery
```

The goal would be to explore relationships between:

```text
Event → Context → Emotion → Change
```

这会让项目从“画情绪曲线”进一步走向“分析文本中的事件与情绪关系”。

---

## 🔮 Experimental Ideas
## 一些脑洞

Some ideas may be experimental rather than guaranteed features:

- **Emotional Summary**  
  自动生成整篇文本的情绪变化摘要

- **Ask the Text**  
  允许用户提问：“为什么这里情绪突然下降？”

- **Compare Two Texts**  
  比较两篇新闻、小说或评论的情绪结构

- **Character Emotion Tracking**  
  在小说中分别追踪不同人物的情绪变化

- **Automatic Chapter Analysis**  
  自动识别章节并生成章节级情绪地图

- **Emotion Heatmap**  
  直接在原文上用颜色标记不同情绪区域

- **Interactive Timeline**  
  点击曲线上的点，直接跳转到对应原文

- **Emotion Search**  
  搜索“全文最愤怒的部分”“最悲伤的部分”“情绪反转最大的地方”

- **Emotion-Based Text Navigation**  
  不按照页码阅读，而按照情绪节点浏览长文本

- **Local AI Model Support**  
  尝试使用本地模型进行更复杂的语义分析

---

## 🎯 Long-Term Vision / 长期目标

The project started with a simple question:

> **Is this text positive or negative?**

It is gradually evolving toward a more interesting question:

> **How does emotion develop throughout a text, what causes it to change, and what does that reveal about the text itself?**

这个项目最开始解决的是一个很简单的问题：

> **“这篇文本是积极还是消极？”**

未来希望它逐渐能够回答：

> **“情绪是怎样发展的？在哪里发生转折？什么内容导致了变化？这些变化又反映了文本怎样的结构？”**

```text
Sentiment Score
      ↓
Sentiment Flow
      ↓
Sentiment Change
      ↓
Turning Points
      ↓
Emotion Recognition
      ↓
Context Understanding
      ↓
Event Understanding
      ↓
Why Did It Change?
```

**The goal is not simply to produce more scores — it is to make those scores increasingly meaningful.**

**目标不是产生更多数字，而是让这些数字逐渐具有真正的语义。**