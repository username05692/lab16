import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from collections import Counter

# Завантаження тексту з перевіркою
try:
    text = gutenberg.words('carroll-alice.txt')
except LookupError:
    print("Не вдалося завантажити текст. Перевірте назву файлу або підключення до інтернету.")
    exit()

# Підрахунок загальної кількості слів
total_words = len(text)
print(f"Загальна кількість слів у тексті: {total_words}")

# Підрахунок частоти слів без обробки
freq_dist = Counter(text)
print("\n10 найбільш вживаних слів (без обробки):")
for word, count in freq_dist.most_common(10):
    print(f"{word}: {count}")

# Функція для побудови стовпчастої діаграми
def plot_bar_chart(words, counts, title):
    plt.figure(figsize=(10, 5))
    plt.bar(words, counts)
    plt.title(title, fontsize=14)
    plt.xlabel("Слова", fontsize=12)
    plt.ylabel("Частота", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Побудова стовпчастої діаграми без обробки
words, counts = zip(*freq_dist.most_common(10))
plot_bar_chart(words, counts, "10 найбільш вживаних слів (без обробки)")

# Обробка тексту: видалення стоп-слів та пунктуації
stop_words = set(stopwords.words('english'))
words_filtered = [word.lower() for word in text if word.isalnum() and word.lower() not in stop_words]

# Підрахунок частоти слів після обробки
freq_dist_filtered = Counter(words_filtered)
print("\n10 найбільш вживаних слів (після обробки):")
for word, count in freq_dist_filtered.most_common(10):
    print(f"{word}: {count}")

# Побудова стовпчастої діаграми після обробки
words, counts = zip(*freq_dist_filtered.most_common(10))
plot_bar_chart(words, counts, "10 найбільш вживаних слів (після обробки)")
