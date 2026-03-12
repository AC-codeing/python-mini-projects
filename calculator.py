def tambah(x, y): return x + y
def kurang(x, y): return x - y
def kali(x, y): return x * y
def bagi(x, y): return x / y if y != 0 else "error"

while True:
    try:
        print("\n === Kalkulator Sederhana ===")
        print('\n 1.Tambah 2.Kurang 3.Kali 4.Bagi 5.Keluar')
        a = input("\nSilahkan pilih menu di atas (1-5): ")

        if a in ('1', '2', '3', '4'):
            n1 = float(input("Masukkan angka pertama: "))
            n2 = float(input("Masukkan angka kedua: "))

            if a == '1':
                print(f'{n1} + {n2} = ', tambah(n1, n2))
            elif a == '2':
                print(f'{n1} - {n2} = ', kurang(n1, n2))
            elif a == '3':
                print(f'{n1} x {n2} = ', kali(n1, n2))
            elif a == '4':
                print(f'{n1} / {n2} = ', bagi(n1, n2))
        else:
            break    
    except ValueError: 
        print("Input salah! Masukkan angka yang valid")
else:
    print("Pilihan tidak valid")   
