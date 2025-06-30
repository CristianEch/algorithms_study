def get_dic(string):
    """fucntion who returns a dictionary with keys equal to the letters in the input string, and
    values equal to the quantity of each key"""
    dic = {}
    for letter in string:
        if letter not in dic:
            dic[letter]=1
        else:
            dic[letter]+=1
    return dic


lista = ["apt","man","qom","apt","lei","hus","pet","gay","six","mai"]
#lista = ["eat","tea","tan","ate","nat","bat"]
already_in_dic = []
word_dic = {}

                    
for index in range(len(lista)):
    if lista[index] not in already_in_dic:
        word_dic[lista[index]] = [lista[index]]

        # for the rest of the array
        for index_2 in range(index+1,len(lista)):
            if get_dic(lista[index]) == get_dic(lista[index_2]):
                word_dic[lista[index]].append(lista[index_2])
                already_in_dic.append(lista[index_2])
        already_in_dic.append(lista[index])



print(list(word_dic.values()))
