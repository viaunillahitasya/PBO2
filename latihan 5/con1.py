try:
    my_list = [1, 2, 3]
    my_list.remove(4)
except ValueError:
    print("Error: Elemen tidak ada di dalam list!")

try:
    # Buka file dan baca isinya
    with open('file.txt', 'r') as file:
        data = file.read()

    # Ubah teks menjadi bilangan bulat
    num = int(data)

    # Bagi dengan angka yang diinputkan oleh user
    divisor = int(input("Masukkan angka pembagi: "))
    result = num / divisor

    # Tampilkan hasil bagi
    print("Hasil bagi adalah:", result)

# Tangani beberapa jenis exception
except FileNotFoundError:
    print("File tidak ditemukan!")
except ValueError:
    print("Isi file harus berupa bilangan bulat!")
except ZeroDivisionError:
    print("Angka pembagi tidak boleh nol!")
except Exception as e:
    print("Terjadi kesalahan:", str(e))


    