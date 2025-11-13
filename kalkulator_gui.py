import tkinter as tk



# buat window
root = tk.Tk()
root.title('Kalkulator')





# buat kotak input( widget )
entry = tk.Entry(root, width=20, font=('Arial', 20), borderwidth=5, relief='ridge', justify='right')    
entry.grid(row=0, column=0, columnspan=4, pady=10)    





# buat fungsi handler
def klik(tombol):    
    if tombol == 'c':    
        entry.delete(0, tk.END)    
    elif tombol == '=':
        try:    
            hasil = eval(entry.get())    
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(hasil))    
        except:    
            entry.delete(0, tk.END)    
            entry.insert(tk.END, 'Error')    
    else:
        entry.insert(tk.END, tombol)    





# daftar tombol     
tombol_list = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'c'
]





# buat + tempatkan tombol
row_val = 1
col_val = 0

for tombol in tombol_list:
    tk.Button(root, text=tombol, width=5, height=2, font=('Arial', 16),
              command=lambda t=tombol: klik(t)).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1



# jalankan main loop
root.mainloop()