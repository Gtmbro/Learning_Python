import requests
from concurrent.futures import ThreadPoolExecutor

def images_collecter():
    while True:
        try:
            n = int(input("How many images to download? "))
            if n<=0:
                print("Enter positive value..")
                continue
        
        except ValueError:
            print("Value Error!!")
            continue

        images_list = []
        for _ in range(n):
            url = input("Enter the url: ")
            name = input("Enter the name: ")
            images_list.append([url, name])

        return images_list

def image_downloader(image):
    # for img in image:
    #     url = img[0]
    #     name = img[1]
    url, name = image
    response = requests.get(url)
    with open(f"{name}.jpg",'wb') as f:
        f.write(response.content)
    return ("Succesfully downloaded..")

def main():
    images_list = images_collecter()
    with ThreadPoolExecutor() as executor:
        results = executor.map(image_downloader, images_list)
        for result in results:
            print(result)

main()
