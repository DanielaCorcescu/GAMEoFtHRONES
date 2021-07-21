# Game of Thrones
# Dothraki plănuiesc să usurpe tronul Regelui Robert. Regele Robert aude de această
# conspirație de la un raven și plănuiește
# să încuie singura ușă prin care inamicul poate să pătrundă în regat lui.
#     Dar această ușă are nevoie de o cheie care este reprezentată
#     de către anagrama unui palindrom.
#     începe să caute în cutia lui de șiruri de caractere,
#     verificând pe fiecare în parte dacă poate fi rearanjat într-un palindrom.
# Cerință:
#     Pentru un șir de caractere,
#     să se tipărească pe ecran cuvântul DA sau NU
#     dacă acest șir poate fi rearanjat astfel încât să fie
#     un palindrom.
# Constrangeri:
# Poat fi folosite doar caractere
# din alfabetul latin cu litere mici
# Date de intrare:
#     Șirul de caractere.
# Exemplu:
# INPUT:
# aaabbbb
# OUTPUT:
# DA
# Șirul poate fi permutat astfel: bbaaabb

def checkpal(word):
    # we create an empty list to which we're adding the string
    char_list = []
    for i in word.lower():
        # if the character is not in our list, we add it
        if i not in char_list:
            char_list.append(i)
        # if the character is in our list, we remove it
        else:
            char_list.remove(i)
    # if the lenght of the list and the lenght...
    if len(char_list) == 0 and len(word) % 2 == 0:
        print("True")
    # if the lenght of the list and the lenght of the string are odd numbers, the string is also a palindrome
    # but in this case only 1 character repeats itself an odd number of time
    elif len(char_list) == 1 and len(word) % 2 == 1:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    str = input("Introduce-ti un string ")
    checkpal(str)