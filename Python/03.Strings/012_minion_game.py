# Problem: https://www.hackerrank.com/challenges/the-minion-game/problem
# Score: 40


def minion_game(string):
    s=len(string)
    vowel = 0
    consonant = 0

    for i in range(s):
        if string[i] in "AEIOU":
            vowel+=(s-i)
        else: consonant += (s-i)

    if vowel > consonant:
        print("Kevin "+str(vowel))
    elif consonant > vowel: 
        print("Stuart "+str(consonant))
    else: print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)