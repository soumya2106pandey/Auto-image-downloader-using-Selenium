import os
from selenium import webdriver
import download_images
import fetch_data


def save_images_locally(query, dest_dir, total_imgs, driver):
    for name in list(query):
        path = os.path.join(dest_dir, name)
        if not os.path.isdir(path):
            os.mkdir(path)
        print('Current Path', path)
        total_links = fetch_data.get_images_from_net(name, total_imgs, driver)

        if total_links is None:
            print('images not found for :', name)
            continue
        else:
            for i, link in enumerate(total_links):
                file_name = f"{i:150}.jpg"
                download_images.download_images(path, file_name, link)


PATH = "D:\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
searchNames = ['Car']
destDir = "D:\\TestImages"
totalImgs = 5

save_images_locally(searchNames, destDir, totalImgs, driver)
