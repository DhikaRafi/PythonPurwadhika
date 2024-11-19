from tabulate import tabulate
import sys
import maskpass


listvespa = [
    ["Sprint 20v", 10, 32000000, 2020, "3v"],
    ["Sprint S 19i", 5, 45000000, 2019, "iget"],
    ["Gts 21v", 2, 60000000, 2021, "3v"],
    ["Primavera 22v", 15, 27000000, 2022, "3v"],
    ["Lx 22v", 20, 25000000, 2022, "3v"],
    ["S 22i", 20, 25000000, 2022, "iget"],
]

# submenu ubah info
def ubahharga():
    while True:
        try:
            nama_vespa = input('Masukkan nama Vespa yang harganya ingin diganti (Kosongkan bila ingin kembali ke sub menu): ').capitalize()
            
            # Jika input nama Vespa kosong
            if not nama_vespa.strip():
                print('''
===============================
    Kembali ke Sub Menu...
===============================
                ''')
                mengganti_info_vespa()
            
            # Cari Vespa berdasarkan nama
            vespa_index = None
            for i in range(len(listvespa)):
                if listvespa[i][0] == nama_vespa:
                    vespa_index = i
                    break
                            
            if vespa_index is not None:
                print(f'''
Vespa yang harganya ingin Anda ubah adalah Vespa {listvespa[vespa_index][0]} tahun {listvespa[vespa_index][3]} Jenis mesin {listvespa[vespa_index][4]} 
Yang memiliki harga {listvespa[vespa_index][2]}
                ''')
                harga_baru = int(input("Ganti harga unit Vespa menjadi: Rp. ")) 
                konfirmasigantiharga = input('Apa Anda yakin ingin mengganti harga unit ini? (Y/N) ').upper()
                if konfirmasigantiharga == 'Y': 
                    listvespa[vespa_index][2] = harga_baru
                    print(f"Harga baru unit Vespa menjadi: Rp. {harga_baru}")
                    read_semua_vespa()
                    mengganti_info_vespa()
                elif konfirmasigantiharga == 'N':
                    inginbalikkesubmenu = input('''
===========================
    Balik ke Sub Menu?
        ( Y / N )   
===========================                                                 
                                            ''').upper()
                    if inginbalikkesubmenu == 'Y':
                        mengganti_info_vespa()
                    elif inginbalikkesubmenu == 'N':
                        ubahharga()
                    else:
                        print('''
===========================
    INVALID INPUT ! ! !    
===========================
                          
                      ''')
                    
                else:
                    print('''
===========================
    INVALID INPUT ! ! !    
===========================
                          
                      ''')
            else:
                print(f'''
=====================================================
  Nama Vespa "{nama_vespa}" tidak ditemukan! Coba lagi
=====================================================
                ''')
                mengganti_info_vespa()
            
        except ValueError:
            print('''
==================================                 
                  
    INPUT HARGA YANG VALID!             
                  
==================================                 
                  ''')

def ubahstok():
    while True:
        try:
            nama_vespa = input('Masukkan nama Vespa yang stoknya ingin diganti (Kosongkan bila ingin kembali ke sub menu): ').capitalize()

            # Jika input nama Vespa kosong
            if not nama_vespa.strip():
                print('''
===============================
    Kembali ke Sub Menu...
===============================
                ''')
                mengganti_info_vespa()

            # Cari Vespa berdasarkan nama menggunakan for loop
            vespa_index = None
            for i in range(len(listvespa)):
                if listvespa[i][0] == nama_vespa:
                    vespa_index = i
                    break

            if vespa_index is not None:
                print(f'''
Vespa yang stoknya ingin Anda ubah adalah {listvespa[vespa_index][0]} tahun {listvespa[vespa_index][3]} 
Jenis mesin {listvespa[vespa_index][4]} dengan stok saat ini {listvespa[vespa_index][1]}.
                ''')
                stok_baru = int(input("Ganti stok unit Vespa menjadi: ")) 
                konfirmasigantistok = input('Apakah Anda yakin ingin mengganti stok unit ini? (Y/N): ').upper()
                if konfirmasigantistok == 'Y':
                    listvespa[vespa_index][1] = stok_baru
                    print(f"Stok unit Vespa {listvespa[vespa_index][0]} berhasil diubah menjadi: {stok_baru}")
                    read_semua_vespa()
                    mengganti_info_vespa()
                    
                elif konfirmasigantistok == 'N':
                    inginbalikkesubmenu = input('''
===========================
    Balik ke Sub Menu?
        ( Y / N )   
===========================                                                 
                                            ''').upper()
                    if inginbalikkesubmenu == 'Y':
                        mengganti_info_vespa()
                    elif inginbalikkesubmenu == 'N':
                        ubahstok()
                    else:
                        print('''
===========================
    INVALID INPUT ! ! !    
===========================
                          
                      ''')
            else:
                print(f'''
===========================================================
   Nama Vespa "{nama_vespa}" tidak ditemukan! Coba lagi.
===========================================================
                ''')
                mengganti_info_vespa()

        except ValueError:
            print('''
=================================================                 
                  
    Masukkan angka stok yang valid!             
                  
=================================================                 
                  ''')

