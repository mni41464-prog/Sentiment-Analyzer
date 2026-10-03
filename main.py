from newspaper import Config
from newspaper import Article
from textblob import TextBlob
import matplotlib
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
import re

choice = input("Choose input type (url/txt): ")


if choice == "url":
    url = input("Enter article URL: ")
    config = Config()
    config.browser_user_agent = "Mozilla/5.0"
    article = Article(url, config=config)
    article.download()
    article.parse()
    text = article.text

elif choice == "txt":
    file_name = input("Enter txt file name: ")

    with open(file_name, "r", encoding="utf-8") as file:
        text = file.read()
else:
    print("Invalid input type")
    exit()


blob = TextBlob(text)
sentiment = blob.sentiment.polarity


print("\nText:")
print(text)
print("\nSentiment Score:")
print(sentiment)

if len(text) < 5000:
    parts = re.split(r'[.!?;,]+', text)

else:
    parts = re.split(r'[.!?]+', text)


sentences = [   part.strip()
                for part in parts
                if part.strip()
             ]



scores = []

for sentence in sentences:
    score = TextBlob(sentence).sentiment.polarity
    scores.append(score)
    print(sentence)
    print("Score:",score)
    print()

positions = []
start = 0

for sentence in sentences:
    position = text.find(sentence, start)
    positions.append(position)
    start = position + len(sentence)

max_points = 50

if len(scores) > max_points:
    group_size = len(scores) // max_points

    display_scores = []
    display_positions = []

    for i in range(0, len(scores), group_size):
        group = scores[i:i + group_size]
        average = sum(group) / len(group)

        display_scores.append(average)
        display_positions.append(positions[i])
else:
    display_scores = scores
    display_positions = positions

print("Original points:", len(scores))
print("Display points:", len(display_scores))


plt.figure(figsize=(10, 5))

plt.plot(display_positions,
          display_scores,
          marker="o",
          markersize=7,
          linewidth=2.2,
          color="#6366F1")

max_score = max(display_scores)
min_score = min(display_scores)
max_index = display_scores.index(max_score)
min_index = display_scores.index(min_score)
max_position = display_positions[max_index]
min_position = display_positions[min_index]

plt.scatter(
    max_position,
    max_score,
    color="#16A34A",
    s=100,
    zorder=5,
    label="Most Positive"
)
plt.scatter(
    min_position,
    min_score,
    color="#DC2626",
    s=100,
    zorder=5,
    label="Most Negative"
)


plt.legend()



plt.axhspan(0, 1, color="#DCFCE7", alpha=0.35)
plt.axhspan(-1, 0, color="#FEE2E2", alpha=0.35)

plt.axhline(0,
            color="#64748B",
            linestyle="--",
            linewidth=1.2)

plt.ylim(-1, 1)

plt.title("Sentiment Flow",
          fontsize=16,
          fontweight="bold"
          )
plt.xlabel("Character Position")
plt.ylabel("Polarity Score")

plt.grid(axis="y",
         linestyle="--",
         alpha=0.25)

plt.tight_layout()
plt.show()








