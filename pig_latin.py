import re

VOWELS = ['a', 'e', 'i', 'o', 'u']
TAIL = 'way'
TAIL1 = 'ay'


def convert_pig_latin(file_name):
    new_list = []  # List of converted words to Pig Latin
    with open(file_name, 'r') as file_obj:
        for line in file_obj.readlines():
            for word in line.split():
                # Get index of the first vowel in each word
                first_vowel_idx = re.search("[aeiou]", word, re.IGNORECASE)
                # if word begins with vowel
                if first_vowel_idx.start() == 0:
                    new_list.append(word + TAIL)
                else:
                    new_list.append(word[1:] + word[0] + TAIL1)
        return " ".join(new_list)


if __name__ == '__main__':
    file_name = 'myfile.txt'
    print(convert_pig_latin(file_name))
