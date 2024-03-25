import datetime

#Tahun saat ini
tahun_sekarang = datetime.datetime.now().year

#Menghitung jumlah hari dalam tahun ini
if tahun_sekarang % 4 == 0 and (tahun_sekarang % 100 != 0 or tahun_sekarang % 400 == 0):
    num_days_in_year = 366
else:
    num_days_in_year = 365

#Membaca sebuah bilangan bulat dari pengguna
bilangan_bulat = int(input("Masukkan sebuah bilangan bulat: "))

#Menghitung hasilnya
hasil = bilangan_bulat / num_days_in_year

#Menampilkan hasilnya
hasil_terformat = "{:.11f}".format(hasil)
print("Hasil:", hasil_terformat)