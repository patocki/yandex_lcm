cities_list = []


def cities(town: str):
    if not cities_list:
        cities_list.append(town)
        return ", ".join(cities_list)
    else:
        if town[0].lower() == cities_list[-1][-1].lower():
            cities_list.append(town)
            return ", ".join(cities_list)
        else:
            return "Miss!"
