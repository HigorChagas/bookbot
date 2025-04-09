def get_num_words(text):
    words = text.split()
    num_words = len(words)

    return f"Found {num_words} total words"

def count_characters(text):
    words_lowercased = text.lower()
    letters_count = {}

    for letters in words_lowercased:
        if letters in letters_count:
            letters_count[letters] += 1
        else:
            letters_count[letters] = 1
            
    return letters_count


def chars_dict_to_sorted_list(char_dict):
    chars_list = []

    for char, count in char_dict.items():
        if char.isalpha():
            chars_list.append({"char": char, "count": count})

    return chars_list

def sort_on(dict):
    return dict["count"]