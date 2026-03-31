def triple_attack(damage_one, damage_two, damage_three):
    return damage_one + damage_two + damage_three

attack_one = 2
attack_two = 4 
attack_three = 3

first_triple_attack_damage = triple_attack(attack_one, attack_two, attack_three)

print(attack_one, attack_two, attack_three)
print(first_triple_attack_damage)
print("====================================")


attack_four = -1
attack_five = 10
attack_six = 5

sekond_triple_attack_damage = triple_attack(attack_four,attack_five, attack_six)

print(attack_four, attack_five, attack_six)
print(sekond_triple_attack_damage)
print("=====================================")