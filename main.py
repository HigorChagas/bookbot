import sys
from stats import (
    get_num_words,
    count_characters,
    chars_dict_to_sorted_list,
    sort_on
)

def get_book_text():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    with open(book_path, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents

def main():
    text = get_book_text()
    num_of_words = get_num_words(text)
    char_count = count_characters(text)
    char_list = chars_dict_to_sorted_list(char_count)
    char_list_sorted = sorted(char_list, key=sort_on, reverse=True)
    someVariable = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(num_of_words)
    print("--------- Character Count -------")

    for values in char_list_sorted:
        print(f"{values['char']}: {values["count"]}")

    print("============= END ===============")


main()