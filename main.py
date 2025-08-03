from stats import get_num_words
from stats import counting_characher

def get_book_text(parameter_name):
    with open(parameter_name) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(book_text)
    char_count = counting_characher(book_text)
    print(f"{char_count}")

main()