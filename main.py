def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    chars = count_characters(text)
    report_print(word_count, chars, book_path)
    

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(file):
    word_list = file.split()
    word_count = len(word_list)
    return word_count

def count_characters(file):
    character_hash = {}
        
    for letter in file:
        letter = letter.lower()
        if letter in character_hash:
            character_hash[letter] += 1
        else:
            character_hash[letter] = 1
    return character_hash  

def report_print(word_count, character_hash, book_path):
    sorted_character_hash = dict(sorted(character_hash.items(), key = lambda item: item[1], reverse=True))
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for char in sorted_character_hash:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_character_hash[char]} times")
    print("--- End report ---")

main()
        