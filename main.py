from stats import get_num_words, count_characters, sorted_characters
import sys
def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
        return file_contents
def check_arguments():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
def main():
    check_arguments()
    book = get_book_text(sys.argv[1])
    words = get_num_words(book)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    characters = count_characters(book)
    for char in sorted_characters(characters):
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()

    
