import datetime

def print_future_date(num_days):
    # Dapatkan tanggal hari ini
    hari_ini = datetime.date.today()

    # Hitung tanggal di masa depan
    tanggal_di_masa_depan = hari_ini + datetime.timedelta(days=num_days)

    # Array untuk nama hari dalam seminggu
    nama_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

    # Array untuk nama bulan
    nama_bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]

    # Format dan cetak tanggal di masa depan
    print(nama_hari[tanggal_di_masa_depan.weekday()], "pada", tanggal_di_masa_depan.day, nama_bulan[tanggal_di_masa_depan.month - 1], tanggal_di_masa_depan.year)

def main():
    num_days = int(input("Masukkan jumlah hari dari sekarang: "))
    print_future_date(num_days)

if __name__ == "__main__":
    main()