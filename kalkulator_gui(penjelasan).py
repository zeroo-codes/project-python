# CATATAN
# - jarak 2 tanda pembatas = penjelasan sintak
# - jarak 4 tanda pembatas = penjelasan 2 konsep di baris yang sama
# - jarak bebas, tapi berurutan + nyambung di beberapa baris = sekedar pembatas biasa









# BAGIAN 0 : IMPORT LIBRARY
import tkinter as tk    # import library tkinter + aliasing



# BAGIAN 1 : BUAT WINDOW
root = tk.Tk()    # 1 buat window + simpan dlm var root, yang berarti window == root  |  sintak buat window : tkinter.Tk()  ->  tk.Tk()
root.title('Kalkulator')    # 2 beri nama gui menggunakan method title










# BAGIAN 2 : BUAT WIDGET ENTRY
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5, relief='ridge', justify='right')    # 1 buat widget entry + styling  |  sintak buat entry : tkinter.Entry()  ->  tk.Entry()
# - root : ditaruh di awal yang berarti entry ini ditempel di var root
# - width : lebar, berapa huruf yang muat. Di sini muat 20 huruf
# - font : gaya + ukuran font. Di sini gaya 'Arial' + ukuran 20
# - borderwidth : lebar bingkai. Di sini 5 pixel    |    relief : gaya bingkai. Di sini gaya 'ridge'    |    di sini borderwidth dan relief saling melengkapi
# - justify : teks nya muncul dari mana, bisa kiri, kanan, tengah. Di sini muncul dari kanan   
entry.grid(row=0, column=0, columnspan=4, pady=10)    # 2 atur tempat entry muncul di window dgn method grid  |  sintak grid : .grid()  ->  harus digunakan sesudah sebuah widget dibuat agar muncul di window
# - row : ditaruh di baris ke berapa. Di sini baris ke 0    |    column : ditaruh di kolom ke berapa. Di sini kolom ke 0
# - columnspan : mau dibuat lebar berapa kolom. Di sini 4 kolom
# - pady / pad y : untuk mengatur jarak sebuah widget dengan widget lainnya secara vertikal. Di sini jarak nya 10 pixel










# BAGIAN 3 : BUAT FUNGSI HANDLING
def klik(tombol):    # 1 buat fungsi klik yang menerima parameter tombol

    # - kondisi untuk setiap argumen tombol yg diterima
       
    if tombol == 'c':    # jika argumen tombol yg diterima 'c'   
        entry.delete(0, tk.END)    # hapus teks di kotak entry dari awal - akhir  |  sintak entry delete : .delete(posisi_awal, posisi_akhir)


    elif tombol == '=':    # jika argumen tombol yg diterima '='

        # buat blok try except untuk mencegah program crash( eval() yg berpotensi menyebabkan crash )
        try:    # jika berhasil 
            hasil = eval(entry.get())    # ambil semua teks / angka yg ada di entry / get() -> hitung expresi mtk nya / eval() -> simpan dlm var 'hasil'  |  sintak di bawah :
            # - get() : untuk mengambil semua teks / angka yg ada di kotak entry
            # - eval() : fungsi bawaan python untuk menghitung ekspresi. Tdk terbatas pada ekspresi mtk saja, bisa ekspresi logika, dll, selama ekspresi nya valid. WARNING(ADA RESIKO NYA)
            entry.delete(0, tk.END)    # kurang lebih sama spt baris ke 59
            entry.insert(tk.END, str(hasil))    # sisipkan / munculkan hasil ekpresi mtk yg sudah dihitung tadi di kotak entry  |  sintak entry insert : .insert(posisi, isi/teks)   
        except:    # jika gagal / pencegahan error
            entry.delete(0, tk.END)    # kurang lebih sama spt baris ke 59 & 69   
            entry.insert(tk.END, 'Error')    # sisipkan / munculkan teks error di kotak entry  |  sintak nya kurang lebih sama spt baris ke 70


    else:    # jika argumen tombol yg diterima selain '=' dan 'c'
        entry.insert(tk.END, tombol)    # munculkan teks / angka di kotak entry spt biasa, dan selalu di posisi terakhir  |  sintak nya kurang lebih sama spt baris ke 70 & 73  

    
    # - Dari kode fungsi di atas, mengapa kode kode nya tidak menggunakan return ? gampang nya karena itu tidak perlu, mau menggunakan retrun atau tidak hasil nya akan sama untuk gui. 
    #   Jadi tidak menulis retrun akan menghemat kode. Untuk jawaban lainnya, 'itu karena gui hanya membutuhkan side effect dari functionnya saja'










