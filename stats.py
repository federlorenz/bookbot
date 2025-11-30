def get_num_words(book):
    return len(book.split())

def count_characters(book):
    book = book.lower()
    characters = {}
    for char in book:
        if char in characters.keys():
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(items):
    return items["num"]

def sorted_characters(characters):
    sorted_list = [{"char":key,"num":value} for key,value in characters.items() if key.isalpha()]
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list
