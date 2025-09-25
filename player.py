from random import randint
import time

player = {
    "health": 0,
    "armor": 100,
    "damage": 10,
    "gold": 0,
    "size_inventory": 5,
}

enemy = {
    "health": 100,
    "armor": 100,
    "damage": 10,
    "gold": 0,
    "size_inventory": 5,
}


def get_gold():
    if player["gold"] == 0:
        random_gold = randint(1, 100)
        player["gold"] += random_gold
        print(
            f"Игрок получил: {random_gold} золота. Сейчас у него {player['gold']} золота.\n"
        )
    elif player["gold"] >= 42:
        random_gold = randint(37, 456)
        player["gold"] += random_gold
        print(
            f"Игрок получил: {random_gold} золота. Сейчас у него {player['gold']} золота.\n"
        )
    elif player["gold"] >= 498:
        random_gold = randint(0, 2753)
        player["gold"] += random_gold
        print(
            f"Игрок получил: {random_gold} золота. Сейчас у него {player['gold']} золота.\n"
        )
    else:
        random_gold = randint(0, 10)
        player["gold"] += random_gold
        print(
            f"Игрок получил: {random_gold} золота. Сейчас у него {player['gold']} золота.\n"
        )


def heal(*, person_dict: dict):
    while person_dict["health"] < 100:
        person_dict["health"] += 5
        time.sleep(0.5)
        print(f"Игрок восстановил 1 хп. Сейчас у него {person_dict['health']} хп.")
    print(f"Игрок восстановился. Сейчас у него {person_dict['health']} хп.\n")


def repair_armor(*, person_dict: dict):
    while person_dict["armor"] < 100:
        person_dict["armor"] += 10
        time.sleep(0.5)
        print(f"Игрок восстановил 1 броню. Сейчас у него {person_dict['armor']} едbниц брони.")
    print(f"Игрок восстановился. Сейчас у него {person_dict['armor']} единиц брони.\n")


def get_damage(*, person_dict: dict, enemy_dict: dict):  # с каждым уменьшением брони будет наноситься больше урона
    total_damage = 0
    # if person_dict['health'] == 0:
    #     return 'Игрок уже мертв. Он не может получить урон'
    #
    # elif person_dict['health'] < enemy_dict['damage']:
    #     person_dict['health'] = 0
    #     return person_dict
    #
    #     total_damage = enemy_dict['damage'] * (1 - (person_dict['armor'] / 100))
    # elif person_dict['health'] == 0:
    #     return 'Игрок уже мертв. Он не может получить урон'
    # elif total_damage <= 0:
    #     total_damage = 1
    #     person_dict['armor'] -= 10
    #     person_dict['health'] -= total_damage

    # итоговый урон = базовый урон врага × (1 – (броня получающего урон / 100))
    pass


get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
get_damage(person_dict=player, enemy_dict=enemy)
print(player["health"])
