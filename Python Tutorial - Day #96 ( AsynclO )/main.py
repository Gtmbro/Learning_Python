import asyncio
import requests
    
async def image_downloader(url, name):
    response = requests.get(url)
    with open(f"{name}.jpg",'wb') as f:
        f.write(response.content)
    return (f"{name}.jpg is downloaded.")

def urls_taker():
    while True:
        try:
            number = int(input("How many images do u wanna download? "))
            if number <=0:
                print("Enter a positive number.. ")
                continue
        except ValueError:
            print("Invalid input..")

        images_list = []
        for _ in range(1, number+1):
            url = input("Enter url of image: ")
            name = input("Enter the name: ")
            images_list.append([url,name])

        return images_list

async def main():
    images_list = urls_taker()
    tasks = [image_downloader(*pair) for pair in images_list]
    L = await asyncio.gather(*tasks)
    for i in L:
        print(i)

asyncio.run(main())   
