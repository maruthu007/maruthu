ma=input()
if (ma>='a' and ma<='z') or (ma>='A' and ma<='Z'):
    if ma in ('A','E','I','O','U','a','e','i','o','u'):
        print("Vowel")
    elif ma not in('A','E','I','O','U','a','e','i','o','u'):
        print("Consonant")
else:
    print("invalid")
