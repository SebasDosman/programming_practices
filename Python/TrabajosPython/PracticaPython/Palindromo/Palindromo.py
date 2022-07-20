contPalindromos = 0
str = ["ama", "amor", "rosa", "omo", "imi"]
reversed_string = [0 for i in range(len(str))]

for i in range(len(str)):
    reversed_string[i] = ''.join(reversed(str[i]))
    
    if (reversed_string[i] == str[i]):
        contPalindromos += 1

print("Existen ", contPalindromos , " palabras palindromas")