#!/usr/bin/env python3

from PIL import Image
from PIL.ExifTags import TAGS
import glob


def get_exif_of_image(file):
    """Get EXIF of an image if exists.

    指定した画像のEXIFデータを取り出す関数
    @return exif_table Exif データを格納した辞書
    """
    im = Image.open(file)

    # Exif データを取得
    # 存在しなければそのまま終了 空の辞書を返す
    try:
        exif = im._getexif()
    except AttributeError:
        return {}

    # タグIDそのままでは人が読めないのでデコードして
    # テーブルに格納する
    exif_table = {}
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exif_table[tag] = value

    return exif_table

# print (get_exif_of_image("img/IMG_7714.jpg"))

def get_date_of_image(file):
    """Get date date of an image if exists

    指定した画像の Exif データのうち日付データを取り出す関数
    @return yyyy:mm:dd HH:MM:SS 形式の文字列
    """

    # get_exif_of_imageの戻り値のうち
    # 日付データのみを取得して返す
    exif_table = get_exif_of_image(file)
    return exif_table.get("DateTimeOriginal")

file_path = glob.glob("img/*.jpg")
for f in file_path:
    print (get_date_of_image(f))
# => yyyy:mm:dd HH:MM:DD 形式の文字列
#    Exif データが存在しない場合は None
