import threading
def worker(num):
    """Fungsi untuk menjalankan tugas pada thread baru"""
    print('Worker', num)
if __name__ == '__main__':
    # Membuat list untuk menyimpan setiap thread
    threads = []
    # Memulai setiap thread dengan menggunakan threading.Thread
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)
# Menunggu thread selesai
for t in threads:
    t.join()