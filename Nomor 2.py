def calculate_product(num):
    product = 1
    for i in range(1, num + 1):
        product *= i
    return product

def main():
    tanggal_hari_ini = 25  # Mengasumsikan hari ini adalah tanggal 25
    num = int(input("Masukkan sebuah angka (tanggal hari ini): "))
    if num != tanggal_hari_ini:
        print("Tanggal hari ini bukanlah", num)
        return
    
    hasil = calculate_product(num)
    print("Hasil perkalian dari semua nilai dari 1 hingga", num, "adalah:", hasil)

if __name__ == "__main__":
    main()