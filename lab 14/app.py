from textblob import TextBlob

def hello(name):
    return f'Hello {name}'


def extract_sentiment(text):
    text = TextBlob(text)

    return text.sentiment.polarity


def text_contain_word(word: str, text: str):
    return word in text


def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 0:
        return n * factorial(n - 1)
    else:
        return "n < 0!"
