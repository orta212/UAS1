
Nama 		    : Orta Yamaesa <br>
NIM 			  : 312210147 <br>
Kelas 		  : TI.22.B1 <br>
Mata Kuliah : Bahasa Pemrograman <br>
Praktek		  : Ujian Akhir Semester 1 <br>

#### Daftar Isi
[Pembuatan Folder dan File sesuai ketentuan :	3](#Pembuatan-Folder-dan-File-sesuai-ketentuan)

[Program utama pada file main.py	4](#_Toc124159784)

[Cetak Data	5](#_Toc124159785)

[Tambah Data	6](#_Toc124159786)

[Ubah Data	7](#_Toc124159787)

[Hapus Data	8](#_Toc124159788)

[Cari Data	9](#_Toc124159789)

[Input selain dari pilihan pada menu	10](#_Toc124159790)

[Keluar Program	10](#_Toc124159791)






![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.002.png)

# Pembuatan Folder dan File sesuai ketentuan
1. Struktur Folder 
![Aspose Words 3da5a5f8-9048-439b-a62f-2e08a7f81535 002](https://user-images.githubusercontent.com/47426095/211247792-28b1b63b-2027-43cf-8a7b-87f5686625ff.png)


1. Modul daftar\_nilai.py

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.004.png)


1. modul view nilai.py

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.005.png)

2. modul input\_nilai.py

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.006.png)
# Program utama pada file main.py
##### ![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.007.png)

1. lakukan import package local yang sudah dibuat dan juga buat variabel berupa dictionary dengan isi berupa list untuk menampung data nilai

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.008.png)

nantinya, data nilai seorang mahasiswa akan memiliki index yang sama dengan nama nya



1. buat fungsi perulangan dengan while sehingga program akan terus berjalan berulang ulang,
1. kemudian cetak daftar menu agar dapat dipilih oleh user
1. minta user untuk input pilihan menu
1. kemudian lakukan pengecekan terhadap inputan user menggunakan *match* (mungkin lebih familiar dengan *switch case* di bahasa pemrograman lain)

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.009.png)

# Cetak Data
jika inputan berupa ‘l’, maka akan menampilkan data

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.010.png)

- proses menampilkan data akan ditangani oleh cetak\_daftar\_nilai yang ada pada file view\_nilai dan kita kirim variabel data sebagai parameter

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.011.png)

- import modul tabulate untuk kita gunakan dalam menampilkan data berbentuk tabel
- tangkap data yang dikirimkan, lalu cek apakah ada isi dari data tersebut
- jika ada kita tampilkan data nya
- jika tidak ada, maka cetak pesan “Tidak Ada Data”

# Tambah Data
jika input berupa ‘t’, maka lakukan penambahan data

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.012.png)

- data yang lama akan kita timpa dengan data yang sudah diproses pada tambah\_data di daftar\_nilai.py, kita kirimkan variabel data sebagai parameter
- data akan ditangkap oleh tambah\_data, kemudian akan di proses pada input\_data pada input\_nilai setelah, diproses, kemuadian masukan ke dalam variabel newData, lalu return kembali ke main.py

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.013.png)

- tangkap data, kemudian proses input data baru

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.014.png)

- buat inputan nama, lakukan pengecekan
- kemudian input nilai, lakukan pengecekan kembali
- tambahkan data baru dengan fungsi append
- cetak pesan ‘data berhasil ditambah’








# Ubah Data
jika inputan ‘u’ , maka akan masuk program mengubah data
##### ![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.015.png)
- cetak daftar nilai terlebih dahulu untuk mencetak daftar nilai, jika tidak ada data akan muncul keterangan tidak ada data
- kemudian cek jika ada data di daftar nilai lakukan input data nama yang akan diubah, kemudian akan di proses pada ubah\_data di daftar nilai kemudian kirim data utama dan juga nama yang di input sebagai parameter, setelah di proses akan menimpa data utama

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.016.png)

- cek nama yang di kirim dari main.py, lalu cek apakah nama yang di input ada pada data utama
- jika ada buat variabel *dataMhs* yang akan menampung data mahasiswa yang akan diubah

