from tabulate import tabulate
from datetime import datetime

# User Login
users = {
    'senior': {'password': 'senior123', 'role': 'Senior Engineer'},
    'junior': {'password': 'junior123', 'role': 'Junior Engineer'}
}

# Dummy data aset information di field X 
data_aset = {
    'PA1': {'Equipment': 'Pompa', 'tgl_sertif': '15-01-2010', 'Resiko': 'Tinggi', 'Status_Sertif': 'Belum', 'Area': 'Zona 1'},
    'PA2': {'Equipment': 'Pompa', 'tgl_sertif': '29-04-2001', 'Resiko': 'Tinggi', 'Status_Sertif': 'Belum', 'Area': 'Zona 1'},
    'PG1': {'Equipment': 'Piping', 'tgl_sertif': '18-04-2005', 'Resiko': 'Sedang', 'Status_Sertif': 'Belum', 'Area': 'Zona 1'},
    'PG2': {'Equipment': 'Piping', 'tgl_sertif': '03-05-2011', 'Resiko': 'Sedang', 'Status_Sertif': 'Belum', 'Area': 'Zona 1'},
    'KR1': {'Equipment': 'Kompressor', 'tgl_sertif': '18-05-2002', 'Resiko': 'Tinggi', 'Status_Sertif': 'Belum', 'Area': 'Zona 1'},
    'KR2': {'Equipment': 'Kompressor', 'tgl_sertif': '12-02-2016', 'Resiko': 'Tinggi', 'Status_Sertif': 'Belum', 'Area': 'Zona 1'}
}

#Fungsi untuk input loging
def login():
    while True:
        # Meminta input username
        username = input("Masukkan username (Senior/Junior): ").strip()
        
        # Jika input adalah '*' untuk keluar
        if username == '*':
            return None, None
        
        # Verifikasi bahwa username tidak kosong
        if not username:
            print("Username tidak boleh kosong! Silakan coba lagi.")
            continue  # Mengulang loop dan meminta input lagi

        # Meminta input password
        password = input("Masukkan password: ").strip()
        
        # Jika input adalah '*' untuk keluar
        if password == '*':
            return None, None
        
        # Verifikasi bahwa password tidak kosong
        if not password:
            print("Password tidak boleh kosong! Silakan coba lagi.")
            continue  # Mengulang loop dan meminta input lagi

        # Validasi jika username dan password cocok
        if username in users and users[username]['password'] == password:
            print(f"Login berhasil sebagai {users[username]['role'].capitalize()}")
            return username, users[username]['role']  # Kembalikan username dan role jika valid
        else:
            print("Login gagal! Username atau password salah.")
            return None, None  # Kembalikan None jika login gagal

#Fungsi input dan cek equipment
def input_equipment():
    while True:  # Memulai loop terus-menerus
        equipment = input("Masukkan nama equipment (hanya huruf dan tanpa spasi) atau tekan b untuk kembali: ").strip()

        # Jika input adalah 'b', keluar dari loop
        if equipment == 'b':
            return None  # Keluar dari loop jika input 'b'

        # Cek apakah input kosong
        if not equipment:
            print("Harus diisi, silakan masukkan input")
            continue  # Kembali ke awal loop dan meminta input lagi

        # Validasi jika equipment hanya terdiri dari huruf dan tanpa spasi
        elif equipment.replace(" ", "").isalpha():
            print(f"Equipment '{equipment}' valid.")
            return equipment  # Mengembalikan input yang valid

        # Jika input tidak valid (mengandung angka atau simbol selain huruf)
        else:
            print("Equipment tidak valid! Harus hanya huruf dan tanpa spasi. Coba lagi.")


