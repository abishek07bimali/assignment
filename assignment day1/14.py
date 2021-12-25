#14. Write a Python script to check if a given key already exists in a dictionary.
A={1: 'Abishek', 2: 'Bimali', 3: 'Balmiki', 4: 'Devi', 5: 'Softwarica', 6: 'Acadamic',7:"Requirement"}
B=int(input("enter the number: "))
if B in A:
    print("present")
else:
    print("Not Present")
