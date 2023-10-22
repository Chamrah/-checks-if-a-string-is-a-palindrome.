#Program that checks if a string is a palindrome.
a=str(input())
if (a==a[::-1]):
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palidrome")