#Fungsi input dan cek Asset ID
def input_aset(equipment):
    Kode_Peralatan = equipment[0].upper()+equipment[-1].upper()

    while True:
        aset_id = input(f"Masukkan aset ID untuk equipment {equipment} (dengan format {Kode_Peralatan}1,{Kode_Peralatan}2) atau tekan b untuk kembali: ")
        # Jika input adalah 'b', keluar dari loop
        if aset_id == 'b':
            return None # Keluar dari loop jika input 'b'
        # Cek apakah input kosong
        if not aset_id:
            print("Harus diisi, silakan masukkan input") # Mengembalikan input yang valid
        # cek jika aset.id  sesuai dengan kriteria penamaan
        elif aset_id[:2] == Kode_Peralatan and aset_id[2:].isdigit() and len(aset_id[2:]) == 1:
            return aset_id # Mengembalikan input yang valid
        
        # Jika input tidak valid 
        else:
            print(f"Aset ID tidak valid! Silakan kode diawali dengan {Kode_Peralatan} dan diikuti nomor urut 2 digit pertama, seperti {Kode_Peralatan}1 ")

# Fungsi input dan cek area
def input_area():
    valid_zones = ['Zona 1', 'Zona 2', 'Zona 3']  # Daftar zona yang valid
    while True:
        area = input(f"Masukkan area (pilihan area: Zona 1, Zona 2, dan Zona 3)(atau tekan b untuk kembali)").strip()

        # Jika input adalah 'b', keluar dari fungsi
        if area == 'b':
            return None  # Kembali ke menu jika input 'b'
        
        if not area:
            print("Harus diisi, silakan masukkan input")
        # Memeriksa apakah input area sesuai dengan zona yang valid
        elif area in valid_zones:
            return area  # Mengembalikan area yang valid
        else:
            print(f"Area tidak valid! Pilihan valid: {', '.join(valid_zones)}. Silakan coba lagi.")

#Fungsi input dan cek resiko
def input_resiko():
    while True:
        resiko = input(f"Masukkan resiko untuk equipment (Tinggi,Sedang,Rendah) atau tekan b untuk kembali: ").title()
        # Jika input b, maka akan keluar dari loop dengan None
        if resiko == 'b':
            return None
        
        # Cek input apakah kosong
        if not resiko:
            print("Harus diisi, silakan masukkan input") # jika kosong akan mengulang loop input

        # Cek apakah input termasuk ke kriteria resiko
        elif resiko in ['Tinggi','Sedang','Rendah']:
            return resiko # Mengembalikan input valid
        
        else:
            print("Resiko tidak valid! masukkan sesuai pilihan (Tinggi,Rendah,Kecil)")

#Fungsi input dan cek tgl_sertif
def input_tgl_sertif():
    while True:
        tgl_sertif = input("Masukkan tanggal sertifikasi (dd-mm-yyyy) atau b untuk kembali: )")

        # cek input apakah b
        if tgl_sertif == 'b':
            return None # Keluar dari loop
        
        # cek input apakah kosong
        if not tgl_sertif:
            print("Harus diisi, silakan masukkan input")
        
        # Mengkonversi input tanggal ke format date time
        try:
            datetime.strptime(tgl_sertif, "%d-%m-%Y") # Format tanggal yang diinginkan
            return tgl_sertif # Mengembalikkan nilai tgl_sertif yang sudah sesuai
        except ValueError: # Apabila format salah maka akan looping ke input tgl sertif
            print("Fromat tanggal tidak valid! Format harus dd-mm-yyyy")

#Fungsi input dan cek status sertifikasi
def input_sertif():
    while True:
        status_sertif = input("Masukkan status sertifikatsi equipment (Belum atau sudah) atau b untuk kembali: ").title()
        
        # cek input apakah b
        if status_sertif == 'b':
            return None # Mengeluarkan dari loop
        
        # cek apakah input tidak kosong
        if not status_sertif:
            print("Harus diisi, silakan masukkan input")

        # cek validasi input
        elif status_sertif in ['Belum','Sudah']:
            return status_sertif # mengembalikkan value input sebagai variable
        
        else:
            print("Status sertifikasi tidak valid! Masukkan sesuai pilihan (Belum atau sudah) ")


#Fungsi untuk membuat table
def tampilkan_data_aset(data):
    # Format data aset untuk tabulate
    aset_list = []  # Membuat list kosong untuk menampung data aset

    # Iterasi untuk setiap aset dalam data
    for asset_id, aset in data.items():
        # Menambahkan data aset dalam bentuk list ke aset_list
        aset_list.append([asset_id, aset['Equipment'], aset['tgl_sertif'], aset['Resiko'], aset['Status_Sertif'], aset['Area']])

    # Header kolom tabel
    headers = ['Asset ID', 'Equipment', 'Tanggal Sertifikasi', 'Resiko', 'Status Sertifikasi', 'Area']
    
    # Menampilkan data dalam tabel menggunakan tabulate dengan alignment untuk memperbaiki sejajarnya
    print(tabulate(aset_list, headers=headers, tablefmt='fancy_grid', stralign='left', numalign='center'))

