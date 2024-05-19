with open("books/frankenstein.txt") as f:
    file_contents = f.read()


def sort_on(dict):
    return dict["num"]


def number_of_words(content):
    words = content.split()
    return len(words)


def count_letters(content):
    letter_count = {}

    for char in content:
        if char.isalpha():
            char = char.lower()
            if char not in letter_count:
                letter_count[char] = 1
            else:
                letter_count[char] += 1
    return letter_count


print("--- Begin report of books/frankenstein.txt ---")
print(f"{number_of_words(file_contents)} words found in the document\n")

letters = count_letters(file_contents)
letters_list = []


for letter in letters:
    letters_list.append({"letter": letter, "num": letters[letter]})

letters_list.sort(reverse=True, key=sort_on)

for dictionary in letters_list:
    print(f"The '{dictionary['letter']}' character was found \
{dictionary['num']} times")
print("--- End report ---")
