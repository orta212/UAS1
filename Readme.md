Nama 		    : Orta Yamaesa <br>
NIM 			  : 312210147 <br>
Kelas 		  : TI.22.B1 <br>
Mata Kuliah : Bahasa Pemrograman <br>
Praktek		  : Ujian Akhir Semester 1 <br>

#### Daftar Isi
* [Pembuatan Folder dan File sesuai ketentuan](#Pembuatan-Folder-dan-File-sesuai-ketentuan)
* [Program utama pada file main.py](#Program-utama-pada-file-main.py)
* [Cetak Data](#Cetak-Data)
* [Tambah Data](#Tambah-Data)
* [Ubah Data](#Ubah-Data)
* [Hapus Data](#Hapus-Data)
* [Cari Data](#Cari-Data)
* [Input selain dari pilihan pada menu](#Input-selain-dari-pilihan-pada-menu)
* [Keluar Program](#Keluar-Program)

# Pembuatan Folder dan File sesuai ketentuan
1. Struktur Folder <br>
![image](https://user-images.githubusercontent.com/47426095/211249744-e4ab1d18-fe97-4126-8ee2-1a428fc9076c.png)
2. Modul daftar_nilai.py <br>
![image](https://user-images.githubusercontent.com/47426095/211249777-4c7e7968-59ac-4dc7-b75f-1c39971e1a46.png)

3. modul view_nilai.py
![image](https://user-images.githubusercontent.com/47426095/211249858-2d9e1f58-a673-462a-bfa3-ad8c7c4eb02a.png)

4. modul input_nilai.py
![image](https://user-images.githubusercontent.com/47426095/211249871-83a5488d-b1da-403b-8d9a-f1a27b0baded.png)

# Program utama pada file main.py <br>
![image](https://user-images.githubusercontent.com/47426095/211250191-a0f9a684-66d5-4822-bf79-c51fe9b5d2f1.png)

1. lakukan import package local yang sudah dibuat dan juga buat variabel berupa dictionary dengan isi berupa list untuk menampung data nilai

![image](https://user-images.githubusercontent.com/47426095/211249241-0927ae09-8435-40be-a5a4-ed72c686b6a9.png)

nantinya, data nilai seorang mahasiswa akan memiliki index yang sama dengan nama nya <br><br>
![image](https://user-images.githubusercontent.com/47426095/211249571-e42765bd-5b7f-4a20-a645-cf8db4ef7f2b.png)

<br> <br>
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

