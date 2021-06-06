def chooseandswap(str):

    temp = sorted(str)
    ch1 = ''
    ch2 = ''
    flag = False
    # choosing
    for i in range(len(str)):
        k = str.index(temp[i])
        for j in range(k):
            if str[j] > temp[i]:
                ch1 = str[j]
                ch2 = temp[i]
            flag = True
            break
        if flag == True:
            break
    #swapping
    output = ""
    for char in str:
        if char == ch1:
            output += ch2
        elif char == ch2:
            output += ch1
        else:
            output += char

    return output

str="ccad"
print(chooseandswap(str))
str="abba"
print(chooseandswap(str))