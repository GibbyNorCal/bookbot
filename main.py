def main():
    book_path = "books/frankenstein.txt"
    text = book_contents(book_path)
    num_words = book_length(text)
    print(f"This book has", num_words, "words")

def book_length(file_contents):
    words = file_contents.split()
    return len(words)

def book_contents(path):
    with open(path) as f:
        return f.read()








main()
