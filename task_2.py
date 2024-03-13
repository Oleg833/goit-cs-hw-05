import requests
from collections import Counter
import re
import matplotlib.pyplot as plt
from functools import reduce
from collections import defaultdict


# Виконання MapReduce в одній функції
# def map_reduce(text):
#     # Крок Map: розбиття тексту на слова та створення пар (слово, 1)
#     words = text.split()
#     mapped_values = [(word, 1) for word in words]

#     # Крок Shuffle: групування значень за ключами
#     shuffled = defaultdict(list)
#     for key, value in mapped_values:
#         shuffled[key].append(value)

#     # Крок Reduce: обрахунок суми значень для кожного ключа
#     reduced = {key: sum(values) for key, values in shuffled.items()}

#     return reduced


def map_reduce(text):
    words = text.split()
    # Крок Map:  створення пар (слово, 1)
    mapped_words = map(lambda word: (word, 1), words)
    sorted_words = sorted(mapped_words)
    # reduced_words = reduce(
    #     lambda acc, val: acc.update({val[0]: acc.get(val[0], 0) + 1}) or acc,
    #     sorted_words,
    #     {},
    # )
    reduced_words = {}
    for val in sorted_words:
        if val[0] in reduced_words:
            reduced_words[val[0]] += 1
        else:
            reduced_words[val[0]] = 1
    # Вивести перші 10 елементів словника
    i = 0
    for word in reduced_words:
        i += 1
        if i < 10:
            print(word, reduced_words[word])
        else:
            break

    return reduced_words


def visualize_top_words(word_counts, top_n=20):
    top_words = dict(Counter(word_counts).most_common(top_n))
    plt.bar(top_words.keys(), top_words.values())
    plt.xlabel("Слова")
    plt.ylabel("Частота")
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
