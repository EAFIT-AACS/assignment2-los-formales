import random
import string

def palindrome():
    num = random.randint(0, 6)
    pal = ''.join(random.choices(string.ascii_lowercase, k=num))    # Randomly generate a string of lowercase letters
    select = random.randint(0, 1)
    if select == 1:          # If select is 1, the string is a palindrome with even length
        pal += pal[::-1]
    else:                    # If select is 0, the string is a palindrome with odd length
        pal += pal[::-1][1:]
    return pal

def nopalindrome():
    num = random.randint(2, 12)
    nopal = ''.join(random.choices(string.ascii_lowercase, k=num))      # Randomly generate a string of lowercase letters
    # Check if the string is a palindrome, if it is, generate a new string
    if num % 2 == 0:
        if nopal[0:num//2] == nopal[num//2:]:
            nopal = nopalindrome()
    else:
        if nopal[0:num//2] == nopal[num//2+1:]:
            nopal = nopalindrome()
    return nopal

def main():
    strings = []        # List of strings
    for i in range(4):      # Generate 4 palindromes
        new_pal = palindrome()
        # Check if the string is already in the list, if it is, generate a new string
        if new_pal not in strings:
            strings.append(new_pal)
        else:
            i -= 1

    for i in range(4):      # Generate 4 non-palindromes
        new_nopal = nopalindrome()
        # Check if the string is already in the list, if it is, generate a new string
        if new_nopal not in strings:
            strings.append(new_nopal)
        else:
            i -= 1

    random.shuffle(strings)    # Shuffle the list of strings
    print(strings)

if __name__ == "__main__":
    main()