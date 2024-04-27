import main
from services import db

def add():
    kode_barang = input('\nkode barang : ')
    nama_barang = input('nama barang : ')
    harga_barang = int(input('harga barang : '))
    stok_barang = int(input('stok barang : '))

    db.insert_item(kode_barang, nama_barang, harga_barang, stok_barang)



def check():
    items = db.fetch_item()
    for item in items:
        kode_barang = item[0]
        nama_barang = item[1]
        harga_barang = item[2]
        stok_barang = item[3]
        print(f'''
kode {kode_barang}           
{nama_barang} | Rp {harga_barang}           
stok :  {stok_barang}           
''')


def start():
    while True:
        menu = int(input('\nMenu :\n1. Tambah barang\n2. Cek barang\n3. Kembali\n\nSilahkan pilih : '))
        if menu == 1:
            add()
        elif menu == 2:
            check()
        elif menu == 3:
            main.menu()
        else:
            break

if __name__ == '__main__':
    start()