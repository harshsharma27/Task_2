# with open("TwowaitsData.txt") as f:
#     a = f.read()
#     b= "is"
#     c= a.count(b)
    # c=0
    # for i in a:
    #     if i == 'p':
    #         c = c+1
    # print(c)
# Python program to count the number of occurrence
# of a word in the given string given string

def countOccurences(str, word):
    a = str.split()
    count = 0
    for i in range(0, len(a)):
        if (word == a[i]):
            count = count + 1
    return count

f = open("TwowaitsData.txt")
str = f.read()
word = "English"
print(countOccurences(str, word))
