from random import randint
import time


player = {
    "health": 100,
    "armor": 10,
    "damage": 5,
    "gold": 0,
    "size_inventory": 5,
}


enemy = {
    "health": 100,
    "armor": 10,
    "damage": 2,
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
    while person_dict["health"] < 20:
        person_dict["health"] += 5
        time.sleep(0.5)
        print(f"Игрок востановил 1 хп. Сейчас у него {person_dict['health']} хп.")
    print(f"Игрок восстановился. Сейчас у него {person_dict['health']} хп.\n")
    
    
def repair_armor(*, person_dict: dict):
    while person_dict["armor"] < 10:
        person_dict["armor"] += 1
        time.sleep(0.5)
        print(f"Игрок востановил 1 броню. Сейчас у него {person_dict['armor']} единиц брони.")
    print(f"Игрок восстановился. Сейчас у него {person_dict['armor']} единиц брони.\n")
    
    
def get_damage(*, person_dict: dict, dict_enemy: dict):  #с каждмы уменшением бронии будет наносится больше урона
    while person_dict['health'] > 0:
        pass


heal(person_dict=player)
repair_armor(person_dict=player)