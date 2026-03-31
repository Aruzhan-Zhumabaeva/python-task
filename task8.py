def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage * 2
    new_health = target_health - enchanted_damage
    enchanted_weapon = "enchanted " + weapon
    return enchanted_weapon, new_health


def test(target_health, damage, weapon):
    print(f"У цели {target_health} здоровья.")
    print(f"Базовый урон оружия {weapon}: {damage}... Зачаровываем и атакуем.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"Цель была атакована оружием: {enchanted_weapon}.")
    print(f"У цели осталось {new_health} здоровья.")
    print("=====================================")


def main():
    test(100, 50, "sword")
    test(500, 100, "axe")
    test(1000, 250, "bow")


main()