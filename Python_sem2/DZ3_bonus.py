from DZ3_account import card
def add_bonus():
    BONUSSUM = card.BALANCE * card.BONUSRATE
    card.BALANCE += card.BALANCE * card.BONUSRATE
    print(f'начислен бонус {BONUSSUM}')
