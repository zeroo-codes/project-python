import tkinter as tk    #import tkinter

# 1 Buat jendela utama / window
root = tk.Tk()    #mengapa di namakan root? sec umum root itu berarti akar  ->  var root menyimpan jendela utama
root.title('Kalkulator')    #tambahkan judul di jendela utama  ->  isi method title










# 2 Buat widget + handling ? mengapa event nya tidak dibuat( penjelasan di bawah )

# - Hubungan widget, event, dan handling( penting / konsep)
#   ~ ada 2 tipe widget :
#      1 widget dengan event bawaan spt button  ->  jika widget nya memiliki event bawaan, tidak perlu menghubungkan wiget + event( '<>' ) + handling( command ) dengan method .bind(), langsung tulis handling( command ) di dlm widget nya
#      2 widget tanpa event bawaan  ->  jika widget tidak memiliki event bawaan, widget nya dihubungkan dengan + event( 'n<>' ) + handling( command ) menggunakan method .bind()

# - Catatan( cukup penting )
#   ~ root : ditaruh di awal argumen setiap widget, menandai bahwa setiap widget itu ditempel di variabel root( yg di sini root itu sebagai window ). Dan harus ditaruh di awal
#   ~ .grid() : method untuk memposisikan sebuah widget. Dan harus digunakan pada widget yg dibuat agar widget nya muncul di root / window
#      - row / column : widget diposisikan di baris / kolom ke berapa
#      - rowspan / columnspan : tinggi / lebar widget berapa baris / kolom

# - buat widget entry
entry = tk.Entry(root, width=15, font=("Arial", 16), borderwidth=5, relief='ridge')    
# Penjelasan argumen / parameter( tidak sebegitu penting / sekedar sintak )
# - width : panjang entry nya / banyak huruf yg bisa dimuat. Di sini 20 huruf  
# - font : gaya font, dan ukuran huruf. Di sini gaya arial, dan ukuran 16  
# - bordewidth : ketebalan pinggir. Di sini 5 piksel  |  relief : gaya pinggir. Nah disini gaya nya ridge / spt timbul  |  borderwidth dan relief saling melengkapi
entry.grid(row=0, column=0, columnspan=4)

# - buat widget button 1 : tanpa handling
btn_1 = tk.Button(root, text='1', width=5, height=2)
btn_1.grid(row=1, column=0)

# - buat widget button 2 : dengan handling
btn_2 = tk.Button(root, text='2', width=5, height=2, command=lambda: entry.insert(tk.END, '2'))
btn_2.grid(row=1, column=1)

# Penjelasan argumen( tidak begitu penting / sekedar sintak )
# - text : tulisan yg ingin dimunculkan
# - width / lebar : seberapa lebar tombol nya / horizontal
# - height / tinggi : seberapa tinggi tombol nya / vertikal
# - command : handling  ->  command=lamda: entry.insert(tk.END, '2') : gampangnya memunculkan angka 2 saat di tekan  ->  sintaks : entry.insert(posisi, 'teks')

# - Tambahan( cukup penting )
# - mengapa handling itu harus menggunakan fungsi ? agar hasil handling nya tidak langsung muncul begitu main loop dijalankan, melainkan harus terjadi event dulu baru hasil handling nya muncul
# - bagaiaman cara kerja fungsi dalam gui ? memicu event == memanggil fungsi handling, jadi harus picu event dahulu agar hasil handling muncul, misal harus tekan tombol angka dulu baru keluar angka,
# bukan angka nya keluar duluan sebelum ditekan










# 4 Main loop / event loop
root.mainloop()    #tambahkan methdo mainloop di root agar aplikasi berjalan


