#Fungsi untuk melihat table (read table)
def read_aset(role,username=None):
    if role == 'Senior Engineer' or role == 'Junior Engineer':
        while True:
            pilihan_menu = input('1. Lihat semua data \n2. Lihat data aset yang lebih dari 20 tahun (Per-tahun ini)\n Masukkan pilihan (atau tekan b untuk kemabli):' )
            if not pilihan_menu:
                continue

            if pilihan_menu == 'b':
                return

            if pilihan_menu == '1':
                tampilkan_data_aset(data_aset)
                break
            
            elif pilihan_menu == '2':
                tahun_ini = datetime.now().year
                data_lebih_20_tahun = {aset_id : aset for aset_id,aset in data_aset.items() if (tahun_ini - int(aset['tgl_sertif'].split('-')[2])) >20}
                if data_lebih_20_tahun:
                    tampilkan_data_aset(data_lebih_20_tahun)
                    return
                
                else:
                    print("Tidak ada aset yang lebih dari 20 Tahun")
            
            else:
                print("Pilihan tidak valid! Masukkan sesuai pilihan yang ada")
    
    else:
        print("Anda tidak memiliki akses untuk masuk!")

# Fungsi untuk membuat value baru (create)
def create_aset(role,username=None):
    if role == 'Senior Engineer':
        #Masukkan input equipment nya dulu untuk cek validasi aset id yang nanti diinput
        equipment = input_equipment()
        if equipment == None:
            return
        
        aset_id = input_aset(equipment)
        if aset_id == None:
            return
        if aset_id in data_aset:
            print(f"Aset dengan ID {aset_id} sudah ada!")
            return
        

        tgl_sertif = input_tgl_sertif()
        if tgl_sertif is None:
            return
        resiko = input_resiko()
        if resiko is None:
            return
        status_sertif = input_sertif()
        if status_sertif is None:
            return
        area = input_area()
        if area is None:
            return
        # Menampilkan data yang akan disimpan
        print("\nData yang dimasukkan:")
        print(f"Asset ID: {aset_id}")
        print(f"Equipment: {equipment}")
        print(f"Tanggal Sertifi: {tgl_sertif}")
        print(f"Resiko: {resiko}")
        print(f"Status Sertif: {status_sertif}")
        print(f"Area: {area}")

        # Menanyakan apakah data ingin disimpan
        while True:
            simpan = input("\nApakah Anda ingin menyimpan data ini? (Ya/Tidak): ").strip().lower()
            if simpan == 'ya':
                # Menyimpan data ke dictionary dengan key aset_id
                data_aset[aset_id] = {
                    'Equipment': equipment,
                    'tgl_sertif': tgl_sertif,
                    'Resiko': resiko,
                    'Status_Sertif': status_sertif,
                    'Area': area
                }
                print("Data aset berhasil disimpan.")
                return  # Kembali ke menu utama setelah data disimpan
            elif simpan == 'tidak':
                print("Data tidak disimpan.")
                return  # Kembali ke menu setelah memilih 'tidak'
            else:
                print("Pilihan tidak valid, data tidak disimpan. Harap masukkan 'Ya' atau 'Tidak'.")
                continue  # Mengulang input jika pilihan tidak valid

    else:
        print("Anda tidak memiliki akses untuk menambah data aset.")

