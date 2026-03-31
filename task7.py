def curse(weapon_damage):
    lesser_cursed = weapon_damage * 0.5   
    greater_cursed = weapon_damage * 0.25 
    return lesser_cursed, greater_cursed
    

def test(weapon_damage):
    print("Базовый урон оружия:", float(weapon_damage))
    print("Накладываем проклятие...")
    lesser_cursed, greater_cursed = curse(weapon_damage)
    print("С малым проклятием урон:", float(lesser_cursed), "ед.")
    print("С большим проклятием урон:", float(greater_cursed), "ед.")
    print("=====================================")


def main():
    test(100)
    test(500)
    test(1000)


main()