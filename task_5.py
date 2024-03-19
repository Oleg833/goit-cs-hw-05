import requests
from collections import Counter
import re
import matplotlib.pyplot as plt
from functools import reduce
from collections import defaultdict


def map_reduce(text):
    words = text.split()
    mapped_words = map(lambda word: (word, 1), words)
    sorted_mapped_words = sorted(mapped_words)
    reduced_words = reduce(
        lambda acc, word_val: acc.update({word_val[0]: acc.get(word_val[0], 0) + 1})
        or acc,
        sorted_mapped_words,
        {},
    )

    return reduced_words


def visualize_top_words(word_counts, top_n=20):
    top_words = Counter(word_counts).most_common(top_n)
    words, counts = zip(*top_words)  # Розпаковуємо для графіка
    plt.figure(figsize=(10, 8))
    plt.bar(words, counts)
    plt.xlabel("Слова")
    plt.ylabel("Частота використання")
    plt.title("Топ-слова за частотою використання")
    plt.xticks(rotation=45)
    plt.show()


def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Перевіряємо на помилки
        return response.text
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")


def main(url):
    text = fetch_content(url)
    word_counts = map_reduce(text)
    visualize_top_words(word_counts)


if __name__ == "__main__":
    url = "https://www.gutenberg.org/files/11/11-0.txt"  # Alice in Wonderland by Lewis Carroll
    main(url)
