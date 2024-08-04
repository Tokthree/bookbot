def sort_on(dict):
    return dict["num"]

def count_characters_unique(text):
    characters_unique = dict()
    characters_list = []

    for character in text:
        if character not in characters_unique:
            characters_unique.update({character:0})
        characters_unique[character] += 1

    for key in characters_unique:
        characters_list.append({"character":key, "num":characters_unique[key]})

    characters_list.sort(reverse=True, key=sort_on)
    return(characters_list)

def count_words(text):
    return(len(text.split()))

def print_report(words, characters_list):
    print(f"--- Begin report of books/frankenstein/txt ---\n{words} words found in the document\n")
    for index in characters_list:
        if index["character"].isalpha():
            print(f"the '{index['character']}' character was found {index['num']} times")
    print("--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print_report(count_words(file_contents), count_characters_unique(file_contents.lower()))

main()