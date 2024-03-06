def main():
    book_path = "books/frankenstein.txt"
    file_contents = read_text(book_path)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()

    letters_dict = count_letters(file_contents)
    for entry in dict_to_sorted_list(letters_dict):
        if entry["item"].isalpha():
            letter = entry["item"]
            count = entry["count"]
            print(f"The '{letter}' character was found {count} times")

    print("--- End report ---")

def read_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    dict = {}
    text = text.lower()
    for ch in text:
        if ch in dict:
            dict[ch] += 1
        else:
            dict[ch] = 1
    return dict

def sort_on_count(dict):
    return dict["count"]

def dict_to_sorted_list(dict):
    ret = []
    for key in dict:
        ret.append({"item": key, "count": dict[key]})
    ret.sort(reverse=True, key=sort_on_count)
    return ret

main()