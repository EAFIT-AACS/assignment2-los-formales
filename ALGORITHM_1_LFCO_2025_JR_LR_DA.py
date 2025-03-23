import random
import string

def palindrome():
    num = random.randint(0, 6)
    pal = ''.join(random.choices(string.ascii_uppercase, k=num))
    select = random.randint(0, 1)
    if select == 1:
        pal += pal[::-1]
    else:
        pal += pal[::-1][1:]
    return pal

def nopalindrome():
    num = random.randint(0, 12)
    nopal = ''.join(random.choices(string.ascii_uppercase, k=num))
    return nopal

def main():
    cant_pal = random.randint(0, 7)
    cant_nopal = random.randint(0, 7)
    palring = []
    while cant_pal != 0 or cant_nopal != 0:
        select = random.randint(0, 1)
        if select == 1 and cant_pal != 0:
            palring.append(palindrome())
            cant_pal -= 1
        elif cant_nopal != 0:
            palring.append(nopalindrome())
            cant_nopal -= 1
    print(palring)

if __name__ == "__main__":
    main()