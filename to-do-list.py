print("=== To-do list ===")
print("1.Tambah Tugas")
print("2.Lihat Tugas")
print("3.Hapus Tugas")
print("4.Keluar")

tugas_list = []
while True:
    a = input("Silahkan pilih menu di atas (1-4): ")

    if a == '1':
        tugas = input("Masukkan tugas baru : ")
        tugas_list.append(tugas)
        print("Tugas berhasil di tambah")
    elif a == '2':
        if len(tugas_list) == 0:
            print('Belum ada tugas')
        else:    
            print("Daftar tugas : ")
            for i, t in enumerate(tugas_list, start=1):
                print(f'{i}. {t}')
    elif a == '3':
        if len(tugas_list) == 0:
            print("Tidak ada tugas yang bisa dihapus")
        else:
            print('Daftar tugas : ')
            for i, t in enumerate(tugas_list, start=1):
                print(f'{i}. {t}')
            hapus = int(input("Tugas nomor berapa yang mau dihapus: "))
            if 1 <= hapus <= len(tugas_list):
                tugas_list.pop(hapus - 1)
                print('Tugas berhasil dihapus')
            else:
                print("Nomor tugas tidak valid")
    elif a == '4':                        
        print('Berhasil keluar')
        break
    else:
        print('Menu tidak ada')    
