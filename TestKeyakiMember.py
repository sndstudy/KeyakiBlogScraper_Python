import unittest
from KeyakiMember import get_member_name

class TestKeyakiMember(unittest.TestCase):

    def test_get_member_name(self):
        member_number = "33"
        return_str = "higashimura_mei"
        member_name = get_member_name(member_number)
        self.assertMultiLineEqual(return_str, member_name)

if __name__ == "__main__":
    unittest.main()
