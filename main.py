import sys

from stats import count_book_characters, count_book_words, sorted_letters


def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf-8") as f:
        read_data = f.read()
        return read_data


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    book_characters = count_book_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(count_book_words(book_text))
    print("--------- Character Count -------")
    for item in sorted_letters(book_characters):
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
