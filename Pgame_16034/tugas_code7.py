w="Ini Merupakan Perulangan While"	# perulangan “while”
print(w)
x = 0
while (x < 5): 	# jika x lebih kecil dari 5 maka ulangi
# 	x = x + 1
	x += 1 			# x + 1
	print(" Wuyun Hamid ")

u="Ini Merupakan Perulangan For"	# perulangan “for”
print(u)
for x in range(5):
	print("Wuyun Hamid")

y="Ini Merupakan Fungsi / Function"	# Fungsi / Function
print(y)
# Fungsi / Function
def tambah_1(w,u):
	y = w + u
	print(y) # langsung cetak hasil

def tambah_2(w,u):
	y = w + u
	return y # mengembalikan nilai, disimpan dalam fungsi

# cara memanggil kedua fungsi tersebut
tambah_1(15,9)
print(tambah_2(55,9))

# memanggil fungsi dengan variable
w=36
u=38
tambah_1(w,u)
print(tambah_2(w,u))
