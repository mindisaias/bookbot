import sys
from stats import count_words, count_chars, sort_dict
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    file_path = sys.argv[1]
    #file_contents = get_book_text(file_path)
    num_words = count_words(file_path)
    print(f"Found {num_words} total words")
    num_chars = count_chars(file_path)
    sorted_dict = sort_dict(num_chars)
    for entry in sorted_dict:
        if entry["char"].isalpha():
          print(f"{entry["char"]}: {entry["count"]}")
def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

main()
