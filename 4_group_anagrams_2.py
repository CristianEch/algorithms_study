strs = ["kris", "car", "none", "risk", "kris", "cra", "no"]

# This excercise is so simple man: the idea is that each type of anagram has an unique DNA which is 
# shared only with the anagrams of the word. I can use this concept to group all the words with shared 
# DNA in a dictionary with the structure :
#
#           {DNA:[list of words with the same DNA]}
#
# I just need to modify or create a function who returns a DNA that can be used as key in a dic.


def get_dna(word):
    dna = [0] * 26
    for letter in word:
        index = ord(letter) - ord("a")
        dna[index] += 1
    return tuple(dna)

word_dic = {}
for word in strs:
    key = get_dna(word)
    if key not in word_dic:
        word_dic[key] = []
    word_dic[key].append(word)

print(list(word_dic.values()))
    









