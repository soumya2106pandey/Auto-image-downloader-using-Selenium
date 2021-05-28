import time


def get_images_from_net(query, max_images, wd):
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"
    image_search_url = search_url.format(q=query)

    wd.get(image_search_url)

    image_urls = set()
    image_count = 0
    start = 0

    while image_count < max_images:
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wd.implicitly_wait(5)

        thumbnail_results = wd.find_elements_by_xpath("//img[contains(@class,'rg_i Q4LuWd')]")
        total_results = len(thumbnail_results)

        for thumbnail in thumbnail_results[start:total_results]:
            try:
                thumbnail.click()
                time.sleep(2)
                images = wd.find_elements_by_css_selector('img.n3VNCb')
                for image in images:
                    if image.get_attribute('src') and 'https' in image.get_attribute('src'):
                        image_urls.add(image.get_attribute('src'))
                image_count = len(image_urls)
            except Exception as e:
                print(e)
            if image_count >= max_images:
                break
            else:
                show_more_results_button = wd.find_element_by_css_selector(".mye4qd")
                wd.execute_script("document.querySelector('.mye4qd').click();")
                start = len(thumbnail_results)

    return image_urls
