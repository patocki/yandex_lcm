last_letter = ""


def city(town):
    global last_letter
    if last_letter == "":
        last_letter = town[-1].lower()
        return True
    else:
        if last_letter == town[0].lower():
            last_letter = town[-1].lower()
            return True
        else:
            last_letter = town[-1].lower()
            return False
