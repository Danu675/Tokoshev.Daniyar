while True :
    word = input("Введите слово на латинице или на кирилице = ")
    print("Ваше слово = " ,word)
    if word == "exit":
        break
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"
    letter =len(word)
    vowels_cnt = len([letter for letter in word.lower()if letter in vowels])
    consonants_cnt = letter - vowels_cnt
    vowels_procent = round(vowels_cnt/letter * 100,2)
    consonants_procent = round(consonants_cnt/letter * 100,2)
    print(f"Общее количество букв = {letter}")
    print(f"Количество гласных букв = {vowels_cnt}")
    print(f"Количество согласных букв = {consonants_cnt}")
    print(f"Гласные/Согласные = {vowels_procent}%/{consonants_procent}%")