def matchword(word):
    count = 0
    lst = []
    for i in word:
        if len(i) > 1 and i[0] == i[-1]:
            count += 1
            lst.append(i)
    print("List of words with the same first and last letter:", lst)
    return count
l = ["abc", "xyz", "aba", "1221"]
print("Number of words with the same first and last letter:", matchword(l))