string = input()
result1 = string.find('h')
length = len(string)
if result1 != -1:
    result2 = length - 1 - string[::-1].find('h')
    string = string[:result2] + string[result1 + 1: result2] + string[result2:]
    print(string)
