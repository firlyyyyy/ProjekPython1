from .Operasi import read, create, update, delete


def read_console():
    data_file = read()

    index = "No"
    penulis = "Penulis"
    judul = "Judul"
    tahun = "Tahun"

    # ==> Header
    print(f"\n{100*'=':^100}")
    print(f"{index:4} | {penulis:40} | {judul:40} | {tahun:10}")
    print(f"{100*'-':^100}")

    # ==> Data
    for index, data in enumerate(data_file, 1):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index:4} | {penulis:.40} | {judul:.40} | {tahun:10}")

    # ==> Footer
    print(f"{100*'=':^100}\n")


def create_console():
    print(f"\n{30*'=':^30}")
    print(f"{'Masukkan Buku Baru':^30}")
    print(f"{30*'=':^30}\n")

    penulis = input("Penulis Buku\t: ")
    judul = input("Judul Buku\t: ")
    while True:
        try:
            tahun = int(input("Tahun Terbit\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun Terbit harus 4 digit!")
        except:
            print("Tahun Terbit harus angka!")

    create(penulis, judul, tahun)
    # print("data yang udah dibuat")
    read_console()


def update_console():
    read_console()

    while True:
        print(f"\n{50*'=':^50}")
        print(f"{'Pilih Buku Yang Mau Di Update':^50}")
        print(f"{50*'=':^50}\n")
        no_buku = int(input("Masukkan no buku yang mau di update\t: "))
        data_buku = read(index=no_buku)
        # print(data_buku)

        if data_buku:
            break
        else:
            print(
                "nomor buku tidak tersedia, masukkan kembali nomor buku yang ada di dalam tabel")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while True:
        # ==> data yang mau di update
        print(f"\n{50*'=':^50}")
        print(f"{'Data Apa Yang Mau Di Ubah':^50}")
        print(f"{50*'=':^50}\n")
        print(f"1. Penulis Buku\t: {penulis:.40}")
        print(f"2. Judul Buku\t: {judul:.40}")
        print(f"3. Tahun Terbit\t: {tahun:4}\n")

        # ==> pilihan update
        user_option = input("masukkan nomor data yang mau di ubah\t: ")
        print(f"{50*'-':^50}\n")

        match user_option:
            case "1": penulis = input("Penulis Buku\t: ")
            case "2": judul = input("Judul Buku\t: ")
            case "3":
                while True:
                    try:
                        tahun = int(input("Tahun Terbit\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun Terbit harus 4 digit!")
                    except:
                        print("Tahun Terbit harus angka!")
                    break
            case _: print("Pilihan tidak ada, silakan pilih kembali!")

        isDone = input("apakah sudah selesai? (y/n) ")
        if isDone == "y" or isDone == "Y":
            break

    update(no_buku, pk, date_add, penulis, judul, tahun)


def delete_console():
    read_console()

    while True:
        print(f"\n{50*'=':^50}")
        print(f"{'Pilih Buku Yang Mau Di Delete':^50}")
        print(f"{50*'=':^50}\n")
        no_buku = int(input("Masukkan no buku yang mau di delete\t: "))
        data_buku = read(index=no_buku)
        # print(data_buku)

        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]
            

            # ==> data yang mau di update
            print(f"\n{50*'=':^50}")
            print(f"{'Data Apa Yang Mau Di Hapus':^50}")
            print(f"{50*'=':^50}\n")
            print(f"1. Penulis Buku\t: {penulis:.40}")
            print(f"2. Judul Buku\t: {judul:.40}")
            print(f"3. Tahun Terbit\t: {tahun:4}\n")
        
        isDone = input("apakah yakin untuk di hapus? (y/n) ")
        if isDone == "y" or isDone == "Y":
            delete(no_buku)
            break        
        else:
            print(
                "nomor buku tidak tersedia, masukkan kembali nomor buku yang ada di dalam tabel")

    print("data berhasil di hapus")
