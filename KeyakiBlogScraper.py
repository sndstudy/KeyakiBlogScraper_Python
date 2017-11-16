"""
欅坂の公式ブログから画像を取得するモジュール
"""
import urllib.request
import urllib.error
import os
import datetime
import KeyakiMember
from bs4 import BeautifulSoup

def create_directory(directory_name):
    """
    create_directory関数
    ディレクトリが既に存在している場合は何もしない
    """
    if not os.path.isdir("./img/" + directory_name):
        os.makedirs("./img/" + directory_name)

def get_today_datetime():
    """
    get_today_datetime関数
    今日の日時をYYYYMMDDhhmmで取得する
    """
    today = datetime.datetime.today()

    return  str(today.year)+str(today.month)+str(today.day)+str(today.hour)+str(today.minute)


def main():
    """
    main関数
    """
    member_num_str = "250"

    member_num_str = KeyakiMember.check_member_number(member_num_str)

    # アクセスするURL(欅坂の公式ブログのURL)
    url = "http://www.keyakizaka46.com/s/k46o/diary/member/list?ima=0000&ct=" + member_num_str

    # URLにアクセスする htmlが帰ってくる
    html = urllib.request.urlopen(url)

    # htmlをBeautifulSoupで扱う
    soup = BeautifulSoup(html, "html.parser")

    member_name = KeyakiMember.get_member_name(member_num_str)

    create_directory(member_name)

    # 個人ブログ最新記事内のimgタグを取得する
    img_tags = soup.find("div", class_="box-article").find_all("img")

    img_cnt = 0
    today_str = get_today_datetime()

    for img_tag in img_tags:
        img_src = img_tag.get("src")
        urllib.request.urlretrieve(img_src, "./img/" + member_name +  "/" +
                                   today_str + member_name + str(img_cnt) + ".jpg")
        img_cnt += 1

main()
