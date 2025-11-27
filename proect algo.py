import pandas as pd

try:
    pd.read_csv('data_gudang.csv')
except FileNotFoundError:
    df = pd.DataFrame({'Kategori': [], 'Nama Barang': [], 'Jumlah': [], 'Satuan': []})
    df.to_csv('data_gudang.csv', index=False)

data_admin = {
    'username': ['admin123', 'LiverPool'],
    'password': ['admin123', 'YNWA']
}

data_operator = {
    'username': ['Heru123', 'LiverpoolForever', 'Liverpool1-0RealMadrid'],
    'password': ['Herruzzz', "you'll never walk alone", 'Ipulzzaa']
}

def menu_utama():
    while True:
        print("="*50)
        print("Selamat datang di Gudang Barokah")
        print("="*50)
        print("Anda sebagai apa: ")
        print("1. Admin")
        print("2. Operator")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan: ")

        if pilihan == '1':
            login_admin()
        elif pilihan == '2':
            login_operator()
        elif pilihan == '3':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid!\n")

def login_admin():
    name_admin = input("Masukkan username: ")
    password_admin = input("Masukkan password: ")

    if name_admin in data_admin['username']:
        index = data_admin['username'].index(name_admin)
        if data_admin['password'][index] == password_admin:
            print(f"\nLogin berhasil! Selamat datang, {name_admin}\n")
            while True:
                print('''Menu Admin:
1. Tampilkan Data
2. Tambah Data
3. Ubah Data
4. Hapus Data
5. Kembali ke Menu Utama
''')
                jawaban_admin = input("Masukkan pilihan: ")

                if jawaban_admin == '1':
                    tampilkan_data()
                elif jawaban_admin == '2':
                    tambah_data()
                elif jawaban_admin == '3':
                    ubah_data()
                elif jawaban_admin == '4':
                    hapus_data()
                elif jawaban_admin == '5':
                    break
                else:
                    print("Pilihan tidak valid!\n")
        else:
            print("Password salah!\n")
    else:
        print("Username tidak ditemukan!\n")

def login_operator():
    name_operator = input("Masukkan username: ")
    password_operator = input("Masukkan password: ")

    if name_operator in data_operator['username']:
        index = data_operator['username'].index(name_operator)
        if data_operator['password'][index] == password_operator:
            print(f"\nLogin berhasil! Selamat datang, {name_operator}\n")
            while True:
                print('''Menu Operator:
1. Tambah Data
2. Tampilkan Data
3. Kembali ke Menu Utama
''')
                jawaban_operator = input("Masukkan pilihan: ")

                if jawaban_operator == '1':
                    tambah_data()
                elif jawaban_operator == '2':
                    tampilkan_data()
                elif jawaban_operator == '3':
                    break
                else:
                    print("Pilihan tidak valid!\n")
        else:
            print("Password salah!\n")
    else:
        print("Username tidak ditemukan!\n")

def tampilkan_data():
    df = pd.read_csv('data_gudang.csv')
    if df.empty:
        print("\nBelum ada data barang di gudang.\n")
    else:
        print("\nData Barang di Gudang:")
        print(df.to_string(index=False))
        print()

def tambah_data():
    df = pd.read_csv('data_gudang.csv')
    kategori = input("Masukkan kategori (Bahan Baku / Produk Jadi): ")
    nama = input("Masukkan nama barang: ")
    jumlah = int(input("Masukkan jumlah barang: "))
    satuan = input("Masukkan satuan (kg, liter, dll): ")

    data_baru = {'Kategori': kategori, 'Nama Barang': nama, 'Jumlah': jumlah, 'Satuan': satuan}
    df = pd.concat([df, pd.DataFrame([data_baru])], ignore_index=True)
    df.to_csv('data_gudang.csv', index=False)
    print(f"\nData barang '{nama}' berhasil ditambahkan!\n")

def ubah_data():
    tampilkan_data()
    nama = input("Masukkan nama barang yang ingin diubah: ")
    df = pd.read_csv('data_gudang.csv')

    if nama in df['Nama Barang'].values:
        print("\nMasukkan data baru (kosongkan jika tidak ingin mengubah):")
        kategori_baru = input("Kategori baru: ")
        jumlah_baru = input("Jumlah baru: ")
        satuan_baru = input("Satuan baru: ")

        if kategori_baru:
            df.loc[df['Nama Barang'] == nama, 'Kategori'] = kategori_baru
        if jumlah_baru:
            df.loc[df['Nama Barang'] == nama, 'Jumlah'] = int(jumlah_baru)
        if satuan_baru:
            df.loc[df['Nama Barang'] == nama, 'Satuan'] = satuan_baru

        df.to_csv('data_gudang.csv', index=False)
        print(f"\nData barang '{nama}' berhasil diubah!\n")
    else:
        print("\nBarang tidak ditemukan!\n")

def hapus_data():
    tampilkan_data()
    nama = input("Masukkan nama barang yang ingin dihapus: ")
    df = pd.read_csv('data_gudang.csv')

    if nama in df['Nama Barang'].values:
        df = df[df['Nama Barang'] != nama]
        df.to_csv('data_gudang.csv', index=False)
        print(f"\nBarang '{nama}' berhasil dihapus!\n")
    else:
        print("\nBarang tidak ditemukan!\n")

menu_utama()
