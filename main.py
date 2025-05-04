import time

meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "ИЗИ": "Легко",
            "ЛП": "Лучшая подруга",
            "РОФЛ": "Смешной прикол",
            }

while True:
    time.sleep(1)
    word = input("Введите непонятное слово (большими буквами!): ")
    load = "Загрузка."
    found = "Найдено!"

    if word in meme_dict.keys():
        # Что делать, если слово нашлось?
        time.sleep(1)
        print(load)
        load = "Загрузка.."
        time.sleep(1)
        print(load)
        load = "Загрузка..."
        time.sleep(1)
        print(load)
        time.sleep(1)
        print(found)
        print(word, "-", meme_dict[word])    
    else:
        # Что делать, если слово не нашлось?
        time.sleep(1)
        print("Слово не нашлось")
