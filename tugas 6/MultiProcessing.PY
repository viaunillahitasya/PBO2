import multiprocessing
def worker(num):
    """Fungsi untuk menjalankan tugas pada proses baru"""
    print('Worker', num)
if __name__ == '__main__':
# Membuat objek Process sebanyak 5
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()
# Menunggu proses selesai
    for p in processes:
        p.join()