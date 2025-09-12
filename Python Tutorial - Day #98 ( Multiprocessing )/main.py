import time
import requests
from multiprocessing import Process

def downloader(url, name):
    print("Download has started..")
    time.sleep(2)
    response = requests.get(url)
    open(f"deleter/{name}.jpg",'wb').write(response.content)
    print("Download has finished..")

if __name__ == "__main__":
    url = "https://picsum.photos/200/300"

    processes = []
    for i in range(10):
        m = Process(target=downloader, args=(url, i))
        m.start()
        processes.append(m)

    for p in processes:
        p.join()