- kemudian buat variabel index untuk menyimpan index dari data mahasiswa tersebut (karena nama dan nilai nya memiliki index yang sama) gunakan fungsi index() untuk mencari index dari data yang cocok, lakukan pencarian menggunakan nama karena index nya sama dengan nilai
- lakukan pengulangan untuk mencetak key dari variabel data, kemudian isi variabel *dataMhs* dengan key yang ada pada variabel data, kemudian lakukan fungsi append berdasarkan pada data nama yang telah di dapatkan index nya
- kemudian tampilkan data nya dengan modul *tabulate*
- beri pilihan data yang akan diubah
- kemudian masukan data baru, jika data nama sudah ada, maka akan gagal
- jika berhasil, tampilkan kembali data yang sudah diubah
- kemudian return data

# Hapus Data
jika inputan ‘h’ maka akan melakukan hapus data

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.017.png)

- cetak daftar nilai terlebih dahulu untuk mencetak daftar nilai, jika tidak ada data akan muncul keterangan tidak ada data
- kemudian cek jika ada data di daftar nilai lakukan input data nama yang akan diubah, kemudian akan di proses pada hapus\_data di daftar nilai kemudian kirim data utama dan juga nama yang di input sebagai parameter yang kemudian akan mendapat data baru lalu menimpa data yang lama

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.018.png)

- cek nama yang di kirim dari main.py, lalu cek apakah nama yang di input ada pada data utama
- jika ada buat variabel *dataMhs* yang akan menampung data mahasiswa yang akan diubah
- kemudian buat variabel index untuk menyimpan index dari data mahasiswa tersebut (karena nama dan nilai nya memiliki index yang sama) gunakan fungsi index() untuk mencari index dari data yang cocok, lakukan pencarian menggunakan nama karena index nya sama dengan nilai
- lakukan pengulangan untuk mencetak key dari variabel data, kemudian isi variabel *dataMhs* dengan key yang ada pada variabel data, kemudian lakukan fungsi append berdasarkan pada data nama yang telah di dapatkan index nya
- kemudian tampilkan data nya dengan modul *tabulate*
- buat inputan untuk konfirmasi,
- jika inputan selain y atau t, maka lakukan input secara berulang
- jika input y maka gunakan fungsi pop(index) untuk menghapus data pada data utama
- kemudian tampilkan pesan “Data berhasil dihapus”
- return data
- jika data nama tidak ada yang cocok, maka tampilkan pesan gagal
# Cari Data
jika inputan ‘c’ maka akan melakukan hapus data

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.019.png)

- jika ada data di daftar nilai lakukan input data nama yang akan diubah, kemudian akan di proses pada cari\_data di daftar nilai kemudian kirim data utama dan juga nama yang di input sebagai parameter

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.020.png)

- cek nama yang di kirim dari main.py, lalu cek apakah nama yang di input ada pada data utama
- jika ada buat variabel *dataMhs* yang akan menampung data mahasiswa yang akan diubah
- kemudian buat variabel index untuk menyimpan index dari data mahasiswa tersebut (karena nama dan nilai nya memiliki index yang sama) gunakan fungsi index() untuk mencari index dari data yang cocok, lakukan pencarian menggunakan nama karena index nya sama dengan nilai
- lakukan pengulangan untuk mencetak key dari variabel data, kemudian isi variabel *dataMhs* dengan key yang ada pada variabel data, kemudian lakukan fungsi append berdasarkan pada data nama yang telah di dapatkan index nya
- jika data sudah ada pada dataMhs, maka panggil fungsi cetak\_hasil\_pencarian() yang ada pada view\_nilai.py
- di fungsi cetak\_hasil\_pencarian(dataMhs) lakukan cetak data yang dikirim dari daftar\_nilai.py dengan modul *tabulate*
- jika tidak ada data, maka tampilkan pesan kesalahan “Data Tidak Ditemukan”

# Input selain dari pilihan pada menu
bagaimana jika yang diinputkan user tidak sesuai dengan pilihan??

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.021.png)

- tampilkan pesan “Tidak sesuai pilihan, silahkan pilih kembali”
- kemudian gunakan *continue* untuk memilih ulang menu yang tersedia
# Keluar Program
jika hasil inputan adalah ‘k’, maka kode akan keluar dari program

![](Aspose.Words.3da5a5f8-9048-439b-a62f-2e08a7f81535.022.png)

- cetak pesan bahwa sudah keluar dari program
- kemudian gunakan *break* untuk menghentikan pengulangan yang berarti program sudah selesai

