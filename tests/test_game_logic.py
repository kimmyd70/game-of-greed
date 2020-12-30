from game_of_greed import __version__
from game_of_greed.game_logic import GameLogic, Banker
roll_dice = GameLogic.roll_dice


# passes
def test_version():
    assert __version__ == '0.1.0'

##### 18 required tests #####

### Testing - Roll Dice
# When rolling 1 to 6 dice ensure…

# 1) A sequence of correct length is returned

# passes: generates correct length
def test_roll_dice_length():
    actual = len(roll_dice(4))
    expected = 4
    assert actual == expected
    
# 2) Each item in sequence is an integer with value between 1 and 6
# passes: broken into separate verifications
def test_roll_dice_int():
    our_tuple = roll_dice(4)
    result = 'types'
    for item in range (0,4):
        result = f'{result} : {type(our_tuple[item])}'
    actual = result
    expected = "types : <class 'int'> : <class 'int'> : <class 'int'> : <class 'int'>" 
    assert actual == expected
    
def test_roll_dice_range():
    our_second_tuple = roll_dice(4)
    result = 'result:'
    for item in range (0,4):
        if 1 <= our_second_tuple[item] <= 6:
            result = f'{result} Ok'
            
    actual = result
    expected = "result: Ok Ok Ok Ok" 
    assert actual == expected


### Testing - Calculate Score

# 3)  zilch - non scoring roll should return 0
# 4)  ones - rolls with various number of 1s should return correct score
# 5)  twos - rolls with various number of 2s should return correct score
# 6)  threes - rolls with various number of 3s should return correct score
# 7)  fours - rolls with various number of 4s should return correct score
# 8)  fives - rolls with various number of 5s should return correct score
# 9)  sixes - rolls with various number of 6s should return correct score
# 10) straight - 1,2,3,4,5,6 should return correct score
# 11) three_pairs - 3 pairs should return correct score
# 12) two_trios - 2 sets of 3 should return correct score
# 13) leftover_ones - 1s not used in set of 3 (or greater) should return correct score
# 14) leftover_fives - 5s not used in set of 3 (or greater) should return correct score

### Testing - Banker

# 15) shelf: should properly track unbanked points
# 16) bank:should properly add unbanked points to total and return the deposited amount
# 17) clear_shelf: should remove any unbanked points, resetting to zero.
# 18) clear_shelf: should not affect previously banked points