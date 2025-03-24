import random
import string

def palindrome():
    num = random.randint(0, 6)
    pal = ''.join(random.choices(string.ascii_lowercase, k=num))
    select = random.randint(0, 1)
    if select == 1:
        pal += pal[::-1]
    else:
        pal += pal[::-1][1:]
    return pal

def nopalindrome():
    num = random.randint(2, 12)
    nopal = ''.join(random.choices(string.ascii_lowercase, k=num))
    if num % 2 == 0:
        if nopal[0:num//2] == nopal[num//2:]:
            nopal = nopalindrome()
    else:
        if nopal[0:num//2] == nopal[num//2+1:]:
            nopal = nopalindrome()
    return nopal

def main():
    num_pal = random.randint(2, 7)
    num_nopal = random.randint(2, 7)
    palring = []
    while num_pal != 0 or num_nopal != 0:
        select = random.randint(0, 1)
        if select == 1 and num_pal != 0:
            palring.append(palindrome())
            num_pal -= 1
        elif num_nopal != 0:
            palring.append(nopalindrome())
            num_nopal -= 1
    print(palring)

if __name__ == "__main__":
    main()