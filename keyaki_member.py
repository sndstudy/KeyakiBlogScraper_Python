"""
欅坂のメンバーを定義するモジュール
"""
MEMBER_LIST = {"01":"ishimori_nijika",
               "02":"imaizumi_yui",
               "03":"uemura_rina",
               "04":"ozeki_rika",
               "05":"oda_nana",
               "06":"koike_minami",
               "07":"kobayashi_yui",
               "08":"saitou_fuyuka",
               "09":"satou_shiori",
               "10":"shida_manaka",
               "11":"sugai_yuuka",
               "12":"suzumoto_miyu",
               "13":"nagasawa_nanako",
               "14":"habu_miduho",
               "15":"harada_aoi",
               "17":"hirate_yurina",
               "18":"moriya_akane",
               "19":"yonetani_nanami",
               "20":"watanabe_rika",
               "21":"watanabe_risa",
               "22":"nagahama_neru",
               "23":"iguchi_mao",
               "24":"ushio_sarina",
               "25":"kakizaki_memi",
               "26":"kageyama_yuuka",
               "27":"katou_shiho",
               "28":"saitou_kyouko",
               "29":"sasaki_kumi",
               "30":"sasaki_mirei",
               "31":"takase_mana",
               "32":"takamoto_ayaka",
               "33":"higashimura_mei",
               "1000":"hiragana2"}

def get_member_name(member_num):
    """
    欅坂のメンバー名を取得する関数
    引数:2桁の数字(公式ブログでのメンバーページ)
    戻り値:リストに存在した場合はそれに紐づくメンバー名を返却。
    無い場合は米さんの名前を返却。
    """
    return MEMBER_LIST.get(member_num, MEMBER_LIST.get("19"))

def check_member_number(member_num):
    """
    公式ブログのメンバーページにある数字かチェックする関数
    引数:2桁の数字(公式ブログでのメンバーページ)
    戻り値:リストに存在する数字であればそのまま返却。
    無い場合は米さんのメンバー数字（19）を返却。
    """
    if member_num in MEMBER_LIST:
        return member_num
    else:
        return "19"
