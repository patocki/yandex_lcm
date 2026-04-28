numP = int(input())
name_bb = ""
pages_bb = 0

book_is_found = False
for i in range(numP):
    max_book = 0
    numB = int(input())
    for j in range(numB):
        name = input()
        pages = int(input())
        if pages <= len(name):
            print(f"У {j + 1}-й книги на {i + 1}-й полке слишком длинное название!")
            book_is_found = True
            break
        if pages > pages_bb:
            pages_bb = pages
            name_bb = name
            max_book = j

    if book_is_found:
        break
    print(f"На {i + 1}-й полке это {max_book + 1}-я книга.")
