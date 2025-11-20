# - what - : lamda, adalah fungsi tanpa nama / anonymous function


# - why - :
#   ~ pastinya akan dibutuhkan untuk saya membuat aplikasi kalkulator
#   ~ untuk membuat fungsi2 sederhana(lebih baik pakai lambda daripada menulis fungsi seperti biasa jika fungsi nya tidak terlalu kompleks / pendek)
#   ~ untuk menulis fungsi2 sekali pakai


# - how - :

# sintaks
# 1 lamda argumen: ekspresi  /  lamda a: f'hallo {a}'  /  lamda a, b: a + b  ->  lambda + argumen + : + ekspresi
# 2 lamda: ekspresi/hasil  / lamda: 'hallo world'  ->  lambda + : + ekspresi/hasil

# cara panggil
# 1 print
print((lambda nama: f'hallo {nama}')('gus '))    # - gunakan tanda () untuk menulis lamda + gunakan tanda () sekali lagi untuk memanggil fungsi nya

# 2 simpan di variabel
perkalian = lambda a, b: a * b    # - simpan di varibel
print(perkalian(1, 3))    # - mirip seperti memanggil fungsi pada umumnya  ->  variabel nya jadi nama fungsi


