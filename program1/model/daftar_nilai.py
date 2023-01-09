from tabulate import tabulate
from view import input_nilai
from view import view_nilai


def tambah_data(data):
    newData = input_nilai.input_data(data)
    return newData

def ubah_data(data, nama):
    if nama in data['nama']:
        # buat dictionary kosong untuk menampilkan data yang cocok sesuai input nama
        dataMhs = {}
        index = data['nama'].index(nama)
        # lakukan pengisian data yang cocok ke dalam variabel dataMhs
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])

        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        # lakukan input data apa yang akan diubah
        pilihan = input("pilih field yang akan diubah : \n1.Nama\n2.Nilai\n")
        # lakukan pengecekan pada variabel pilihan yang dikonversi menjadi nilai integer
        match int(pilihan):
            case 1:
                print("data nama sebelumnya : " + dataMhs['nama'][0])
                nama = input("Masukkan nama Baru : ")
                while nama in data['nama']:
                    if nama == dataMhs['nama'][0]:
                        break
                    print("Mahasiswa dengan nama yang sama sudah ada")
                    nama = input("Masukkan nama Baru : ")
                data['nama'][index] = nama

            case 2:
                print("data nilai sebelumnya :" , dataMhs['nilai'][0])
                nilai = input("Masukkan nilai baru : ")
                data['nilai'][index] = nilai

        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        return data
    else:
        print("data nama tidak ditemukan!")

def hapus_data(data, nama):
    if nama in data['nama']:
        # buat dictionary kosong untuk menampilkan data yang cocok sesuai input NIM
        dataMhs = {}
        index = data['nama'].index(nama)

        # lakukan pengisian data yang cocok ke dalam variabel dataMhs
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        print(tabulate(dataMhs, headers="keys", tablefmt="rounded_outline"))
        # lakukan konfirmasi penghapusan
        confirm = input("anda yakin ingin menghapus data ini?? (y/t)")

        # jika input selain y atau t lakukan konfirmasi berulang
        while (confirm not in ['y', 't']):
            print("input salah")
            confirm = input("anda yakin ingin menghapus data ini?? (y/t)")

        # jika konfirmasi selesai dilakukan, maka hapus data mahasiswa pada variabel data
        if confirm == "y":
            for key in data.keys():
                data[key].pop(index)
            print("Data Berhasil Dihapus!!\n")
        return data

    else:
        print("data nama tidak ditemukan!!")

def cari_data(data, nama):
    dataMhs = {}
    if nama in data['nama']:
        index = data['nama'].index(nama)
        for key in data.keys():
            dataMhs[key] = []
            dataMhs[key].append(data[key][index])
        view_nilai.cetak_hasil_pencarian(dataMhs)
    else:
        print("Data Tidak Ditemukan!")
