from stats import count_words, count_chars, sorted_char_list
import sys

def get_boot_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def print_word_count(text):
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

def print_char_count(text):
    print("--------- Character Count -------")
    chars = count_chars(text)
    sorted_chars = sorted_char_list(chars)
    for item in sorted_chars:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():
            print(f"{ch}: {num}")

def report(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    text = get_boot_text("./" + filepath)

    print_word_count(text)
    print_char_count(text)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    report(sys.argv[1])

main()