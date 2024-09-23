from . import Operasi

DB_NAME = "data.txt"
TEMPLATE = {
    "pk":"XXXXXX",
    "data_add":"yyyy-mm-dd",
    "penulis":255*" ",
    "judul":255*" ",
    "tahun":"yyyy"
}

def init_console():
    try:
        with open(DB_NAME, mode="r") as file:
            print("database tersedia, init selesai!")
    except:
        print("database tidak ditemukan, silahkan membuat database!")
        # with open(DB_NAME, mode="w", encoding="utf-8") as file:
        #     penulis = input("Penulis Buku: ")
        #     judul = input("Judul Buku: ")
        #     tahun = input("Tahun Terbit: ")
        Operasi.create_first_data()