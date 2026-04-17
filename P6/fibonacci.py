def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Hitung Pangkat")
        print("2. Deret Pecahan Fibonacci")
        print("0. Keluar")

        pilihan = int(input("Masukkan pilihan: "))

        if pilihan == 1:
            hitung_pangkat()
        elif pilihan == 2:
            deret_fibonacci()
        elif pilihan == 0:
            print("selesai.")
            break
        else:
            print("Pilihan tidak valid!")


def hitung_pangkat():
    bilangan = int(input("Masukkan bilangan bulat: "))
    pangkat = int(input("Masukkan pangkat: "))

    for i in range(1, pangkat + 1):
        hasil = bilangan ** i
        print(f"hasil {bilangan} pangkat {i} adalah {hasil}")


def deret_fibonacci():
    n = int(input("Masukkan jumlah n: "))

    # buat deret fibonacci
    fib = [1, 1]
    for i in range(2, n * 2):  # cukup panjang untuk pembilang & penyebut
        fib.append(fib[i-1] + fib[i-2])

    hasil = 0
    tanda = 1  # +1 untuk +, -1 untuk -

    print("Deret: ", end="")

    for i in range(n):
        pembilang = fib[2 * i]
        penyebut = fib[2 * i + 1]

        if i == 0:
            print(f"{pembilang}", end="")
            hasil += pembilang
        else:
            if tanda == 1:
                print(f" + {pembilang}/{penyebut}", end="")
                hasil += pembilang / penyebut
            else:
                print(f" - {pembilang}/{penyebut}", end="")
                hasil -= pembilang / penyebut

        tanda *= -1  # ganti tanda + jadi - dan sebaliknya

    print("\nHasil =", hasil)


menu()