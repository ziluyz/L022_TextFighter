import hero
import weapons
import random
import time

available_weapons = [weapons.Bare_hands(), weapons.Sword(), weapons.Bow(), weapons.Lightning()]
available_armor = [weapons.Bare_skin(), weapons.Large_shield(), weapons.Small_shield(), weapons.Magic_dome()]

class Game:
    def __init__(self) -> None:
        self.heroes = [hero.Hero(True), hero.Hero(False)]

    def show_stats(self) -> None:
        print (f'\nPlayer | {self.heroes[0].get_name()} (COMPUTER)\t|\tPlayer 2 - {self.heroes[1].get_name() } (YOU)')
        print ('-------|------------------------|-------------------------')
        print (f'Health | \t{self.heroes[0].get_health()}\t\t|\t{self.heroes[1].get_health()}')
        print (f'Attack | \t{self.heroes[0].get_attack_power()}\t\t|\t{self.heroes[1].get_attack_power()}')
        print (f'Weapon | \t{self.heroes[0].get_weapon().get_name()}\t|\t{self.heroes[1].get_weapon().get_name()}')
        print (f'Armour | \t{self.heroes[0].get_armor().get_name()}\t|\t{self.heroes[1].get_armor().get_name()}')
        print ('-------|------------------------|-------------------------\n')

    def get_answer(self, hero: hero.Hero_abstract, length: int) -> int:
        if hero.is_computer():
            return random.randint(1, length)
        while True:
            try:
                answer = int(input("Your choice: "))
                if answer > 0 and answer <= length:
                    return answer
            except ValueError:
                pass

    def make_action(self, hero: hero.Hero_abstract, enemy: hero.Hero_abstract, action: int) -> None:
        if action == 1:
            print("Available weapons:")
            for i, weapon in enumerate(available_weapons, start=1):
                print(f'{i}. {weapon.get_name()}')
            print()
            hero.change_weapon(available_weapons[self.get_answer(hero, len(available_weapons)) - 1])
        elif action == 2:
            print("Available armor:")
            for i, armor in enumerate(available_armor, start=1):
                print(f'{i}. {armor.get_name()}')
            print()
            hero.change_armor(available_armor[self.get_answer(hero, len(available_armor)) - 1])
        elif action == 3:
            hero.attack(enemy)
        
    def start(self) -> None:
        round = 0
        human_wins = 0
        while round < 3:
            round += 1
            print (f'\n---====Round {round}!====---\n')
            for hero in self.heroes:
                hero.regenerate()
            previous_action = 0
            round_ended = False
            while not round_ended:
                for hero in self.heroes:
                    enemy = [enemy for enemy in self.heroes if enemy != hero][0]
                    self.show_stats()
                    if not hero.is_alive():
                        print(f'{hero.get_name()} is dead!\n')
                        if hero.is_computer():
                            human_wins += 1
                        round_ended = True
                        break
                    print(f"\n{hero.get_name()}'s turn\n")
                    print ('1. Change weapon\n2. Change defence\n3. Attack\n4. Quit game\n')
                    action = self.get_answer(hero, 4)
                    if hero.is_computer():
                        if action == 4:
                            action = 3
                        elif action in [1, 2] and action == previous_action:
                            action = 3
                        previous_action = action
                    elif action == 4:
                        return
                    self.make_action(hero, enemy, action)
                    time.sleep(1)
                
        print(f'Score: {human_wins} (YOU) - {3 - human_wins} (COMPUTER)')
        if human_wins > 2:
            print('YOU WIN!')
        else:
            print('YOU LOSE!')