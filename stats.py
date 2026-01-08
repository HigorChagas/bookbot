def count_book_words(text):
    book_words = text.split()
    num_words = len(book_words)

    return f"Found {num_words} total words"


def count_book_characters(text):
    letter_dict = {}
    book_text_lower = text.lower()

    for letter in book_text_lower:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    return letter_dict


def sorted_letters(input_dict):
    report_list = []

    for char in input_dict:
        item = {"char": char, "num": input_dict[char]}
        report_list.append(item)

    def get_num(item):
        return item["num"]

    report_list.sort(key=get_num, reverse=True)

    return report_list


def sort_on(items):
    return items["num"]
