'''
Created on Sep 24, 2013

@author: hunters
'''
import os, itertools

VOWELS = "aoeiu"

def init_dictionary():
    words = set()
    if os.path.isfile('/usr/share/dict/words'):
        with open('/usr/share/dict/words', 'r') as f:
            for line in iter(f):
                words.add(line.strip('\n'))
    else:
        print("Was unable to open the dictionary file")
        exit()
    return words

def spell_check(word, dictionary):
    undupl = eliminate_duplicate(word)
    for elem in undupl:
        if elem in dictionary or isinstance(permutate_vowels(elem, dictionary, complete = False), str):
            return True
    return False

def permutate_vowels(word, dictionary, complete = True):
    rtn = []
    vowel_locations = [index for index in range(len(word)) if word[index] in VOWELS]
    vowel_permutations = itertools.product(VOWELS, repeat = len(vowel_locations))
    for permutation in vowel_permutations:
        tmp = ""
        vowel_index = 0
        for index in range(len(word)):
            if word[index] in VOWELS:
                tmp += permutation[vowel_index]
                vowel_index += 1
            else:
                tmp += word[index]
        if not complete and tmp in dictionary:
            return tmp
        rtn.append(tmp)
    return rtn

def eliminate_duplicate(word):
    rtn = []
    enumerated_word = [[k, 2] if len(list(v)) >= 2 else [k, 1] for k,v in itertools.groupby(word)]
    duplicate_count = len([elem for elem in enumerated_word if elem[1] == 2])
    permutations = itertools.product("12", repeat = duplicate_count)
    for elem in permutations:
        tmp = ""
        duplicate_index = 0
        for char in enumerated_word:
            if char[1] == 2:
                tmp += char[0] * int(elem[duplicate_index])
                duplicate_index += 1
            else:
                tmp += char[0]
        rtn.append(tmp)
    return rtn

def duplicate_word(word):
    rtn = []
    permutations = itertools.product("12", repeat = len(word))
    for elem in permutations:
        rtn.append("".join([word[index] * int(elem[index]) for index in range(len(word))]))
    return rtn
    
def main():
    dictionary = init_dictionary()
    while True:
        word = input("> ")
        if "--verify" in word:
            success = True
            word = word.split("--verify")[0].strip().lower()
            if word not in dictionary:
                print("word to verify must already exist in dictionary")
                continue
            tmp = permutate_vowels(word, dictionary)
            possible_words = itertools.chain(*list(map(duplicate_word, tmp)))
            for misspelling in possible_words:
                print(misspelling)
                if not spell_check(misspelling, dictionary):
                    print(("\nThe following mis-spelling: \"" + misspelling + "\" was not found in the dictionary"))
                    success = False
                    break
            if success:
                print("\n\nSuccess!")

        elif "--exit" in word:
            print("See you next time!")
            break

        else:
            word = word.strip().lower()
            if word == "":
                print("Please enter a word")
            else:
                found = False
                unduplicated = eliminate_duplicate(word)
                for elem in unduplicated:
                    if elem in dictionary:
                        print(elem)
                        found = True
                        break
                if not found:
                    for elem in unduplicated:
                        rst = permutate_vowels(elem, dictionary, complete = False)
                        if isinstance(rst, str):
                            print(rst)
                            found = True
                            break
                if not found:
                    print("NO SUGGESTIONS")

if __name__ == '__main__':
    main()