import math

# 인벤토리 클래스 입니다.-----------------------------
inventory = {"회복물약": 0, "완전회복물약": 0, "공격물약": 0, "속도물약": 0}


class Inventory():
    def __init__(self, item):
        self.item = item
    # 아이템을 구매하는 코드

    def addItem(self, item):
        if item in inventory:
            inventory[item] += 1
            print(f"\033[32m{item} 구매를 완료하였습니다!\033[0m")
        # 올바른 값을 입력하지 않은 경우
        else:
            print(f"\033[32m{item} 를 찾을 수 없습니다.\033[0m")
    # 현재 가지고 있는 인벤토리를 확인하는 코드

    def removeItem(self, item):
        if item in inventory:
            inventory[item] -= 1
            print(f"\033[32m{item} 를 사용하였습니다.\033[0m")

    def showInventory(self):
        print("\033[33m================= 현재인벤토리 =================\n\033[0m")
        for item in inventory:
            if inventory[item] > 0:
                print(f"\033[32m{item} x {inventory[item]}\033[0m")
        if inventory[item] == 0:
            print(f"\033[91m인벤토리가 비어있습니다.\033[0m\n")
        print("\033[33m============================================\n\033[0m")


# 얍
# 도저언~
# 가보자구~
player_inventory = Inventory('item')


# Inventory.addItem("회복물약")시 회복물약 추가

# 게임머니 클래스


class Currency:
    def __init__(self, money):
        self.money = money

    def add_money(self, money):
        self.money += money

    def sub_money(self, money):
        self.money += money

    def remove_money(self, money):
        if self.money < money:
            # 물품대비 돈이 부족할 경우(value가 없는 오류가 발생)
            raise ValueError("\033[33m골드가 부족합니다.\033[0m")
        self.money -= money

    def show_money(self):
        return self.money


my_money = Currency(100)  # 0골드을 가진 화폐 객체 생성

# my_money.add_money(5)  # 5골드 추가
# my_money.remove_money(3)  #3골드 빼기
# print(my_money.money)  # 5골드 출력

# 포션 클래스
# other는 Character(player)
#


class Potion:
    def __init__(self, other):
        self.half_recovery_potion = min(
            other.hp + other.max_hp*0.5, other.max_hp)
        self.full_recovery_potion = other.max_hp
        self.attack_potion = math.ceil(other.power*1.1)
        self.speed_potion = math.ceil(other.speed*1.1)
        # 필담 좋네요! :)

    def use(self, other):
        while True:
            print(f"어떤 물약을 사용 하시겠습니까? \n"
                  f"\033[91m1. 50% 회복물약\033[0m \n"
                  f"\033[31m2. 완전 회복물약\033[0m \n"
                  f"\033[30m3. 공격 물약\033[0m \n"
                  f"\033[34m4. 속도물약\033[0m \n"
                  f"\033[37m5. 그만 사용하기\033[0m")

            # use_potion = int(input())로 받아서 활용합니다.
            use_potion = input(">>    ")
            if use_potion == "1":
                other.hp = min(
                    round(other.hp + other.max_hp*0.5), other.max_hp)
                player_inventory.removeItem("회복물약")
                print(f"{other.name}의 hp가 50% 회복됐습니다.")

            elif use_potion == "2":
                other.hp = other.max_hp
                player_inventory.removeItem("완전회복물약")
                print(f"{other.name}의 hp가 완전히 회복됐습니다.")

            elif use_potion == "3":
                other.power = math.ceil(other.power*1.1)
                player_inventory.removeItem("공격물약")
                print(f"{other.name}의 공격력이 10% 상승합니다.")

            elif use_potion == "4":
                other.speed = math.ceil(other.speed*1.1)
                player_inventory.removeItem("속도물약")
                print(f"{other.name}의 속도가 10% 상승합니다.")

            elif not use_potion.isdigit():
                print("숫자로만 입력해 주세요.")
            elif use_potion == "5":
                break
            else:
                print("잘못된 선택입니다. 다시 선택 하세요")
                continue

