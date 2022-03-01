import unittest
import main


class TestMain(unittest.TestCase):

    def test_pale_ple(self):

        self.assertEqual(main.one_away(
            string_one="pale", string_two="ple"), True)

    def test_pale_palest(self):

        self.assertEqual(main.one_away(
            string_one="pale", string_two="palest"), False)

    def test_pale_pa(self):

        self.assertEqual(main.one_away(
            string_one="pale", string_two="pa"), False)

    def test_pa_pale(self):
        self.assertEqual(main.one_away(
            string_one="pa", string_two="pale"), False)

    def test_pale_bale(self):
        self.assertEqual(main.one_away(
            string_one="pale", string_two="bale"), True)

    def test_pale_bane(self):

        self.assertEqual(main.one_away(
            string_one="pale", string_two="bane"), False)


    def test_pales_pale(self):

        self.assertEqual(main.one_away(
            string_one="pales", string_two="pale"), True)

    def test_pale_bake(self):

        self.assertEqual(main.one_away(
            string_one="pale", string_two="bake"), False)

    def test_pale_ble(self):

        self.assertEqual(main.one_away(
            string_one="pale", string_two="ble"), False)

    def test_aaaa_aaa(self):

        self.assertEqual(main.one_away(
            string_one="aaaa", string_two="aaa"), True)

    def test_aaaa_aab(self):
# if shortest not in longest
        self.assertEqual(main.one_away(
            string_one="aaaa", string_two="aab"), False)

    def test_pale_pals(self):

        self.assertEqual(main.one_away(
            string_one="pale", string_two="pals"), True)
        

    #there need to be a lot more tests


