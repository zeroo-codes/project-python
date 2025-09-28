#kalkulator : alur(while True -> print menu -> user input -> while True -> minta angka dan operator -> ketik balik buat balik -> balik ke menu awal)

while True:    #looping pertama
    print('\n--- KALKULATOR --- \n1 Gunakan \n2 Keluar')    #menu

    pilihan = input('Pilih nomor menu(1 / 2) : ')    #user input
    if pilihan == '2':    #konsdisi looping pertama kalo keluar
        print('\nKeluar dari kalkulator')
        break

    elif pilihan == '1':    #kondisi looping pertama kalo masuk
        while True:
            try:    #blok try except
                #minta angka + operator
                angka_1 = int(input('\nMasukan angka pertama : '))  
                operator = input('Masukan operasi matematika(x, :, +, -) : ')
                angka_2 = int(input('Masukan angka pasangan nya : '))

                if operator == 'x':    #kondisi perkalian
                    print(f'{angka_1} x {angka_2} = {angka_1 * angka_2}')    
                elif operator == ':':
                    print(f'{angka_1} : {angka_2} = {angka_1 / angka_2}')
                elif operator == '+':
                    print(f'{angka_1} + {angka_2} = {angka_1 + angka_2}')
                elif operator == '-':
                    print(f'{angka_1} : {angka_2} = {angka_1 - angka_2}')
                else:
                    print('operasi matematika tidak valid')
            
            except ValueError:
                print('Angka tidak valid')
            except ZeroDivisionError:
                print('Tidak bisa membagi angka dengan nol')
            
            sub_pilihan = input('\nKetik "keluar" untuk kembali ke menu awal : ')    #user input ke 2

            if sub_pilihan.lower() == 'keluar':
                break

    else:
        print('\nMenu tidak valid')


    