# 1.=half_recovery_potion
# 2.=full_recovery_potion
# 3.=attack_potion
# 4.=speed_potion


# 상점 이용 함수입니다.-----------------------------


def shop():
    potion = ["회복물약", "완전회복물약", "공격물약", "속도물약"]

    print("\033[35m상점에 진입했습니다.\n상점을 이용 하시겠습니다?\033[0m")
    print("1. 상점 이용하기 2. 다음층으로 이동하기")
    ans = int(input(">>"))
    if ans == 1:
        while True:
            print(inventory)   #
            print(f"현재 가진 금액 : {my_money.money}골드")
            print(f"구입하려는 번호를 입력한 다음 Enter키를 누르세요. \n"
                  f"1. 50% 회복물약 - 10gold \n"
                  f"2. 완전회복물약 - 17gold \n"
                  f"3. 공격 물약 - 30gold \n"
                  f"4. 속도 물약 - 30gold ")
            buy_potion()
            break
    elif ans == 2:
        pass
    elif ans.isdigit() == False:
        print('숫자로만 입력해주세요.')
    elif int(ans) < 1 or int(ans) > 2:
        print("1 또는 2 중에서 선택해주세요.\n")


# 물품 구매 함수 -------------------
def buy_potion():
    potion_list = [
        {"name": "회복물약", "effect": "체력을 50% 증가", "price": 10},
        {"name": "완전회복물약", "effect": "체력을 100% 증가", "price": 17},
        {"name": "공격물약", "effect": "공격력을 10% 증가", "price": 30},
        {"name": "속도물약", "effect": "속도를 10% 증가", "price": 30},
    ]
    buy_choice = input(">>")
    while True:
        a = int(buy_choice) - 1
        print(
            f"{potion_list[a]['name']}은 {potion_list[a]['effect']}시켜줍니다. 구매하시겠습니까?")
        print("1.예 2.아니오(상점으로 돌아가기)")
        buy_ans = int(input(">>"))
        if buy_ans == 1:
            player_inventory.addItem(potion_list[a]["name"])
            my_money.remove_money(potion_list[a]["price"])
            print(f"상점으로 돌아가시겠습니까?\n"
                  f"1.상점으로 돌아가기 2.탑으로 이동하기")
            shop_ans = input(">>")
            if shop_ans == "1":
                break
            elif shop_ans.isdigit() == False:
                print(f'\033[32m숫자로만 입력해주세요.\033[0m')
            elif int(shop_ans) < 1 or int(shop_ans) > 2:
                print("1 또는 2 중에서 선택해주세요.\n")
            elif shop_ans == "2":
                print('탑으로 이동 중 ---')
                break
        elif buy_ans == 2:
            break
        elif buy_ans.isdigit() == False:
            print('숫자로만 입력해주세요.')
        elif int(buy_ans) < 1 or int(buy_ans) > 2:
            print("1 또는 2 중에서 선택해주세요.\n")
            continue

# m = list(monster_dic.items())
# print(m[0][1])


# def battle1(floor, monsters):
#     while True:
#         print(f'{monsters}"이 나타났다!\n')
#         player.show_status()
#         monster_level_1.show_status()
#         aa = int(input('어떤 행동을 하시겠습니까?\n1.일반공격 2.마법공격 3.인벤토리 4.포기한다\n>>    '))
#         if aa == 1:
#             player.normal_attack(monster_level_1)
#             if monster_level_1.hp > 0:  # 선공 후 몹이 살아있을때
#                 monster_level_1.normal_attack(player)
#                 player.show_status()
#                 monster_level_1.show_status()
#             elif monster_level_1.hp <= 0:  # 선공 후 몹이 죽었을때
#                 print(f'{monster_level_1.name}을 처치했다!')
#                 break
