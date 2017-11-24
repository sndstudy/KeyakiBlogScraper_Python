"""
テストモジュール
"""
import unittest
from KeyakiMember import get_member_name

class TestKeyakiMember(unittest.TestCase):
    """
    KeyakiMember.py
    テストクラス
    """
    def test_get_member_name(self):
        """
        指定した値をもとにメンバーの名前を取得することを
        確認するテストケース
        """
        member_number = "33"
        return_str = "higashimura_mei"
        member_name = get_member_name(member_number)
        self.assertMultiLineEqual(return_str, member_name)

if __name__ == "__main__":
    unittest.main()
