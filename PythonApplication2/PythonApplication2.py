# -*- coding: utf-8 -*- =>

def sayme(a, b):
	var = 0

	if(a==b):
		var = -1
	else:
		for x in range(a, b):
			var = var + x
	return var


def calcme(a, b):
   return a + b


def printme(str):
   print(str)
   return



printme("Hidayet")

print(calcme(3, 5))

print(sayme(3, 5))

gülistan = "eda"
print(gülistan)

ad = input("üğşiçö (input)giris yap:")
print(ad)




print("{0} ile {1} iyi bir ikilidir.".format("Python", "Django"))