# BAGIAN 4 : BUAT WIDGET BUTTON + HANDLING 
tombol_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'c'
]    # 1 buat daftar tombol + susunan tombol 4 x 4 + 1(untuk c)


row_val = 1    # 2 buat variabel row_val sbg baris, dan col_val sebagai kolom untuk mengatur susuan tombol di method grid() nanti.                     |    kode ini saling terhubung dengan sebuah blok kode nantinya               
col_val = 0    # Di sini row_val dimulai dari 1 karena baris 0 + kolom 0 sudah ada entry, jadi di sini tombol nya akan mulai dari baris 1 + kolom 0    | 


for tombol in tombol_list:    # 3 looping list tombol untuk meringkas kode( agar tidak menulis setiap tombol satu satu )
    tk.Button(root, text=tombol, width=5, height=2, font=('Arial', 16),    
              command=lambda t=tombol: klik(t)).grid(row=row_val, column=col_val, padx=5, pady=5)
    # 3.1 bagian tombol  |  sintak buat tombol : tk.Button()
    #   ~ root : menandai bahwa button ini ditempel di var root
    #   ~ text : tulisan tombol
    #   ~ width : lebar tombol. Di sini 5 
    #   ~ height : tinggi tombol. Di sini 2 
    #   ~ font : kurang lebih sama spt baris ke 33

    # 3.2 bagian handling / command
    #   ~ Mengapa handling harus menggunakan fungsi( sec universal ) ? untuk menunda eksekusi. Jika kita tidak menggunakan fungsi dlm handling, nanti kode nya malah keluar langsung setelah gui baru saja dijalankan /
    #     sebelum event terjadi. Jadi penggunaan fungsi dlm handling berguna agar logika 'picu event dahulu baru handling merespon' berjalan. Analogi nya memicu event == memanggil fungsi di python
    #   ~ Mengapa cara menulis fungsi di handling spt :
    #      A. command=fungsi() = salah  ->  karena menulis tanda () berarti memanggil. Jadi di sini tkinter hanya menyimpan hasil fungsi nya, bukan referensi fungsi nya
    #         - Bagaimana cara kerja nya ? untuk menjalankan logika 'picu event dahulu baru handling merespon' tkinter butuh referensi fungsi( objek fungsi ), bukan hasil eksekusi fungsi. 
    #           Sedangkan di sini karena menulis 'command=fungsi()' tkinter akan mendapat hasil eksekusi fungsi nya, bukan referensi fungsi nya. Jadi tkinter tidak dapat memproses handling nya.
    #           Beda cerita jika fungsi nya mereturn ojbek fungsi / referensi fungsi lainnya
    #      B. command=fungsi = benar  ->  karena di sini fungsi nya tidak dipanggil, melainkan hanya disimpan tkinter sebagai referensi fungsi
    #         - Bagiamana cara kerja 'command=fungsi' di tkinter ? karena di sini tidak menulis tanda () berarti fungsi nya tidak dijalankan, yg berarti karena hal itu tkinter akan mendapat referensi fungsi( callback function )
    #           nya, bukan hasil fungsi nya. Kemudian ketika ada event yg terjadi, di sanalah tkinter akan mengecek apakah handling dari event tersebut memiliki referensi fungsi, jika ada tkinter akan menjalankannya
    #           sec otomatis dengan menambahkan tanda (), jika tidak ada tkinter tidak akan memproses apa apa 
    #   ~ Mengapa harus menggunakan fungsi 2 kali( klik + lambda ), mengapa tidak bisa menggunakan 1 fungsi saja ? gampangnya agar fungsi klik bisa ditambahkan argumen( 1 'command=klik'  ->  tidak ada argumen.
    #     2 'command=klik(tombol)'  ->  memberikan hasil fungsi / salah juga. 3 'command=lambda t=tombol: klik(t)'  ->  benar )
    #      - Bagaimana cara kerja nya ? lambda digunakan sebagai pembungkus fungsi klik agar fungsi klik bisa ditambahkan argumen. Urutan nya : lambda dipanggil tkinter / lambda jadi callback function nya tkinter -> 
    #        kemudian lambda memanggil fungsi klik yang sudah disertakan argumen / fungsi klik jadi callback function nya lambda
    #   ~ Mengapa pada lambda nya harus ditambahkan argumen lagi( t=tombol ), mengapa tidak diskip saja ? gampangnya adalah agar setiap tombol memiliki handling nya masing masing / agar semua tombol tidak menggunakan
    #     handling dari tombol terakhir( di sini tombol c )
    #      - Bagaimana cara kerja nya ? ada yang namanya late binding jika kita hanya menggunakan 'command=lambda: klik(tombol)', gampangnya di sini fungsi lambda hanya menyimpan referensi dari nilai tombol bukan
    #        nilai tombol itu sendiri, dan hasil dari perilaku tersebut adalah setiap fungsi lambda nya nanti akan menggunakan nilai terakhir dari tombol( di sini c ) di semua tombol nya. Jadi solusi nya adalah
    #        early binding( t=tombol ), dengan menambahkan argumen 't=tombol' pada lambda nya, berarati setiap lambda nanti nya akan menyimpan setiap nilai dari tombol, bukan referensi nya, jadi semua tombol akan
    #        memiliki handling nya masing masing
    #
    
    # 3.3 bagian posisi / grid()   |  sintak dan penjelasan parameter nya kurang lebih sama spt baris ke 39 - 42

    col_val += 1    # tambahkan nilai col_val 1 per setiap looping    |    gampangnya blok kode di sini berguna untuk mengatur susunan tombol agar bisa jadi 5 x 4 dengan cara, 1 menambahkan nlai kolom nya setiap kali looping
    if col_val > 3:    # jika nilai col_val sudah lebih dari 3        |    ->  2 setelah itu buat kondisi ketika kolom nya sudah bernilai 3  ->  2.1 reset nilai kolom nya ke 0, dan di saat yg sama tambahkan nilai baris nya 1.
        col_val = 0    # reset nilai col_val ke 0                     |    Dan blok kode ini saling terhubung dengan 2 variabel yg sudah dibuat tadi(row_val, dan col_val)
        row_val += 1    # tambahkan nilai row_val 1                   |










# BAGIAN 5 : MAIN LOOP / JALANKAN GUI
root.mainloop()










# CATATAN TAMBAHAN
#
# - Hubungan widget, event, dan handling
#   ~ ada 2 tipe widget :
#      1 widget dengan event bawaan spt button  ->  jika widget nya memiliki event bawaan, tidak perlu menghubungkan wiget + event( '<>' ) + handling( command ) dengan method .bind(), langsung tulis handling( command ) di dlm widget nya
#      2 widget tanpa event bawaan  ->  jika widget tidak memiliki event bawaan, widget nya dihubungkan dengan + event( 'n<>' ) + handling( command ) menggunakan method
#
# - Mengapa referensi fungsi dalam handling( command=klik ), dan lambda dalam handling( command=lambda: entry.insert(tk.END, 'tertekan') ), bisa menghasilkan hal yang sama ? karena ke 2 nya sama sama
#   menghasilkan objek fungsi, tapi cuma beda bentuk( satu nya menggunakan referensi fungsi, dan satu nya lambda )






