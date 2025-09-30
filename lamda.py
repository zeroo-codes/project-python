# - what - : lamda, adalah fungsi tanpa nama / anonymous function


# - why - : untuk sekarang saya kurang tahu, tapi yg penting saya belajar lamda untuk buat app kalkulator


# - how - :

# sintaks
# 1 lamda argumen: ekspresi  /  lamda a: f'hallo {a}'  /  lamda a, b: a + b 
# 2 lamda: ekspresi/hasil  / lamda: 'hallo world'

# cara panggil
# 1 print
print((lambda nama: f'hallo {nama}')('gus '))    # - gunakan tanda () untuk menulis lamda + gunakan tanda () sekali lagi untuk memanggil fungsi nya

# 2 simpan di variabel
perkalian = lambda a, b: a * b    # - simpan di varibel
print(perkalian(1, 3))    # - mirip seperti memanggil fungsi pada umumnya  ->  variabel nya jadi nama fungsi