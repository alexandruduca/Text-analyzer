import re
import string
import sys


def get_words(file_name):
    f = open(file_name, 'r')
    word_list = []
    lines = f.readlines()
    for line in lines:
        for c in string.punctuation:
            line = line.replace(c, "")
        for word in line.split():
            word_list.append(word)
    return word_list


def sentences_count(file_name):
    f = open(file_name, 'r')
    lines = f.readlines()
    count = 0
    for line in lines:
        sentences_number = re.split(r'[.?!]', line)
        count += len(sentences_number) - 1
    return count


def CNP_count(word_list):
    CNP = []
    for word in word_list:
        if not word.isalpha():
            if len(word) == 13 and word not in CNP:
                CNP.append(word)
    return CNP


def phone_number_count(word_list):
    phone_number = []
    for word in word_list:
        if not word.isalpha():
            if len(word) == 10 and word.startswith("07") and word not in phone_number:
                phone_number.append(word)
    return phone_number


def words_frequency(word_list):
    alphabet = {}
    for word in word_list:
        if word.isalpha():
            for c in word:
                c = c.upper()
                alphabet[c] = alphabet[c] + 1 if c in alphabet.keys() else 1
    sorted_alphabet = dict(sorted(alphabet.items()))
    total = 0
    for letter in sorted_alphabet:
        total += sorted_alphabet[letter]
    for letter in sorted_alphabet:
        percentage = "(" + str("%.2f" % (sorted_alphabet[letter] / total * 100)) + "%)"
        print(" ", letter, "=", sorted_alphabet[letter], percentage)


def text_analyzer(file_name):
    words = get_words(file_name)
    print("Cuvinte:", len(words))

    sentences = sentences_count(file_name)
    print("Propozitii:", sentences)

    CNPs = CNP_count(words)
    print("CNP(uri):", len(CNPs), CNPs)

    phone_numbers = phone_number_count(words)
    print("Telefoane:", len(phone_numbers), phone_numbers)

    print("Litere:")
    words_frequency(words)


file = sys.argv[1]
text_analyzer(file)
