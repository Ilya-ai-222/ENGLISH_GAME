import sounddevice as sd
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator
import time
import random
duration = 5  # секунды записи
sample_rate = 44100
print("Запуск 🕹️ игры...")
time.sleep(2)

easy_words = [
    "дом", "солнце", "вода", "хлеб", "книга", "друг", "мама", "папа",
    "кошка", "собака", "школа", "урок", "игра", "песня", "цветок",
    "дерево", "река", "гора", "город", "улица", "окно", "дверь", "стол",
    "стул", "чашка", "ложка", "яблоко", "молоко", "сахар", "чай",
    "облако", "звезда", "луна", "снег", "дождь", "ветер", "огонь",
    "птица", "рыба", "машина"
]

normal_words = [
    "путешествие", "библиотека", "концерт", "выставка", "праздник",
    "традиция", "привычка", "настроение", "разговор", "история",
    "наука", "техника", "компьютер", "телефон", "камера", "карта",
    "билет", "отель", "ресторан", "меню", "рецепт", "одежда", "обувь",
    "сумка", "зонт", "ключ", "адрес", "почта", "письмо", "журнал",
    "кино", "театр", "музей", "парк", "рынок", "магазин", "фабрика",
    "офис", "план", "цель"
]

hard_words = [
    "исследование", "эксперимент", "гипотеза", "теория", "анализ",
    "структура", "система", "процесс", "результат", "эффективность",
    "стратегия", "ресурс", "бюджет", "проект", "команда", "лидерство",
    "инновация", "технология", "платформа", "интерфейс", "алгоритм",
    "база данных", "маршрут", "координата", "диаграмма", "график",
    "показатель", "тенденция", "сегмент", "адаптация",
    "оптимизация", "валидация", "интеграция", "архитектура", "прототип",
    "симуляция", "классификация", "кластеризация", "параметр", "метрика"
]

