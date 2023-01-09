def input_data(data):
    # buat inputan untuk mengisi nama
    nama = input("Masukkan Nama : ")
    
    # jika nama kurang dari 3 karakter / huruf maka input ulang
    while len(nama) < 3:
        nama = input("Masukkan Nama : ")
    
    # jika ada nama yang sama pada data, maka input nama secara berulang 
    while nama in data['nama']:
        print("Mahasiswa dengan nama yang sama sudah ada")
        nama = input("Masukkan Nama : ")
        
    nilai = input("masukkan nilai : ")
    #jika inputan bukan berupa angka, masukan input ulang
    while not nilai.isnumeric():
        nilai = input("masukkan nilai : ")
    
    # tambah data yang baru ke data utama kemudian return
    data['nama'].append(nama)
    data['nilai'].append(int(nilai))
    print("Data Berhasil Ditambah!!")
    return data