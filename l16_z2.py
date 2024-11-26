import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string

# Завантаження ресурсів
print("\nЗавантаження необхідних ресурсів NLTK...\n")
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Підготовка стоп-слів
stop_words = set(stopwords.words('english'))

def process_text(text):
    print("\n=== Початок обробки тексту ===\n")
   
    # Токенізація
    tokens = word_tokenize(text)
    print(f"Токени після токенізації (перші 10):\n{tokens[:10]}\n")

    # Видалення пунктуації
    tokens = [word for word in tokens if word not in string.punctuation]
    print(f"Токени після видалення пунктуації (перші 10):\n{tokens[:10]}\n")

    # Видалення стоп-слів
    tokens = [word for word in tokens if word.lower() not in stop_words]
    print(f"Токени після видалення стоп-слів (перші 10):\n{tokens[:10]}\n")

    # Лемматизація
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    print(f"Токени після лемматизації (перші 10):\n{tokens[:10]}\n")

    print("=== Завершення обробки тексту ===\n")
    return tokens

# Зчитування тексту 
file_path = r"C:\Users\Admin\OneDrive\НАВЧАННЯ\ПАЙТОН\input.txt"  
try:
    print(f"Спроба зчитати текст із файлу: {file_path}\n")
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    if not text.strip():  # Перевіряємо, чи текст порожній або складається тільки з пробілів
        print(f"Помилка: Файл {file_path} порожній. Обробка завершена.\n")
        exit()
    print(f"Чи зчитаний текст порожній? {'Так' if not text else 'Ні'}\n")
    print(f"Оригінальний текст з файлу:\n{text}\n")
except FileNotFoundError:
    print(f"Помилка: Файл за шляхом {file_path} не знайдено. Перевірте, чи існує файл.\n")
    exit()

# Обробка тексту
processed_text = process_text(text)

# Запис у файл
output_path = r'C:\Users\Admin\OneDrive\НАВЧАННЯ\ПАЙТОН\output.txt'  
if processed_text:
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(' '.join(processed_text))
    print(f"Текст успішно оброблено та збережено у файл: {output_path}\n")
else:
    print("Після обробки текст виявився порожнім. Запис не виконано.\n")
