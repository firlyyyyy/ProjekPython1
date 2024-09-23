import os
import CRUD as CRUD

# Step 2: Define the function to check if a file exists
if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print(f"{'SELAMAT DATANG DI PROGRAM':^30}")
    print(f"{'DATABASE PERRPUSTAKAAN':^30}")
    print(f"{30*'=':^30}")
    print("\n")
    
    # check database 
    CRUD.init_console()

    while True:
        match sistem_operasi:
            case "posix": os.system("clear")
            case "nt": os.system("cls")

        print(f"{'SELAMAT DATANG DI PROGRAM':^30}")
        print(f"{'DATABASE PERRPUSTAKAAN':^30}")
        print(f"{30*'=':^30}")
        print("\n")
        print("1. Read Data")
        print("2. Create Data")
        print("3. Update Data")
        print("4. Delete Data")
        print("pilih opsi (1 - 4)\n")
        userOption = input("masukkan opsi: ")
        print("\n")
        # print(f"{30*'=':^30}")
        # print("\n")
        # print(30*"=")

        match userOption:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()

        # print(f"{30*'=':^30}")
        print("\n")

        isDone = input("apakah sudah selesai? (y/n) ")
        if isDone == "y" or isDone == "Y":
            break
    print("program selesai")
