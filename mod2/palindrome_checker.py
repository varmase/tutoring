#We need 3 things:
# - word
# - left to right index
# - right to left index
# - function = ()
# - indexing = []

def pc(word, l_ind, r_ind):
    if word[l_ind] == word[r_ind] and l_ind >= r_ind:
        return pc(word, l_ind + 1, r_ind - 1)
    if word[l_ind] != word[r_ind]:
        return False
    return True
string = "racecar"
print(pc(string, 0, len(string) - 1))

   



