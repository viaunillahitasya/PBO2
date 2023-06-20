import subprocess
def worker(num):
    """Fungsi untuk menjalankan tugas pada proses baru"""
    print('Worker', num)
if __name__ == '__main__':
# Membuat list untuk menyimpan setiap proses
    processes = []
# Memulai setiap proses dengan menggunakan subprocess.Popen
    for i in range(5):
        p = subprocess.Popen(['python', '-c', 'import multiprocessing; ''multiprocessing.Process(target=worker,args=('+str(i)+',)).start()'],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        processes.append(p)
# Menunggu proses selesai dan mendapatkan output dari setiap proses
    for p in processes:
        out, err = p.communicate()
        print(out.decode('utf-8'), err.decode('utf-8'))