words = easy_words + normal_words + hard_words
print("Добро пожаловать в тренажер произношения английских слов! Выбери уровень сложности: легкий, средний, сложный, любительский, или введи 'инструкция', чтобы узнать о программе больше.")
balls = 0
while True:
    difficulty = input("⚙️Уровень сложности:")
    if difficulty == "легкий" or difficulty == "Легкий":
        print("Включаем легкий уровень сложности...")
        for i in range(5):
            time.sleep(1)
            i = len(easy_words)
            word = random.randint(0, i)  
            print(easy_words[word])
            time.sleep(1)
            print("📼Запись начнется через..")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Говори...")
            recording = sd.rec(
            int(duration * sample_rate), 
            samplerate=sample_rate,      
            channels=1,                 
            dtype="int16")              
            sd.wait() 
            wav.write("output.wav", sample_rate, recording)
            print("📼Запись завершена, теперь распознаём...")

            recognizer = sr.Recognizer()
            with sr.AudioFile("output.wav") as source:
                audio = recognizer.record(source)
            
            text = recognizer.recognize_google(audio, language="en-US")
            translator = Translator()
            translated_text = translator.translate(text, dest='ru').text
            text_2 = easy_words[word]
            translator_2 = Translator()
            translated_text_2 = translator_2.translate(text_2, dest='en').text
            if translated_text == easy_words[word]:
                print(f"✅Правильно! Это слово переводится на английский как '{translated_text_2}', +1 балл")
                balls += 1
                time.sleep(1)
            else:
                print(f"❌Неправильно! Это слово переводится на английский язык как '{translated_text_2}'")
                time.sleep(1)
        print(f"Вы набрали {balls} из 5 баллов")
        balls = 0

    elif difficulty == "сложный" or difficulty == "Сложный":
        print("Включаем сложный уровень сложности...")
        for i in range(5):
            time.sleep(1)
            i = len(hard_words)
            word = random.randint(0, i)  
            print(hard_words[word])
            time.sleep(1)
            print("📼Запись начнется через..")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Говори...")
            recording = sd.rec(
            int(duration * sample_rate), 
            samplerate=sample_rate,      
            channels=1,                 
            dtype="int16")              
            sd.wait() 
            wav.write("output.wav", sample_rate, recording)
            print("📼Запись завершена, теперь распознаём...")

            recognizer = sr.Recognizer()
            with sr.AudioFile("output.wav") as source:
                audio = recognizer.record(source)
            
            text = recognizer.recognize_google(audio, language="en-US")
            translator = Translator()
            translated_text = translator.translate(text, dest='ru').text
            text_2 = hard_words[word]
            translator_2 = Translator()
            translated_text_2 = translator_2.translate(text_2, dest='en').text
            if translated_text == hard_words[word]:
                print(f"✅Правильно! Это слово переводится на английский как '{translated_text_2}', +1 балл")
                balls += 1
                time.sleep(1)
            else:
                print(f"❌Неправильно! Это слово переводится на английский язык как '{translated_text_2}'")
                time.sleep(1)
        print(f"Вы набрали {balls} из 5 баллов")
        balls = 0
        
    elif difficulty == "средний" or difficulty == "Средний":
        print("Включаем средний уровень сложности...")
        for i in range(5):
            time.sleep(1)
            i = len(normal_words)
            word = random.randint(0, i)  
            print(normal_words[word])
            time.sleep(1)
            print("📼Запись начнется через..")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Говори...")
            recording = sd.rec(
            int(duration * sample_rate), 
            samplerate=sample_rate,      
            channels=1,                 
            dtype="int16")              
            sd.wait() 
            wav.write("output.wav", sample_rate, recording)
            print("📼Запись завершена, теперь распознаём...")

            recognizer = sr.Recognizer()
            with sr.AudioFile("output.wav") as source:
                audio = recognizer.record(source)
            
            text = recognizer.recognize_google(audio, language="en-US")
            translator = Translator()
            translated_text = translator.translate(text, dest='ru').text
            text_2 = normal_words[word]
            translator_2 = Translator()
            translated_text_2 = translator_2.translate(text_2, dest='en').text
            if translated_text == normal_words[word]:
                print(f"✅Правильно! Это слово переводится на английский как '{translated_text_2}', +1 балл")
                balls += 1
                time.sleep(1)
            else:
                print(f"❌Неправильно! Это слово переводится на английский язык как '{translated_text_2}'")
                time.sleep(1)
        print(f"Вы набрали {balls} из 5 баллов")
        balls = 0

    elif difficulty == "любительский" or difficulty == "Любительский":
        print("Включаем любительский уровень сложности...")
        for i in range(5):
            time.sleep(1)
            i = len(words)
            word = random.randint(0, i)  
            print(words[word])
            time.sleep(1)
            print("📼Запись начнется через..")
            print("3")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("1")
            time.sleep(1)
            print("Говори...")
            recording = sd.rec(
            int(duration * sample_rate), 
            samplerate=sample_rate,      
            channels=1,                 
            dtype="int16")              
            sd.wait() 
            wav.write("output.wav", sample_rate, recording)
            print("📼Запись завершена, теперь распознаём...")

            recognizer = sr.Recognizer()
            with sr.AudioFile("output.wav") as source:
                audio = recognizer.record(source)
            
            text = recognizer.recognize_google(audio, language="en-US")
            translator = Translator()
            translated_text = translator.translate(text, dest='ru').text
            text_2 = words[word]
            translator_2 = Translator()
            translated_text_2 = translator_2.translate(text_2, dest='en').text
            if translated_text == words[word]:
                print(f"✅Правильно! Это слово переводится на английский как '{translated_text_2}', +1 балл")
                balls += 1
                time.sleep(1)
            else:
                print(f"❌Неправильно! Это слово переводится на английский язык как '{translated_text_2}'")
                time.sleep(1)
        print(f"Вы набрали {balls} из 5 баллов")
        balls = 0

    elif difficulty == "инструкция" or difficulty == "Инструкция" or difficulty == "'инструкция'" or difficulty == "'Инструкция'":
        print("Инструкция:" \
        "Что это такое? Это приложение, которое проверяет ваше произношение путем перевода слов." \
        "Как этим пользоваться? Запустите приложние и выберите уровень сложности:" \
        "😊Легкий - уровень для новичков. Самые базовые слова." \
        "😐Средний - тем, кто любит посложнее. Слова сложнее, подходит людям с опытом." \
        "☹️Сложный - этот уровень не жалеет никого. Слова, перевод которых заставит вас вспомнить весь школьный материал!" \
        "🤯Любительский - тем, кому нечем заняться. Вам может выпасть как простое слово, так и что-то из разряда невозможного." \
        "После выбора сложности у вас будет несколько секунд, чтобы перевести слово и 5 сек. чтобы озвучить. Приложение постарается определить правильность перевода и произношения и выдаст вам результат.  ")
    else:
        print("Error:name")
    



