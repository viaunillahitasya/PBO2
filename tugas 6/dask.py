import dask.bag as db
def worker(num):
    """Fungsi untuk menjalankan tugas pada proses multiprocessing"""
    print('Worker', num)
if __name__ == '__main__':
    # Buat dask bag dengan 5 item
    bag = db.from_sequence(range(5))
    # Panggil fungsi worker pada setiap item secara parallel
    bag.map(worker).compute()
