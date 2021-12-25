#13. Write a Python script to concatenate following dictionaries to create a new one.

dic1= {1:"Abishek", 2:"Bimali"}
dic2= {3:"Balmiki", 4:"Devi"} 
dic3= {5:"Softwarica",6:"Acadamic"}
dic4={}
for d in (dic1, dic2, dic3): dic4.update(d)

print(dic4)