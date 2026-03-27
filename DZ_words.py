from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator  # ✅ Библиотека для перевода


def get_inglish_words():

    url = "http://randomword.com/"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        english_words = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_words": english_words,
            "word_definition": word_definition
        }
    except:
        print("Вы ошиблись.")
        return None


def word_game():

    print("🎮 Добро пожаловать в игру!")

    while True:
        word_dikt = get_inglish_words()


        if not word_dikt:
            continue

        word = word_dikt.get("english_words")  # слово на английском
        word_definition = word_dikt.get("word_definition")  # определение на английском

        translated_definition = GoogleTranslator(source='en', target='ru').translate(word_definition)

        translated_word = GoogleTranslator(source='en', target='ru').translate(word)

        print(f"💡 Значение слова - {translated_definition}")

        user = input("❓ Что это за слово? (пиши на русском) ").strip().lower()

        if user == translated_word.lower():
            print("Верно!")
        else:
            print(f"Вы ошиблись. Было загадано это слово - {translated_word} ({word})")

        play_again = input("Хотите сыграть еще раз? д/н: ").strip().lower()
        if play_again != "д":
            print("👋 Спасибо за игру!")
            break


# 🚀 Запуск игры
word_game()