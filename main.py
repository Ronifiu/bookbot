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


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print(file_contents)
    print(count_words(file_contents))
    print(count_characters(file_contents))