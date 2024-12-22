def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        print(f"this book has {word_count} words")
        
        char_count = count_char(file_contents)

        char_list = [{"char": char, "num": count} for char, count in char_count.items() if char.isalpha()]
        char_list.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
    
        for item in char_list:
            print(f"The '{item['char']}' character was found {item['num']} times")
        
        print("--- End report ---")

def count_words(text):
    words = text.split()
    count = len(words)
    return count

def count_char(text):
    char_count = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(char):
    return char["num"]

main()