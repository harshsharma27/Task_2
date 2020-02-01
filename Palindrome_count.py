# with open("TwowaitsData.txt") as f:
#     a=f.read()
#
#     c = a.count("palindrome ")
#     print(c)

def count(str, word):
    a = str.split()
    count = 0
    for i in range(0, len(a)):
        if (word == a[i]):
            count = count + 1
    return count

f = open("TwowaitsData.txt")
str = f.read()
word = "palindrome"
print(count(str, word))