# Fungsi update setatus sertifikasi
def update_status_sertifikasi(role, username=None):
    if role == 'Senior Engineer':
        # Meminta input untuk equipment
        equipment = input_equipment()
        if equipment is None:
            return  # Keluar jika input equipment tidak valid

        # Meminta input aset_id berdasarkan equipment
        aset_id = input_aset(equipment)
        if aset_id is None:
            return  # Keluar jika input aset_id tidak valid

        # Memeriksa apakah asset_id ada dalam data_aset
        if aset_id in data_aset:
            # Meminta input status sertifikasi baru
            new_status = input_sertif()
            
            # Validasi apakah input status sertifikasi tidak kosong dan valid
            if new_status in ['Belum', 'Sudah']:
                while True:
                    simpan = input("\nApakah Anda ingin menyimpan update data ini? (Ya/Tidak): ").strip().lower()
                    
                    # Jika pengguna memilih 'Ya', update status sertifikasi
                    if simpan == 'ya':
                        data_aset[aset_id]['Status_Sertif'] = new_status
                        print(f"Status sertifikasi aset {aset_id} telah diperbarui menjadi {new_status}.")
                        return
                    
                    # Jika pengguna memilih 'Tidak', keluar dari fungsi tanpa menyimpan
                    elif simpan == 'tidak':
                        print("Data tidak disimpan.")
                        return
                    
                    # Jika input selain 'Ya' atau 'Tidak', ulangi meminta input
                    else:
                        print("Pilihan tidak valid, harap masukkan 'Ya' atau 'Tidak'.")
                        continue  # Mengulang jika input tidak valid
            else:
                print("Status sertifikasi tidak valid! Harus 'Belum' atau 'Sudah'.")
        else:
            print("Aset tidak ditemukan.")
    
    else:
        print("Anda tidak memiliki akses untuk memperbarui status sertifikasi.")

# Fungsi delete data berdasarkan key value (Delete item)
def delete_aset(role, username=None):
    if role == 'Senior Engineer' or role == 'Junior Engineer':
        # Input Asset ID yang ingin dihapus
        equipment = input_equipment()
        if equipment is None:
            return  # Keluar jika input equipment tidak valid

        # Meminta input aset_id berdasarkan equipment
        aset_id = input_aset(equipment)
        if aset_id is None:
            return  # Keluar jika input aset_id tidak valid

        # Memeriksa apakah asset_id ada dalam data_aset
        if aset_id in data_aset:
            while True:
                konfirmasi = input("\nApakah Anda ingin menghapus data ini? (Ya/Tidak): ").strip().lower()
                if konfirmasi == 'ya':
                    del data_aset[aset_id]
                    print(f"Data aset dengan ID {aset_id} berhasil dihapus.")
                    return
            
                elif konfirmasi == "tidak":
                    print(f"data {aset_id} tidak berhasil dihapus")
                    return
                else:
                    print("Pilihan tidak valid, harap masukkan 'Ya' atau 'Tidak'.")
                    continue  # Mengulang jika input tidak valid
        else:
            print("Pilihan tidak valid, data tidak dihapus.")
    else:
        print("Anda tidak memiliki akses untuk menghapus data aset.")

# Fungsi main
def main():
    while True:
        print("\n=== Sistem Manajemen Aset ===")
        print("1. Login")
        print("2. Keluar")
        pilihan = input("Masukkan pilihan: ")
        if pilihan == '1':
            username, role = login()
            if role == "Senior Engineer":
                while True:
                    print("\n=== Menu Senior ===")
                    print("1. Lihat Data Aset")
                    print("2. Tambah Data Aset")
                    print("3. Update Status Sertifikasi")
                    print("4. Hapus Data Aset")
                    print("5. Keluar")
                    menu_pilihan = input("Masukkan pilihan: ")
                    if menu_pilihan == '1':
                        read_aset(role, username)
                    elif menu_pilihan == '2':
                        create_aset(role, username)
                    elif menu_pilihan == '3':
                        update_status_sertifikasi(role, username)
                    elif menu_pilihan == '4':
                        delete_aset(role, username)
                    elif menu_pilihan == '5':
                        break
                    else:
                        print("Pilihan tidak valid.")
            elif role == "Junior Engineer":
                while True:
                    print("\n=== Menu Junior ===")
                    print("1. Lihat Data Aset")
                    print("2. Hapus Data Aset")
                    print("3. Keluar")
                    menu_pilihan = input("Masukkan pilihan: ")
                    if menu_pilihan == '1':
                        read_aset(role, username)
                    elif menu_pilihan == '2':
                        delete_aset(role, username)
                    elif menu_pilihan == '3':
                        break
                    else:
                        print("Pilihan tidak valid.")
        elif pilihan == '2':
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")
        
main()