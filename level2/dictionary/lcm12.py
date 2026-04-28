count_elem = {}
num = int(input())

for _ in range(num):
    formule = input()
    element = ""
    count = ""

    for ch in formule:
        if ch.isupper():  # Новая заглавная буква
            if element:  # Сохраняем предыдущий элемент
                count_elem[element] = count_elem.get(element, 0) + (
                    int(count) if count else 1
                )
            element = ch  # Начинаем новый элемент
            count = ""
        elif ch.islower():  # Строчная - продолжаем элемент
            element += ch
        elif ch.isdigit():  # Цифра - добавляем к счетчику
            count += ch

    # Не забываем последний элемент
    if element:
        count_elem[element] = count_elem.get(element, 0) + (int(count) if count else 1)

for k, v in sorted(count_elem.items()):
    print(f"{k}\t->\t{v}")
