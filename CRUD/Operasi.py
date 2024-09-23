from . import Database
from .Util import random_string
import time
import os

def create_first_data():
    penulis = input("Penulis Buku: ")
    judul = input("Judul Buku: ")
    while True:
        try:
            tahun = int(input("Tahun Terbit\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Terbit harus 4 digit!")
        except:
            print("Tahun Terbit harus angka!")

    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']}, {data['date_add']}, {
        data['penulis']}, {data['judul']}, {data['tahun']}\n"
    print(data_str)
    try:
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal menulis data ke file.")


def read(**kwargs):
    try:
        with open(Database.DB_NAME, mode="r") as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs['index']-1
                if index_buku < 0 or index_buku > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:
                return content
    except:
        print("error")
        return False


def create(penulis, judul, tahun):
    data = Database.TEMPLATE.copy()

    data['pk'] = random_string(6)
    data['date_add'] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"

    try:
        with open("data.txt", "a", encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Gagal menambah data ke file.")
        

def update(no_buku, pk, date_add, penulis, judul, tahun):
    data = Database.TEMPLATE.copy()

    data['pk'] = pk
    data['date_add'] = date_add
    data['penulis'] = penulis + Database.TEMPLATE['penulis'][len(penulis):]
    data['judul'] = judul + Database.TEMPLATE['judul'][len(judul):]
    data['tahun'] = str(tahun)

    data_str = f"{data['pk']}, {data['date_add']}, {data['penulis']}, {data['judul']}, {data['tahun']}\n"
    
    data_length = len(data_str)
    
    try:
        with open(Database.DB_NAME, mode="r+") as file:
            file.seek(data_length*(no_buku-1))
            file.write(data_str)
    except:
        print("Gagal mengupdate data ke file.")
        
def delete(no_buku):
    try:
        with open(Database.DB_NAME, mode="r") as file:
            counter = 0
            while True:
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku -1:
                    pass
                else:
                    with open("file_temp.txt", mode="a", encoding="utf-8") as file_temp:
                        file_temp.write(content)
                counter += 1
    except:
        print("error")
        
    os.rename("file_temp.txt", Database.DB_NAME)
                        
