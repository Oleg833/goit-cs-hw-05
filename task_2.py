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
    top_words = dict(Counter(word_counts).most_common(top_n))
    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel("Слова")
    plt.ylabel("Частота використання")
    plt.title("Топ-слова за частотою використання")
    plt.xticks(rotation=45)
    plt.show()


def fetch_text(url):
    response = requests.get(url)
    return response.text


def main(url):
    text = fetch_text(url)
    word_counts = map_reduce(text)
    visualize_top_words(word_counts)


if __name__ == "__main__":
    url = "https://www.gutenberg.org/files/11/11-0.txt"  # Alice in Wonderland by Lewis Carroll
    main(url)