##submenu tambah
def yakintambahlagi():
    while True:
        konfirmasitambahlagi = input('Apakah Anda ingin menambah unit lagi? (Y/N)').upper()
        if konfirmasitambahlagi == 'Y':
            tambahunit()
        elif konfirmasitambahlagi == 'N':
            menambah_vespa()
        else:
            print('''
==========================
    
    INPUT Y atau N !!!

========================== 
                            
                            ''')            

def validasiduplikatunit(nama_baru):
    for i in listvespa:
        if i[0] == nama_baru:
            return True
    return False

def tambahunit():
    # Input nama Vespa
    nama_baru = input("Masukkan nama Vespa: ").capitalize()
    if validasiduplikatunit(nama_baru):
        print('''
========================
    Unit Sudah Ada
========================                              
                          ''')
        return tambahunit()  # Kembali ke awal fungsi jika unit sudah ada

    # Input stok Vespa
    while True:
        try:
            stock_baru = int(input("Masukkan stok Vespa: "))
            if stock_baru < 0:
                print('''
===========================
    STOK INVALID ! ! !
===========================                
              ''')
                continue
            break
        except ValueError:
            print('''
========================================
    Input stok harus berupa angka! ! !
========================================                
              ''')

    # Input harga Vespa
    while True:
        try:
            harga_baru = int(input("Masukkan harga Vespa: "))
            if harga_baru < 0:
                print('''
=========================================
    Harga harus di atas Rp. 0 ! ! !
=========================================                  
              ''')
                continue
            break
        except ValueError:
            print('''
========================================
    Input harga harus berupa angka! ! !
========================================                
              ''')

    # Input tahun Vespa
    while True:
        try:
            tahun_baru = int(input("Masukkan tahun Vespa: "))
            if tahun_baru < 1600:
                print('''
============================              
    Tahun Invalid ! ! !
============================              
              ''')
                continue
            break
        except ValueError:
            print('''
========================================
    Input tahun harus berupa angka! ! !
========================================                
              ''')

    # Input jenis mesin Vespa
    jenis_mesin_baru = input("Masukkan jenis mesin Vespa: ").lower()

    # Konfirmasi penambahan unit
    konfirmasitambah = input('Apa Anda yakin ingin menambahkan unit tersebut? (Y/N) ').upper()
    if konfirmasitambah == 'Y':
        listvespa.append([nama_baru, stock_baru, harga_baru, tahun_baru, jenis_mesin_baru])
        print(f"\n{nama_baru} berhasil ditambahkan ke daftar Vespa.")
        read_semua_vespa()
        yakintambahlagi()
    elif konfirmasitambah == 'N':
        menambah_vespa()
    else:
        print('''
=====================
 
 INPUT Y atau N !!!
 
===================== 
                           
                          ''')
        tambahunit()


#submenu hapus
def hapusunit():
    while True:
        try:
            nama_vespa = input('Masukkan nama Vespa yang ingin dihapus: ')

            # Cari Vespa berdasarkan nama menggunakan for loop
            vespa_index = None
            for i in range(len(listvespa)):
                if listvespa[i][0] == nama_vespa:
                    vespa_index = i
                    break

            if vespa_index is not None:
                print(f'''
Vespa yang ingin Anda hapus adalah {listvespa[vespa_index][0]} tahun {listvespa[vespa_index][3]} 
Jenis mesin {listvespa[vespa_index][4]} dengan stok {listvespa[vespa_index][1]} dan harga Rp. {listvespa[vespa_index][2]:,}.
                ''')
                validasi_hapus = input('Apakah Anda yakin ingin menghapus data tersebut? (Y/N): ').upper()
                if validasi_hapus == 'Y':
                    print(f'Unit {listvespa[vespa_index][0]} berhasil dihapus!')
                    del listvespa[vespa_index]
                    read_semua_vespa()
                    menghapus_vespa()
                elif validasi_hapus == 'N':
                    print('''
====================
 Unit batal dihapus
====================''')
                    menghapus_vespa()
                else:
                    print('''
===================
 Invalid Input !!!
=================== 
                      ''')
            else:
                print(f'''
===============================
   Nama Vespa "{nama_vespa}" tidak ditemukan! Coba lagi.
===============================
                ''')
                menghapus_vespa()

        except ValueError:
            print('''
====================
  INVALID INPUT !!! 
====================                  
                  ''')

