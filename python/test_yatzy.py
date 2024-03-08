from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual  

def test_ChanceRuleShouldReturnTheSumOfAllDice():
        dice = [1,1,3,3,6]
        expected = 14
        actual = Yatzy.chance(dice[0],dice[1],dice[2],dice[3],dice[4])

        assert expected == actual

def test_YatzyRuleAllDiceHaveTheSameNumberThenGet50Points():
        dice = [1,1,1,1,1]
        expected = 50
        actual = Yatzy.yatzy(dice)

        assert expected == actual

def test_YatzyRuleExistsAtLeastOneDifferentDiceThenGet0Points():
        dice = [1,1,1,2,1]
        expected = 0
        actual = Yatzy.yatzy(dice)

        assert expected == actual

def test_PairsRuleShouldGet0PointsForAllDifferentDice():
        dice = [1,2,3,4,5]
        expected = 0
        actual = Yatzy.score_pair(dice[0],dice[1],dice[2],dice[3],dice[4])

        assert expected == actual


def test_CrazyChangeRuleMixedValuesOddAndNotOdds():
        dice = [2,4,6,2,2]
        expected = 48
        actual = Yatzy.crazy_chance(dice)
        
        assert expected == actual

def test_CrazyChangeAllOdds():
        dice = [1,1,3,5,5]
        expected = 30
        actual = Yatzy.crazy_chance(dice)
        
        assert expected == actual

