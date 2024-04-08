def main():
        bookpath = "books/frankenstein.txt"
        text = open_book("books/frankenstein.txt")
        num_words = get_num_words(text)
        print(f"{num_words} words were found in the document.")
        get_letter_count(text)
    

def open_book(path):
        with open("books/frankenstein.txt") as f:
            return f.read()

def get_num_words(text):
        words = text.split()
        return len(words)

def get_letter_count(text):
        lowered_text = text.lower()
        letter_list = []
        return print(words)

       

main()