#submenu Read
def read_semua_vespa():
    if len(listvespa)==0:
        print('''
==========================================

    TIDAK ADA STOK DALAM GUDANG ! ! ! 
    
==========================================
                 
              ''')
        
    else:
        headers = ["Nomor", "Nama", "Stok", "Harga (Rp)", "Tahun", "Jenis Mesin"]
        table = [[i + 1, vespa[0], vespa[1], f"Rp. {vespa[2]:,}", vespa[3], vespa[4]] for i, vespa in enumerate(listvespa)]
        print("\nDaftar Vespa:\n")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid", colalign=("center", "left", "center", "right", "center", "center")))

def read_dari_nama():
    try:
        nama_vespa = input("Masukkan nama Vespa yang ingin ditampilkan: ").capitalize()

        # Cari Vespa berdasarkan nama menggunakan for loop
        vespa_index = None
        for i in range(len(listvespa)):
            if listvespa[i][0] == nama_vespa:
                vespa_index = i
                break

        if vespa_index is not None:  # Jika Vespa ditemukan
            vespa = listvespa[vespa_index]
            
            # Menyiapkan data untuk ditampilkan dalam tabel
            headers = ["Nama", "Stok", "Harga (Rp)", "Tahun", "Jenis Mesin"]
            table = [[vespa[0], vespa[1], f"Rp. {vespa[2]:,}", vespa[3], vespa[4]]]

            # Menampilkan detail Vespa dalam format tabel
            print(f"\n{tabulate(table, headers=headers, tablefmt='fancy_grid', colalign=('center', 'center', 'right', 'center', 'center'))}\n")
        else:  # Jika nama Vespa tidak ditemukan
            print(f'''
============================================================
   Nama Vespa "{nama_vespa}" tidak ditemukan! Coba lagi.
============================================================
                        ''')
            menampilkan_daftar_vespa()

    except ValueError:
        print('''
===============================
   Terjadi kesalahan input! 
===============================
        ''')

def sortharga():
    try:
        pilihan = int(input('''
========================================
                Sort Harga
 1. Dari termurah ke termahal
 2. Dari termahal ke termurah
 3. Kembali ke Menu Melihat Daftar Vespa
========================================                                           
Pilih opsi (1/2/3): '''))
        
        if pilihan == 3:  # Kembali ke menu Melihat Daftar Vespa
            print('''
======================================================

    Kembali ke Menu Melihat Daftar Vespa . . . 
    
======================================================                      
                  
                  ''')
            menampilkan_daftar_vespa()
            return  # Menghentikan eksekusi fungsi sortharga setelah kembali

        if pilihan not in [1, 2]:
            print('''
==============================
        INVALID INPUT 
    Masukkan 1 - 3 ! ! !
==============================
            ''')
            sortharga()  # Meminta input ulang jika input tidak valid
            return

        # Salin data listvespa untuk sorting lokal
        list_vespa_sorted = listvespa.copy()

        # Bubble Sort
        n = len(list_vespa_sorted)
        for i in range(n):
            for j in range(0, n-i-1):
                # Sorting berdasarkan kolom harga (index 2)
                if (pilihan == 1 and list_vespa_sorted[j][2] > list_vespa_sorted[j+1][2]) or \
                   (pilihan == 2 and list_vespa_sorted[j][2] < list_vespa_sorted[j+1][2]):
                    list_vespa_sorted[j], list_vespa_sorted[j+1] = list_vespa_sorted[j+1], list_vespa_sorted[j]

        # Tampilkan hasil sorting lokal
        headers = ["Nomor", "Nama Unit", "Stok", "Harga (Rp)", "Tahun", "Jenis Mesin"]
        table = [[i + 1, vespa[0], vespa[1], f"Rp. {vespa[2]:,}", vespa[3], vespa[4]] for i, vespa in enumerate(list_vespa_sorted)]
        print("\nDaftar Vespa (Hasil Sortir):\n")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid", colalign=("center", "left", "center", "right", "center", "center")))

        # Kembali ke menu sortharga
        sortharga()
        
    except ValueError:
        print('''
===============================
     Masukkan Angka Valid!
===============================
        ''')
        sortharga()

