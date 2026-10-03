from newspaper import Config
from newspaper import Article
from textblob import TextBlob


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













