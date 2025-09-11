import globals
def shop(player, fightInventory, weapons):
    shop = {}
    print("Willkommen in der Kampfarena. Hier kaufst du Ausrüstung für den Kampf. Währung sind deine eigenen Leben. Die Aurüstung bleibt in der Arena, d.h. was übrig bleibt, landet nicht in deinem Inventar.")
    print("Gewinst du den Kampf, werden deine leben wieder zurückgesetzt, und du bekommst eine Belohnung. Verlierst du den kampf allerdings, verlierst du 10 Leben außerhalb der Arena.")
    print("Tippe einfach den namen ein, und beende deinen Eimkauf mit 'ende'\n")

    # --- Print items--- #

    for weapon in weapons:
        print(f"{weapon.type}: {weapon.name} (-{weapon.price} Leben) \n{weapon.info}\n")
        shop[weapon.name.lower().strip()] = weapon.price

    while (item := input(f"{globals.COLOR_INPUT}>").lower().strip()) != "ende":
        print(f"{globals.COLOR_RESET}")
        if item == "verteidigung":
            defence = next((weapon for weapon in weapons if weapon.name.lower().strip() == "verteidigung"), None)
            if defence.counter > 0:
                defence.counter -= 1
                player.lives -= shop[item]
                fightInventory.append(item)
                print("Du hast noch: " + str(player.lives) + " leben")
            else:
                print("Du hast schon die maximale ausrüstung für deine Verteidigung")
        # Wenn man Items schon im shop begrenzen will: (aktuell wird gegner immun; haltbarkeit macht kein sinn)
        # i = [weapon for weapon in weapons if weapon.name.lower().strip() == item]
        # if i.counter != None:
        #   i.counter -= 1
        # if item in shop and i.counter > 0:
        #   player.lives -= shop[item]
        #   fightInventory.append(item)
        #   print("item nichtmehr verfügbar")
        elif item in shop:
            player.lives -= shop[item]
            fightInventory.append(item)
            print("Du hast noch: " + str(player.lives) + " leben")
        else:
            print("Diesen Artikel haben wir nicht im Angebot")
    print(f"{globals.COLOR_RESET}")

def choose(inventory):
    print(f"Wähle 1-2 Items aus deinem {globals.COLOR_NOUN}Inventar{globals.COLOR_RESET} aus, die du nutzen möchtest. Wenn du 2 gleiche Angriffe auswählst, machst du automatisch einen Sepzialangriff. Dieser macht zwar mehr schaden, raubt dir allerdings 10 Leben.")
    print("Wenn du nur 1 Item verwenden willst, tippe beim 2. angriff 'none' ein.")

    # --- First Item --- #

    while (first := input(f"{globals.COLOR_INPUT}1. Angriff: ").lower().strip()) not in inventory.items or inventory.items[first] <= 0 or first == "ausweichmanöver":
        print(f"{globals.COLOR_RESET}")
        print("ungültig")
    if not first == "kick":
        inventory.remove(first)
    print(f"{globals.COLOR_RESET}")
    inventory.print_inventory()

    # --- Second Item --- #

    while (bonus := input(f"{globals.COLOR_INPUT}2. Angriff: ").lower().strip()) != "none" and bonus not in inventory.items or bonus == "ausweichmanöver":
        print(f"{globals.COLOR_RESET}")
        print("ungültig")
    if not bonus == "kick":
        inventory.remove(bonus)
    print(f"{globals.COLOR_RESET}")
    inventory.print_inventory()

    round = [first, bonus]

    return round, inventory