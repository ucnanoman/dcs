import unittest
from parse import loads


class TestNumber(unittest.TestCase):

    def test_integer(self):
        r = loads("int = 3")
        self.assertEqual(r, {"int": 3})

        r = loads("int = 193984")
        self.assertEqual(r, {"int": 193984})

        r = loads("int = -23")
        self.assertEqual(r, {"int": -23})

    def test_decimal(self):
        r = loads("dec = 666.6")
        self.assertEqual(r, {"dec": 666.6})

    def test_object(self):
        luas = """
mission=
{
    ["trig"]=
    {
    },

    ["coalitions"]=
    {
        ["blue"]=
        {
            [1]=11,
            [2]=4,
            [3]=6
        }
    }, -- end of ["coalitions"]
    ["maxDictId"]=18,
    ["descriptionBlueTask"]="DictKey_descriptionBlueTask_3"
}
"""
        ref = {'mission': {
            'coalitions': {'blue': [11.0, 4.0, 6.0]},
            'descriptionBlueTask': 'DictKey_descriptionBlueTask_3',
            'trig': {},
            'maxDictId': 18.0}}
        r = loads(luas)
        self.assertEqual(r, ref)

    def test_syntaxerr(self):
        with self.assertRaises(SyntaxError):
            loads("""m=
            {
                ["x"] 12
            }""")


if __name__ == '__main__':
    unittest.main()
