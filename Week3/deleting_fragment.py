string = input()
result1 = string.find('h')
length = len(string)
if result1 != -1:
    result2 = length - 1 - string[::-1].find('h')
    string = string[:result1] + string[result2 + 1:]
    print(string)