def sorttahun():
    try:
        pilihan = int(input('''
========================================
                Sort Tahun
 1. Dari tahun terbaru ke terlama
 2. Dari tahun terlama ke terbaru
 3. Kembali ke Menu Melihat Daftar Vespa
========================================                                           
Pilih opsi (1/2/3): '''))
        
        if pilihan == 3:  # Kembali ke menu Melihat Daftar Vespa
            print('''
======================================================

    Kembali ke Menu Melihat Daftar Vespa . . . 
    
======================================================                      
                  
                  ''')
            menampilkan_daftar_vespa()
            return  # Menghentikan eksekusi fungsi sorttahun setelah kembali

        if pilihan not in [1, 2]:
            print('''
======================================
    INVALID INPUT! Masukkan 1/2/3
======================================
            ''')
            return

        # Salin data listvespa untuk sorting lokal
        list_vespa_sorted = listvespa.copy()

        # Bubble Sort
        n = len(list_vespa_sorted)
        for i in range(n):
            for j in range(0, n-i-1):
                # Sorting berdasarkan kolom tahun (index 3)
                if (pilihan == 1 and list_vespa_sorted[j][3] < list_vespa_sorted[j+1][3]) or \
                   (pilihan == 2 and list_vespa_sorted[j][3] > list_vespa_sorted[j+1][3]):
                    list_vespa_sorted[j], list_vespa_sorted[j+1] = list_vespa_sorted[j+1], list_vespa_sorted[j]

        # Tampilkan hasil sorting lokal
        headers = ["Nomor", "Nama Unit", "Stok", "Harga (Rp)", "Tahun", "Jenis Mesin"]
        table = [[i + 1, vespa[0], vespa[1], f"Rp. {vespa[2]:,}", vespa[3], vespa[4]] for i, vespa in enumerate(list_vespa_sorted)]
        print("\nDaftar Vespa (Hasil Sortir Berdasarkan Tahun):\n")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid", colalign=("center", "left", "center", "right", "center", "center")))

        # Kembali ke menu sorttahun
        sorttahun()
        
    except ValueError:
        print('''
===============================
     Masukkan Angka Valid!
===============================
        ''')
        sorttahun()

#Main Option
def menampilkan_daftar_vespa():
    while True:
        try:
            menu_options = [
                ["1", "Menampilkan Semua Daftar Vespa"],
                ["2", "Menampilkan Unit Spesifik"],
                ["3", "Mengurutkan Unit Sesuai Harga"],
                ["4", "Mengurutkan Unit Sesuai Tahun"],
                ["5", "Main Menu"]
            ]
            
            # Menampilkan menu dalam format tabel
            print(tabulate(menu_options, headers=["No", "Opsi"], tablefmt="fancy_grid", numalign="center"))
            
            inputmenuread = int(input("Pilih submenu (1/3/4/5): "))
            
            if inputmenuread == 1:
                read_semua_vespa()
                
            elif inputmenuread == 2:
                read_semua_vespa()
                read_dari_nama()
            
            elif inputmenuread == 3:
                sortharga()
            
            elif inputmenuread == 4:
                sorttahun()
                
            elif inputmenuread == 5:
                main_menu()
            
            else:
                print('''
======================================                     
    Angka yang dimasukkan salah!!!
     Pilihlah angka 1/2/3/4/5
======================================    
''')    

        except ValueError:
            print('''
====================================                     
    Inputlah angka 1/2/3/4/5 !!!
====================================                    
                  ''')
                               
def menambah_vespa():
    while True:
        try:
            menu_options = [
                ["1", "Menambahkan Unit Vespa"],
                ["2", "Main Menu"]
            ]
            
            # Menampilkan menu dalam format tabel
            print(tabulate(menu_options, headers=["No", "Opsi"], tablefmt="fancy_grid", numalign="center"))
            
            menutambahvespa = int(input("Pilihlah sub menu (1-2): "))
            
            if menutambahvespa == 1:
                read_semua_vespa()
                tambahunit()
            
            elif menutambahvespa == 2:
                main_menu()
                
            else:
                print('''
================================                     
       INVALID INPUT ! ! !
================================    
''')
            
        except ValueError:
            print('''
===================================                     
    Inputlah angka 1 atau 2 !!!
===================================                    
                  ''')

