import io
import requests
import PIL.Image
import os
import standardise_images


def download_images(folder_path, file_name, url):
    try:
        r = requests.get(url)
        image_content = r.content

    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

    try:
        image_file = io.BytesIO(image_content)
        image = PIL.Image.open(image_file).convert('RGB')
        standardise_images.resizeImages(image)
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'wb') as f:
            image.save(f, "JPEG", quality=85)
        print(f"SUCCESS - saved {url} - as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not save {url} - {e}")
