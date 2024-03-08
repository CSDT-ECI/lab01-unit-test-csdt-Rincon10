from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual  

def test_YatzyRuleAllDiceHaveTheSameNumberThenGetScore50():
        dice = [1,1,1,1,1]
        expected = 50
        actual = Yatzy.yatzy(dice)

        assert expected == actual

def test_YatzyRuleExistsAnDiferentDiceThenGetScore0():
        dice = [1,1,1,2,1]
        expected = 0
        actual = Yatzy.yatzy(dice)

        assert expected == actual