def menghapus_vespa():
    while True:
        try:
            menu_options = [
                ["1", "Menghapus Unit Vespa"],
                ["2", "Main Menu"]
            ]
            
            # Menampilkan menu dalam format tabel
            print(tabulate(menu_options, headers=["No", "Opsi"], tablefmt="fancy_grid", numalign="center"))
            
            menuhapusvespa = int(input("Pilihlah submenu (1-2): "))
            
            if menuhapusvespa == 1:
                read_semua_vespa()
                hapusunit()
                
            elif menuhapusvespa == 2:
                print('''
=========================================

    Kembali Ke Main Menu . . . . . . 

=========================================                       
                      ''')
                main_menu()
                
            else:
                print('''
===============================

    Input Angka 1 - 2 ! ! !
    
===============================                      
                      ''')

        except ValueError:
            print('''
===================================                     
    Inputlah angka 1 atau 2 !!!
===================================                    
                  ''')

def mengganti_info_vespa():
    while True:
        try:
            # Menampilkan menu menggunakan tabulate untuk format tabel
            menu_data = [
                [1, "Mengganti Harga Vespa"],
                [2, "Mengganti Stok Vespa"],
                [3, "Main Menu"]
            ]

            print(tabulate(menu_data, headers=["No", "Opsi"], tablefmt="fancy_grid", colalign=("center", "left")))

            inputmenugantiharga = int(input('\nPilihlah submenu (1/2/3): '))
            
            if inputmenugantiharga == 1:
                read_semua_vespa()
                ubahharga()
                
            elif inputmenugantiharga == 2:
                read_semua_vespa()
                ubahstok()
                
            elif inputmenugantiharga == 3:
                print('''
=========================================

    Kembali Ke Main Menu . . . . . . 

=========================================                       
                      ''')
                main_menu()
                
            else:
                print('''
==================================

    Input Angka (1/2/3) ! ! !
    
==================================                      
                      ''')

        except ValueError:
            print('''
===========================

    INVALID INPUT ! ! !
    
===========================    

                  ''')

def main_menu():
    while True:
        menu_options = [
            ["1", "Menampilkan Daftar Vespa"],
            ["2", "Menambah Vespa"],
            ["3", "Menghapus Vespa"],
            ["4", "Mengganti Detail Vespa"],
            ["5", "Log Out"]
        ]
        print('''
              _                                 
  /\/\   __ _(_)_ __     /\/\   ___ _ __  _   _ 
 /    \ / _` | | '_ \   /    \ / _ | '_ \| | | |
/ /\/\ | (_| | | | | | / /\/\ |  __| | | | |_| |
\/    \/\__,_|_|_| |_| \/    \/\___|_| |_|\__,_|           
              ''')

        print(tabulate(menu_options, headers=["Nomor", "Deskripsi"], tablefmt="fancy_grid",colalign=("center", "left")))
        
        pilihan = input("Masukkan angka Menu yang ingin dijalankan (1/2/3/4/5): ")  # Meminta input dari user

        if pilihan == '1':  # Menampilkan Daftar Vespa
            menampilkan_daftar_vespa()

        elif pilihan == '2':  # Menambah Vespa
            menambah_vespa()

        elif pilihan == '3':  # Menghapus Vespa
            menghapus_vespa()
            
        elif pilihan == '4':
            mengganti_info_vespa()
            
        elif pilihan == '5':
            print('''
===================================
                 
        Logging Out . . . 

===================================    
                  ''')
            startmenu()
        
        else:
            print('''
=======================================

    Masukkan Angka 1/2/3/4/5 ! ! !
    
=======================================                      
                  ''') 

def login():
    menu_login = [
        [" ========================== Menu Login =========================="],
        ["Masukkan username dan password"],
        ["Kosongkan  username dan password bila ingin kembali ke start menu"]
    ]
    print(tabulate(menu_login, tablefmt="fancy_grid"))

    username = input("Masukkan username: ").strip()
    password = maskpass.askpass(prompt='\nMasukan Password : ', mask='*').strip()

    # Cek jika username atau password kosong
    if not username or not password:
        print('''
==============================
  Username dan password kosong!
  Kembali ke menu utama...
==============================
        ''')
        startmenu()

    # Validasi username dan password
    if username == "admin" and password == "admin123":
        print("\nLogin berhasil!\n")
        main_menu()
    else:
        print('''
==============================
Username atau password salah.
==============================
        ''')
        login()

def startmenu():
    startingmenu = input('''
==========================                         
        Start Menu
==========================
    1. Login
    2. Exit Program
==========================          
Masukkan menu yang ingin dijalankan (1/2): ''')
    if startingmenu == '1':
        login()
    elif startingmenu == '2':
        print('''
=================================
    Keluar Dari Program . . . 
=================================              
              
              ''')
        sys.exit()
    else:
        print('''
=======================
    Pilih 1 atau 2
=======================              
              ''')
        startmenu()
    
startmenu()

