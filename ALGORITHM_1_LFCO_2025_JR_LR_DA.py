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
    while True:
        num = random.randint(2, 12)
        nopal = ''.join(random.choices(string.ascii_lowercase, k=num))  # Randomly generate a string of lowercase letters

        # Check if the string is not a palindrome
        if num % 2 == 0:
            if nopal[0:num // 2] != nopal[num // 2:]:
                return nopal        # Return the string if it is not a palindrome
        else:
            if nopal[0:num // 2] != nopal[num // 2 + 1:]:
                return nopal        # Return the string if it is not a palindrome

def generate():
    strings = set()             # Use a set to store the strings to avoid duplicates

    while len(strings) < 4:
        new_pal = palindrome()      # Generate palindromes
        strings.add(new_pal)

    while len(strings) < 8:
        new_nopal = nopalindrome()      # Generate non-palindromes
        strings.add(new_nopal)

    return list(strings)            # Return the list of strings

def print_strings(strings):
    print("Strings generated:")
    for i, string in enumerate(strings, 1):
        string = string if string else 'ε'          # Replace empty strings with 'ε'
        print(f"{i}. {string}")                     # Print the string

if __name__ == "__main__":
    strings = generate()
    print_strings(strings)
