def get_num_words(book_words):
    return len(book_words.split())

def counting_characher(text):
    book_text = {}
    for char in text.lower():
        if char in book_text:
            book_text[char] += 1
        else:
            book_text[char] = 1
    return book_text
   