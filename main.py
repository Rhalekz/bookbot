def main():
        bookpath = "books/frankenstein.txt"
        text = open_book(bookpath)
        num_words = get_num_words(text)
        character_count = get_character_count(text)
        print(f"--- Begin report of {bookpath} ---")
        print(f"{num_words} words were found in the document.")
        print()
        for letter in character_count:
                character = letter["character"]
                number = letter["num"]
                if character.isalpha():
                        print(f"The '{character}' character was found {number} times")
        print("--- End report ---")
    

def open_book(path):
        with open(path) as f:
            return f.read()

def get_num_words(text):
        words = text.split()
        return len(words)

def get_character_count(text):
        lowered_text = text.lower()
        letter_count = {}
        for letter in lowered_text:
                if letter in letter_count:
                        letter_count[letter] += 1
                        
                else: 
                        letter_count[letter] = 1

        list = []
        for letter in letter_count:
                num = letter_count[letter]
                list.append({"character": letter, "num": num})

        list.sort(reverse=True, key=sort_on)
        return list

def sort_on(dict):
        return dict["num"]

main()