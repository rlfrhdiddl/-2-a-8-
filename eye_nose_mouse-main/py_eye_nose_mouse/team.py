# from random import randint, random

import random
# import os
# import time
# - 규칙
#     - 협업을 위해 코드 컨벤션을 정해야 합니다.
#     - 기능별로 파일을 나눠 작업해야 합니다.
#     - 함수, 클래스를 사용해 중복된 코드 사용을 최소화해야 합니다.
# - 기능
#     - 플레이어의 직업이 있고 직업별 특수 능력이 있어야 합니다.
#           - 계열 : 모험가(5+n), 레지스탕스(5+n), 시그너스(5+n)
#           - 특수능력 : 직업별로 기술?(전사,도적,법사,궁수)추가
# 모체니깐 기본만다넣기


class Monster():
    def __init__(self, name, hp, power, speed, normal_attack_name):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.power = power
        self.speed = speed
        self.normal_attack_name = normal_attack_name

    def normal_attack(self, target):  # 일반공격
        m_damage = random.randint(self.power-5, self.power+5)
        target.hp = max(target.hp - m_damage, 0)
        print(
            f"{self.name}의 {self.normal_attack_name}! {target.name}에게 {m_damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f"\033[33m================={self.name}의 상태정보=====================\n"
              f"{self.name}의 상태: HP {self.hp}/{self.max_hp}\n"
              f"========================================================\033[0m")


class Character():  # 전직시 normal_attack
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.max_hp = hp
        self.max_mp = mp
        self.power = power  # 고정값?줄까요?
        self.speed = speed
        self.critical = critical
        # self.normal_attack_name = self.power * randint(1, self.power * 10)
        self.normal_attack_name = normal_attack_name
        self.level = level

    def attack_box(self, target):
        active = int(input('공격선택 일반공격(1)'))
        if active == 1:
            self.normal_attack(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 1:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def normal_attack(self, target):  # 일반공격
        damage = random.randint(self.power*2, self.power*3)
        target.hp = max(target.hp - damage, 0)
        print(
            f"{self.name}의 {self.normal_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================={self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 나는 배짱이 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f'========================================================\033[0m')


#           # 모험가
#               - 2연타 가능(맞은데 또 맞아라!)


class Adventurer_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 마법공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("마나가 부족하여 마법공격을 할 수 없습니다.")

    def Adventurer_Skill(self, target):
        self.magic_attack_name = print(f'맞은데 또 맞아라!')
        magic_name = '맞은데 또 맞아라!'
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의\033[32m {magic_name}발동!\033[0m {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
        # 노말어택 2번나가기

    def show_status(self):
        print(f'\033[33m================={self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 나는 배짱이 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f'========================================================\033[0m')


class Magician_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 마법공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("마나가 부족하여 마법공격을 할 수 없습니다.")

    def Magician_Skill(self, target):
        self.magic_attack_name = print(f'6,000만 볼트 뇌룡')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
        # 노말어택 2번나가기

    def show_status(self):
        print(f'\033[33m================={self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 나는 배짱이 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f'========================================================\033[0m')

#               - 법사(썬,콜) 디버프(Monster def 감소)


# class Magician_Character(Adventurer_Character):
#     def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
#         super().__init__(self, name, hp, mp, power,
#                          speed, critical, normal_attack_name, level)

#     def Magician_Skill(self, target):
#         self.magic_attack_name = print(f'6,000만 볼트 뇌룡')
#         damage = random.randint(self.power*1, self.power*2)
#         target.hp -= damage*2
#         print(
#             f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
#         if target.hp == 0:
#             print(f"{target.name}이(가) 쓰러졌습니다.")

#               - 전사(파이터)

class Warrior_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 일반공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("마나가 부족하여 마법공격을 할 수 없습니다.")

    def Warrior_Skill(self, target):
        self.magic_attack_name = print(f'천본앵경엄(せんぼんざくらかげよし)')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
        # 노말어택 2번나가기

    def show_status(self):
        print(f'\033[33m================={self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 나는 배짱이 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f'========================================================\033[0m')


#               - 도적(나이트로드) 회피율(Player speed 증가)

class Thief_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 일반공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("마나가 부족하여 마법공격을 할 수 없습니다.")

    def Thief_Skill(self, target):
        self.magic_attack_name = print(f'나선환!(らせんがん)!')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")
        # 노말어택 2번나가기

    def show_status(self):
        print(f'\033[33m================={self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 나는 배짱이 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f'========================================================\033[0m')


#               - 궁수(보우마스터) 명중율에따른 치명타확률 (critical)

class Archer_Character(Character):
    def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name):
        super().__init__(name, hp, mp, power, speed,
                         critical, normal_attack_name, level)
        self.magic_attack_name = magic_attack_name

    def attack_box(self, target):
        active = int(input('공격선택 :\n 일반공격(1) \n 마법공격(2)'))
        if active == 1:
            self.normal_attack(target)
        elif active == 2:
            self.Adventurer_Skill(target)
        elif not active.isdigit():
            print("숫자로만 입력해 주세요.")
        elif active < 0 or active > 2:
            print(f'\033[91m잘못된선택입니다.\033[0m')

    def magic_attack(self, target):  # 일반공격
        if self.mp >= 10:
            damage = random.randint(self.power*2, self.power*3)
            self.mp -= 10
            target.hp = max(target.hp - damage, 0)
            print(
                f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
            if target.hp == 0:
                print(f"{target.name}이(가) 쓰러졌습니다.")
        else:
            # 마나가 부족할 경우
            print("마나가 부족하여 마법공격을 할 수 없습니다.")

    def Archer_Skill(self, target):
        self.magic_attack_name = print(f'하일리히 프파일 (Heilig Pfeil)')
        damage = random.randint(self.power*1, self.power*2)
        target.hp = max(target.hp - damage*2, 0)
        print(
            f"{self.name}의 {self.magic_attack_name}! {target.name}에게 {damage}의 데미지를 입혔습니다.")
        if target.hp == 0:
            print(f"{target.name}이(가) 쓰러졌습니다.")

    def show_status(self):
        print(f'\033[33m================={self.name}의 상태정보=====================\n'
              f"{self.name}의 HP: {self.hp}/{self.max_hp}\n"
              f"{self.name}의 MP: {self.mp}/{self.max_mp}\n"
              f"{self.name}의 LEVEL: {self.level}\n"
              f"{self.name}의 직업 : 나는 배짱이 \n"
              f"{self.name}의 공격력 : {self.power}\n"
              f"{self.name}의 속도 : {self.speed}\n"
              f'========================================================\033[0m')

#               - 법사(플레임위자드) 디버프(Monster def 감소)
#               - 전사(소울마스터) 신체강화(power 증가)
#               - 도적(나이트워커) 회피율(Player speed 증가)
#               - 궁수(윈드브레이커) 명중율에따른 치명타확률 (critical)
#           # 직업군 버프
#           = 모험가
#               - 2연타 가능(맞은데 또 맞아라!)

#           # 레벨업, 보상(골드, 아이템)
#               - 레벨상승
#               - 보상(골드, 아이템) 분배


# 게임 시작
# class Character():  # 전직시 normal_attack
#     def __init__(self, name, hp, mp, power, speed, critical, normal_attack_name, level):
# self, name, hp, mp, power, speed, critical, normal_attack_name, level, magic_attack_name

# hp = 1000
# mp = 100
# power = randint(1, 10)
# speed = randint(1, 10)
# critical = randint(1, 10)
# level = 1
# player = Character(name, hp, mp, power, speed, critical, '모험가일반공격딱대.', level)
# Adventurer = Adventurer_Character(player.name, player.hp, player.mp, player.power, player.speed, player.critical, '살려주면좋겠다~!', player.level, '나는 죽지 않는다.')
# Magician = Magician_Character(player.name, player.hp, player.mp, player.power,
#                               player.speed, player.critical, '100만 볼트 방전', player.level, '6,000만 볼트 뇌룡')
# Warrior = Warrior_Character(player.name, player.hp, player.mp, player.power,
#                             player.speed, player.critical, '천본앵((せんぼんざくら)', player.level, '천본앵경엄(せんぼんざくらかげよし)!')
# Thief = Thief_Character(player.name, player.hp, player.mp, player.power,
#                         player.speed, player.critical, '치도리(き千鳥)', player.level, '나선환!(らせんがん)!')
# Archer = Archer_Character(player.name, player.hp, player.mp, player.power,
#                           player.speed, player.critical, '영자병장(靈子兵裝)', player.level, '하일리히 프파일 (Heilig Pfeil)')

# name, hp, power, speed선공율, normal_attack_name):
monster_level_1 = [Monster("리본돼지", 50, 5, 10, "\033[95m애교부리기 !\033[0m")]
monster_level_2 = [Monster("파란리본돼지", 60, 7, 10, "\033[95m귀여운 애교부리기 !\033[0m")]
monster_level_3 = [Monster("와일드보어", 80, 15, 12, "\033[97m몸통박치기 !\033[0m")]
monster_level_4 = [Monster("주니어예티", 100, 10, 10, "\033[90m내려찍기 !\033[0m")]
monster_level_5 = [Monster("파이어드레이크", 110, 10, 12, "\033[31m화염방사 !\033[0m")]
monster_level_6 = [Monster("아이스드레이크", 130, 20, 12, "\033[34m냉동펀치 !\033[0m")]
monster_level_7 = [Monster("마뇽", 140, 15, 15, "\033[35m오로라 브레스 !\033[0m")]
monster_level_8 = [Monster("주니어발록", 150, 20, 15, "\033[32m파이어 볼 !\033[0m")]
monster_level_9 = [Monster("발록", 160, 30, 15, "\033[30m떨어트리기 !\033[0m")]
monster_level_10 = Monster("페어리워터_박", 300, 100, 30,
                           "\033[34m여러분 물 마셔요~!(꼴깍)\033[0m")

monster_dic = {
    "level_low": monster_level_1 + monster_level_2 + monster_level_3,
    "level_middle": monster_level_4 + monster_level_5 + monster_level_6 + monster_level_7 + monster_level_8 + monster_level_9,
    "level_boss": monster_level_3 + monster_level_6 + monster_level_9
}
# 페어리고정1나머지2마리랜덤

# =========================================================================================================================
# 1~2층 몬스터 랜덤 추출 (1:3 전투) 전 뭐하면 좋을까요...
# monster_list = {}
# # if floor < 3 :
# for k in ["level_low"]:
#     selected_monster_1 = random.choice(monster_dic[k])
#     monster_list[k] = Monster(selected_monster_1.name, selected_monster_1.hp,
#                               selected_monster_1.power, selected_monster_1.speed, selected_monster_1.normal_attack_name)

#     selected_monster_2 = random.choice(monster_dic[k])
#     monster_list[k] = Monster(selected_monster_2.name, selected_monster_2.hp,
#                               selected_monster_2.power, selected_monster_2.speed, selected_monster_2.normal_attack_name)

#     selected_monster_3 = random.choice(monster_dic[k])
#     monster_list[k] = Monster(selected_monster_3.name, selected_monster_3.hp,
#                               selected_monster_3.power, selected_monster_3.speed, selected_monster_3.normal_attack_name)
#     print(f"{selected_monster_1.name}가 나타났다!\n"
#           f"{selected_monster_1.name}의 HP : {selected_monster_1.hp}")
#     print(f"{selected_monster_2.name}가 나타났다!\n"
#           f"{selected_monster_2.name}의 HP : {selected_monster_2.hp}")
#     print(f"{selected_monster_3.name}가 나타났다!\n"
#           f"{selected_monster_3.name}의 HP : {selected_monster_3.hp}")
# # =========================================================================================================================
# # 4~6층 몬스터 랜덤 추출 (1:3 전투)
# # elif floor < 6 :
# monster_list_middle = {}
# for k in ["level_middle"]:
#     selected_monster_4 = random.choice(monster_dic[k])
#     monster_list_middle[k] = Monster(selected_monster_4.name, selected_monster_4.hp,
#                                      selected_monster_4.power, selected_monster_4.speed, selected_monster_4.normal_attack_name)

#     selected_monster_5 = random.choice(monster_dic[k])
#     monster_list_middle[k] = Monster(selected_monster_5.name, selected_monster_5.hp,
#                                      selected_monster_5.power, selected_monster_5.speed, selected_monster_5.normal_attack_name)

#     selected_monster_6 = random.choice(monster_dic[k])
#     monster_list_middle[k] = Monster(selected_monster_6.name, selected_monster_6.hp,
#                                      selected_monster_6.power, selected_monster_6.speed, selected_monster_6.normal_attack_name)
#     print(f"{selected_monster_4.name}가 나타났다!\n"
#           f"{selected_monster_4.name}의 HP : {selected_monster_4.hp}")
#     print(f"{selected_monster_5.name}가 나타났다!\n"
#           f"{selected_monster_5.name}의 HP : {selected_monster_5.hp}")
#     print(f"{selected_monster_6.name}가 나타났다!\n"
#           f"{selected_monster_6.name}의 HP : {selected_monster_6.hp}")
# # =========================================================================================================================
# # 7~9층 몬스터 랜덤 추출 (1:3 전투)
# # elif floor < 9 :
# monster_list_high = {}
# for k in ["level_high"]:
#     selected_monster_7 = random.choice(monster_dic[k])
#     monster_list[k] = Monster(selected_monster_7.name, selected_monster_7.hp,
#                               selected_monster_7.power, selected_monster_7.speed, selected_monster_7.normal_attack_name)

#     selected_monster_8 = random.choice(monster_dic[k])
#     monster_list[k] = Monster(selected_monster_8.name, selected_monster_8.hp,
#                               selected_monster_8.power, selected_monster_8.speed, selected_monster_8.normal_attack_name)

#     selected_monster_9 = random.choice(monster_dic[k])
#     monster_list[k] = Monster(selected_monster_9.name, selected_monster_9.hp,
#                               selected_monster_9.power, selected_monster_9.speed, selected_monster_9.normal_attack_name)
#     print(f"{selected_monster_7.name}가 나타났다!\n"
#           f"{selected_monster_7.name}의 HP : {selected_monster_7.hp}")
#     print(f"{selected_monster_8.name}가 나타났다!\n"
#           f"{selected_monster_8.name}의 HP : {selected_monster_8.hp}")
#     print(f"{selected_monster_9.name}가 나타났다!\n"
#           f"{selected_monster_9.name}의 HP : {selected_monster_9.hp}")
# # =========================================================================================================================
# # 보스방 랜덤추출 (1:3 전투)
# # else :
# monster_list_boss = {}
# for k in ["level_boss"]:
#     bossroom_3 = Monster("와일드보어", 80, 15, 12, "몸통박치기 !")
#     bossroom_6 = Monster("아이스드레이크", 130, 20, 12, "냉동펀치 !")
#     bossroom_9 = Monster("발록", 160, 30, 15, "떨어트리기 !")
#     bossroom_10 = Monster("페어리워터_박", 300, 100, 30, "여러분 물 마셔요~!(꼴깍)")
#     print(f"{bossroom_3.name}가 나타났다!\n"
#           f"{bossroom_3.name}의 HP : {bossroom_3.hp}")
#     print(f"{bossroom_6.name}가 나타났다!\n"
#           f"{bossroom_6.name}의 HP : {bossroom_6.hp}")
#     print(f"{bossroom_9.name}가 나타났다!\n"
#           f"{bossroom_9.name}의 HP : {bossroom_9.hp}")
#     print(f"{bossroom_10.name}가 나타났다!\n"
#           f"{bossroom_10.name}의 HP : {bossroom_10.hp}")


# (self, name, hp, mp, power, speed, critical, , normal_attack_name, magic_attack_name):
# (self, name, hp, mp, power, speed, critical, ):
#     - 몬스터 사냥 성공시 보상에 따른 게임 진행이 되어야 합니다.
#           #탑오르기?층오르기?
#               - 층마다 레벨업 및 아이템보상
#               - 팀장님 짱
#               - 보상 : 골드랑 회복물약
#                   보상은 골드/회복물약/골드+회복물약 중 확률적으로 얻음 (시그너스 제외)
#               - 회복물약은 1개씩만 제공
#               - 골드는 최대 1개 제공, 골드 3개당 물약 1 개 구매가능 (상점)
#           !몬스터! 강함의 차이?
#             # 고블린 (1층 ~)
#               - 고블린(ㄹㅇ잔몹)
#               - 홉고블린(ㄹㅇ잔몹)
#               - 고블린로드(ㄹㅇ잔몹 중에서 나는 보스)
#             # 드레이크
#               - 카파드레이크(일반몬)
#               - 레드드레이크(일반몬)
#               - 아이스드레이크(일반몬)
#               - 다크드레이크(일반몬)
#             # 발록
#               - 주니어발록(필드몬)
#               - 발록(보스몬)
#             # 물의요정(혜린님)
#               - 페어리워터(울트라전설보스몬)=나랑비슷하게쎔....?


#     - 몬스터와 1:N or N:M 전투가 가능해야 합니다.
#           - 전투 입장시 Monster객체 수 1~n 랜덤생성, 타겟팅해서 공격가능하게
#           - 입력되는 몬스터이름은 대표몬스터의 이름
#           - 전투입장시 대표몬스터 1마리와 하위 몬스터 1~n마리 등장
#               ex) 주니어발록과의 전투 시작!
#                   주니어발록(필드몬, 대표몬스터), 카파드레이크(일반몬), 홉고블린(ㄹㅇ잔몹)
#
#               기본캐릭터로 시작 > 모험가, 레지, 시그 종족버프 설명 거기서 종족만 택1 >
#               > n층 돌파시 직업선택 > n층 돌파시 전직
#
#
#
#                               정해야할게뭘까요?ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ도와주세요 ㅠㅠㅠㅠㅠㅠㅠㅠ
#                               메이플스토리 : 직업이무지하게많고 몬스터도넘쳐흘립니다. 레벨 및 전직
#
#                       투표소 1. : 0 , 2. : 0           투표완료 : 마우스위치( )


# 만들어야 할 코드들
#       - 캐릭터 직업, 스킬, 몬스터직업&스킬 -> 2명 진규,현식
#       - 던전 및 상점 구현 (골드로 회복물약사기, 골드3개당 회복물약 1개) -> 3명 소진,혜린,명흠
#       - 메인 전투 -> 보류
#           -
#
#     깃허브여기로쓸게요 https://github.com/kyuparfum/eye_nose_mouse
