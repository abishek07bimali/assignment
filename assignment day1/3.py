# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

A=["Abas","Abd","AbA","AsA"]

B=0
for word in A:
    if len(word)>1 and word[0]==word[-1]:
        B=B+1
        print(B)
