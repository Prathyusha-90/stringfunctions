# By using operator overloading
fName = " Kadumuri "
lName =" Prathyusha "
print(fName + " "+lName)

#f string or Interpolation
u = "hi"
h ="ram"
g = f"{u} {h}"
print( g)

#join method
d = "kadumuri"
s = "prathyusha"
b = (d, s)
print((" ...hai...").join(b))

# string split/slicing/diving/partition
email="prathyu@gmail.com"
print(email.split("@"))
fruits= "grapesapple"
print(fruits.split("apple"))

#splitlines
address : str = """ 2-93/3
B.N Reddy 
Madhura nagar
Mahabubnagar
Telangana
India
"""
print(address.split())

family : str = """ 5
father: ramreddy
mother: venkateshwaramma
sisters: sukruthi,pallavi
me: prathyusha
"""
print(family)

#partition
v = "prathyu@gmail.com"
print(v.rpartition("r"))

#Rpartition
b ="prathyu@gmail.com"
print(b.rpartition("@"))
