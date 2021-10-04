import os
import pathlib
import urllib.parse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm


def main():
    URL = input_url()
    OUT_PATH = "./extracted_images/"

    if not os.path.exists(OUT_PATH):
        os.makedirs(OUT_PATH)

    res = requests.get(URL)
    soup = BeautifulSoup(res.text, "html.parser")

    images_elems = soup.find_all("image")
    image_urls = [urllib.parse.urljoin(URL, u.get("href")) for u in images_elems]

    for i, image_url in enumerate(tqdm(image_urls), start=1):
        FILE_PATH = pathlib.Path(OUT_PATH, str(i) + pathlib.Path(image_url).suffix)

        res = requests.get(image_url, timeout=5)
        with open(FILE_PATH, "wb") as f:
            f.write(res.content)


def input_url():
    print("URLを入力してください。空の場合は既定値が適用されます。\n"
        "(既定値: http://localhost:8080/)")

    while True:
        input_url = input("URL: ")

        # 空なら既定値をセットする。
        if not input_url:
            input_url = "http://localhost:8080/"

        # index.htmlが含まれていたら削除する。
        if input_url[-10:] == "index.html":
            input_url = input_url[:-10]

        # 有効なURLか判定する。
        try:
            if requests.get(input_url).status_code == 200:
                break
            else:
                print("指定されたURLにアクセスできません。")
        except Exception:
            print("URLの形式を満たしていません。")

    return input_url

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception:
        print("[異常終了]")
    finally:
        import subprocess
        subprocess.call('PAUSE', shell=True)
