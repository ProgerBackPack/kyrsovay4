def filter_vacancies(list_classes: list[object, ...], word: str | None) -> list[object, ...] | None:
    """
    Функция фильтрует список объектов по полученному слову,
    разделяет слово по "," тем самым будет два слова

    если все слова из списка есть в объекте,
    добавляет объект в отфильтрованный список
    и возвращает отфильтрованный список объектов

    если параметр (word) не указан возвращает
    первоначальный список объектов (list_classes)

    если по заданным параметрам нечего не будет найдено
    вернет сообщение об ошибке поиска
    """
    try:
        if word:
            try:
                if "," not in word:
                    raise ValueError(f"\nНекорректный ввод, вы забыли указать запятую - ',' !")

                if len(word.replace(" ", "").split(",")) > 2:
                    raise ValueError(f"\nВы ввели больше двух аргументов - "
                                     f"{word.replace(" ", "").split(",")}")

            except ValueError as a:
                print(a)

            else:
                list_filtered_classes = []
                name, city = word.lower().replace(" ", "").split(",")
                if name != "" and city != "":
                    for el in list_classes:
                        if name in el.name.lower() \
                                and city == el.city.lower():
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо заданным ключевым словам ({name}, {city.capitalize()}) "
                                        f"не найдено ни одного совпадения")

                    return list_filtered_classes

                elif name != "" and city == "":
                    for el in list_classes:
                        if name in el.name.lower():
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо заданному ключевому слову ({name}) "
                                        f"не найдено ни одного совпадения")

                    return list_filtered_classes

                elif city != "" and name == "":
                    for el in list_classes:
                        if city == el.city.lower():
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо заданному ключевому слову ({city.capitalize()}) "
                                        f"не найдено ни одного совпадения")

                    return list_filtered_classes

        else:
            return list_classes

    except NameError as a:
        print(a)


def get_vacancies_by_salary(list_classes: list[object, ...], salary_range: str) \
        -> list[object, ...] | str:
    """
    Функция сортирует список объектов по указанному диапазону зарплат,
    в случае если указанный диапазон не найден, возвращается сообщение пользователю
    о том что нужно указать другой диапазон

    :param list_classes:  список объектов
    :param salary_range: строковое отображение диапазона зарплат
    :return: список отфильтрованных объектов по переданной зарплате
    """
    try:
        list_filtered_classes = []
        if salary_range:
            try:
                salary_from, salary_to, currency = salary_range.lower().split("-")
            except ValueError:
                print(f"\nВы ввели больше двух аргументов - {salary_range.lower().split("-")}")

            else:
                if salary_from != "" and salary_to != "" and currency != "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from) and el.salary_to <= int(
                                salary_to) and el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from}, до - {salary_to}, валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from != "" and salary_to != "" and currency == "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from) and el.salary_to <= int(salary_to):
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from}, до - {salary_to} )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from != "" and salary_to == "" and currency == "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from):
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from} )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from == "" and salary_to != "" and currency != "":
                    for el in list_classes:
                        if el.salary_to <= int(salary_to) and el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( до - {salary_to}, валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from == "" and salary_to == "" and currency != "":
                    for el in list_classes:
                        if el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону валюты \n"
                                        f"( валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from == "" and salary_to != "" and currency == "":
                    for el in list_classes:
                        if el.salary_to <= int(salary_to):
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( до - {salary_to} )\n"
                                        f"не найдено ни одного совпадения ...")

                if salary_from != "" and salary_to == "" and currency != "":
                    for el in list_classes:
                        if el.salary_from >= int(salary_from) and el.salary_to <= int(
                                salary_to) and el.currency == currency:
                            list_filtered_classes.append(el)

                    if len(list_filtered_classes) < 1:
                        raise NameError(f"\nПо данному диапазону зарплат \n"
                                        f"( от - {salary_from}, валюта - {currency}. )\n"
                                        f"не найдено ни одного совпадения ...")

        else:
            return list_classes

    except NameError as a:
        print(a)
    else:
        return list_filtered_classes


def sort_vacancies(list_classes: list[object, ...] | object | None) -> list[object, ...] | object:
    """
    Функция сортирует список объектов по зарплате
    от большего к меньшему

    :param list_classes: список объектов или объект
    :return: список отсортированных объектов или объект
    """
    try:
        sorted_list = sorted(list_classes, reverse=True)
        return sorted_list
    except TypeError:
        pass


def get_top_vacancies(list_classes: list[object, ...] | object | None, top_n: str) -> list[object, ...] | object:
    """
    Функция возвращает только то количество элементов
    которое укажет пользователь в параметре (top_n)

    если параметр (top_n) не указан
    функция вернет изначальный список (list_classes)

    если переданный параметр (top_n) больше
    чем количество элементов в списке
    пользователю вернется список всех элементов
    и сообщение о том что в списке нет указанного количества элементов

    :param list_classes: список объектов
    :param top_n: количество объектов которые нужно вернуть
    :return: список объектов
    """
    try:
        if top_n:
            if int(top_n) == 0:
                raise IndexError(f"\n\nВы передали некорректное значение - {top_n}\n"
                                 f"Ошибка: невозможно вернуть {top_n} вакансий")

            else:
                try:
                    if int(top_n) > len(list_classes):
                        if len(list_classes) != 11 and len(list_classes) % 10 == 1:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансию")
                        elif 2 <= len(list_classes) <= 4:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "
                                             f"вакансии")
                        else:
                            raise IndexError(f"\n\nПо указанным параметрам мы нашли только {len(list_classes)} "

                                             f"вакансий")
                except IndexError as a:
                    print(a)

                finally:
                    return list_classes[:int(top_n)]

        else:
            return list_classes

    except TypeError:
        pass
    except IndexError as a:
        print(a)


def print_vacancies(list_classes: list[object, ...] | object | None) -> None:
    """
    Функция печатает список объектов
    """
    try:
        for elem in list_classes:
            print(elem)
    except TypeError:
        pass