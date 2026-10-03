from newspaper import Config
from newspaper import Article
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
import math

def load_text():
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

    if not text.strip():
        print("No text found.")
        exit()
    return text

text = load_text()

blob = TextBlob(text)
sentiment = blob.sentiment.polarity


print("\nSentiment Score:")
print(sentiment)


def split_text(text):
    if len(text) < 5000:
        pattern = r'[^.!?;,]+'

    else:
        pattern = r'[^.!?]+'

    sentences = []
    positions = []
    end_positions = []

    for match in re.finditer(pattern, text):
        raw_sentence = match.group()
        sentence = raw_sentence.strip()

        if sentence:
            leading_spaces = len(raw_sentence) - len(raw_sentence.lstrip())
            start_position = match.start() + leading_spaces
            end_position = start_position + len(sentence)
            sentences.append(sentence)
            positions.append(start_position)
            end_positions.append(end_position)
    return sentences, positions, end_positions

sentences, positions, end_positions = split_text(text)

def analyze_sentiment(sentences):
    scores = []

    for sentence in sentences:
        score = TextBlob(sentence).sentiment.polarity
        scores.append(score)
    return scores
scores = analyze_sentiment(sentences)

def prepare_display_data(
        text,
        sentences,
        scores,
        positions,
        end_positions,
        max_points=50
):

    if len(scores) > max_points:
        group_size = math.ceil(len(scores) / max_points)

        display_scores = []
        display_positions = []
        display_end_positions = []
        display_texts = []

        for i in range(0, len(scores), group_size):
            group = scores[i:i + group_size]
            average = sum(group) / len(group)

            start_position = positions[i]
            end_index = min(i + group_size, len(sentences)) - 1
            end_position = end_positions[end_index]

            display_scores.append(average)
            display_positions.append(start_position)
            display_end_positions.append(end_position)
            display_texts.append(text[start_position:end_position])


    else:
        display_scores = scores
        display_positions = positions
        display_end_positions = end_positions
        display_texts = sentences
    return(
        display_scores,
        display_positions,
        display_end_positions,
        display_texts
    )

display_scores, display_positions, display_end_positions, display_texts = (
    prepare_display_data(
        text,
        sentences,
        scores,
        positions,
        end_positions
    )
)

print("Original points:", len(scores))
print("Display points:", len(display_scores))

def calculate_changes(display_scores,display_positions):
    changes = []

    for i in range(1, len(display_scores)):
        change = display_scores[i] - display_scores[i - 1]
        changes.append(change)

    change_positions = display_positions[1:]
    return changes, change_positions
changes, change_positions = calculate_changes(display_scores, display_positions)

print("Sentiment changes:", changes)

def find_key_changes(changes,display_positions):
    most_dramatic_change = max(changes, key=abs)
    dramatic_change_index = changes.index(most_dramatic_change) + 1
    dramatic_position = display_positions[dramatic_change_index]

    max_change = max(changes)
    min_change = min(changes)
    max_change_index = changes.index(max_change) + 1
    min_change_index = changes.index(min_change) + 1
    rise_position = display_positions[max_change_index]
    drop_position = display_positions[min_change_index]
    return (most_dramatic_change, dramatic_change_index, dramatic_position,max_change,min_change,rise_position, drop_position)

(   most_dramatic_change,
    dramatic_change_index,
    dramatic_position,
    max_change,
    min_change,
    rise_position,
    drop_position
    ) = (find_key_changes
         (   changes,
             display_positions
             ))

def print_dramatic_changes(
        most_dramatic_change,
        dramatic_change_index,
        dramatic_position,
        display_positions,
        display_end_positions,
        display_texts
        ):

    before_index = dramatic_change_index - 1
    after_index = dramatic_change_index
    print("\nMost Dramatic Sentiment Change")
    print("------------------------------")
    print("Position:", dramatic_position)
    print("Change:", most_dramatic_change)
    print("\nBefore:")
    print(
        "Position:",
        display_positions[before_index],
        "-",
        display_end_positions[before_index]
    )
    print(display_texts[before_index])
    print("\nAfter:")
    print(
        "Position:",
        display_positions[after_index],
        "-",
        display_end_positions[after_index]
    )
    print(display_texts[after_index])

print_dramatic_changes(
    most_dramatic_change,
    dramatic_change_index,
    dramatic_position,
    display_positions,
    display_end_positions,
    display_texts
)

def plot_results(
        display_scores,
        display_positions,
        changes,
        change_positions,
        max_change,
        min_change,
        rise_position,
        drop_position,
):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

    ax1.plot(display_positions,
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

    ax1.scatter(
        max_position,
        max_score,
        color="#16A34A",
        s=100,
        zorder=5,
        label="Most Positive"
    )
    ax1.scatter(
        min_position,
        min_score,
        color="#DC2626",
        s=100,
        zorder=5,
        label="Most Negative"
    )

    ax1.legend()

    ax1.axhspan(0, 1, color="#DCFCE7", alpha=0.35)
    ax1.axhspan(-1, 0, color="#FEE2E2", alpha=0.35)

    ax1.axhline(0,
                color="#64748B",
                linestyle="--",
                linewidth=1.2)

    ax1.set_ylim(-1, 1)

    ax1.set_title("Sentiment Flow",
                  fontsize=16,
                  fontweight="bold"
                  )
    ax1.set_xlabel("Character Position")
    ax1.set_ylabel("Polarity Score")

    ax1.grid(axis="y",
             linestyle="--",
             alpha=0.25)

    ax2.plot(
        change_positions,
        changes,
        marker="o",
        markersize=6,
        linewidth=2.2,
        color="#0891B2"
    )

    ax2.scatter(
        rise_position,
        max_change,
        color="#16A34A",
        marker="^",
        s=120,
        zorder=5,
        label="Strongest Rise"
    )

    ax2.scatter(
        drop_position,
        min_change,
        color="#DC2626",
        marker="v",
        s=120,
        zorder=5,
        label="Strongest Drop"
    )

    ax2.legend()

    ax2.axhspan(
        0,
        1,
        color="#DCFCE7",
        alpha=0.35
    )

    ax2.axhspan(
        -1,
        0,
        color="#FEE2E2",
        alpha=0.35
    )

    ax2.axhline(
        0,
        color="#64748B",
        linestyle="--",
        linewidth=1.2
    )

    ax2.set_title(
        "Sentiment Change",
        fontsize=16,
        fontweight="bold"
    )

    ax2.set_xlabel("Character Position")
    ax2.set_ylabel("Sentiment Change")

    ax2.grid(
        axis="y",
        linestyle="--",
        alpha=0.25
    )

    plt.tight_layout()
    plt.show()

plot_results(
    display_scores,
    display_positions,
    changes,
    change_positions,
    max_change,
    min_change,
    rise_position,
    drop_position
)








