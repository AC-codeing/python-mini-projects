def tambah(x, y): return x + y
def kurang(x, y): return x - y
def kali(x, y): return x * y
def bagi(x, y): return x / y if y != 0 else "error"

while True:
    try:
        print("=== Kalkulator Sederhana ===")
        print('1.Tambah 2.Kurang 3.Kali 4.Bagi')
        a = input("Silahkan pilih menu di atas (1-4): ")

        if a in ('1', '2', '3', '4'):
            n1 = float(input("Masukkan angka pertama: "))
            n2 = float(input("Masukkan angka kedua: "))

        if a == '1':
            print('Hasil : ', tambah(n1, n2))
        elif a == '2':
            print('Hasil : ', kurang(n1, n2))
        elif a == '3':
            print('Hasil : ', kali(n1, n2))
        elif a == '4':
            print('Hasil : ', bagi(n1, n2))
    except ValueError: 
        print("Input salah! Masukkan angka yang valid")
else:
    print("Pilihan tidak valid")   
