import json

def check_comma_space(s: str) -> bool:
    return ", " in s
guests = ""
list_guest = []

while True:
    print("Пригласим гостей на вечеринку. Напиши кого ты бы хотел пригласить! (Напрмиер: Андрей, Василий, Петр. Обязательно через \", \")")
    guests = input("Кого бы пригласил:")
    print(f"Ты пригласил \"{guests}\", давай отправим приглашение.\n")
    
    list_guests = guests.split(", ")
    len_guests = len(list_guests)
    
    if len_guests > 1:
        if not check_comma_space(guests):
            print("Ошибка: Слова должны быть разделены через \", \"")
            continue
        
    guests_or_guest = ""
    if len_guests == 1 or 0:
        guests_or_guest = "гость"
    else:
        guests_or_guest = "гостей"
    
    print(f"Ты пригласил {len_guests} {guests_or_guest}.\n")
    
    if len_guests > 1:
        print("dsa")
    
    for guest in list_guests:
        print(f"Привет {guest}, приглашаю тебя на вечеринку!")
    break

print(guests, list_guests)
with open("files/list_guests.json", "w", encoding='utf-8') as f:
    json.dump(list_guests, f, ensure_ascii=False, indent=4)