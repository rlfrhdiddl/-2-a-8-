from Dungeon import *
from team import *
import random
import os
import time
import sys
from start import *
from endding import *

game_start = True


# 탑 입장
def game():
    floor = 1
    global player
    while True:
        # 1-2층 탑에 진입
        if floor < 3 and player.hp > 0:
            print(f'탑의 \033[33m{floor}층에 도착하였습니다.\033[0m')
            monster_list = {}
            for k in ["level_low"]:
                selected_monster_1 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_1.name, selected_monster_1.hp,
                                          selected_monster_1.power, selected_monster_1.speed, selected_monster_1.normal_attack_name)

                selected_monster_2 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_2.name, selected_monster_2.hp,
                                          selected_monster_2.power, selected_monster_2.speed, selected_monster_2.normal_attack_name)

                selected_monster_3 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_3.name, selected_monster_3.hp,
                                          selected_monster_3.power, selected_monster_3.speed, selected_monster_3.normal_attack_name)
                print(
                    f"{selected_monster_1.name}(HP : {selected_monster_1.hp})가 나타났다!\n")
                print(
                    f"{selected_monster_2.name}(HP : {selected_monster_2.hp})가 나타났다!\n")
                print(
                    f"{selected_monster_3.name}(HP : {selected_monster_3.hp})가 나타났다!\n")
            # 전투진행코드
            while True:
                if player.hp > 0:
                    player.show_status()
                    if selected_monster_1.hp > 0 or selected_monster_2.hp > 0 or selected_monster_3.hp > 0:
                        aa = int(
                            input('어떤 행동을 하시겠습니까?\n\033[30m1.일반공격\033[0m \033[34m2.마법공격\033[0m \033[32m3.인벤토리\033[0m \033[31m4.포기한다\033[0m\n>>'))
                        if aa == 1:
                            print(
                                f"어떤 몬스터를 공격하시겠습니까?\n1.{selected_monster_1.name} 현재HP: [{selected_monster_1.hp}]\n2.{selected_monster_2.name} 현재HP: [{selected_monster_2.hp}]\n3.{selected_monster_3.name} 현재HP:[{selected_monster_3.hp}]")
                            bb = int(input('>> '))
                            if bb == 1:
                                player.normal_attack(selected_monster_1)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                if selected_monster_1.hp > 0:
                                    continue
                                else:
                                    if selected_monster_1.hp == 0:
                                        print(
                                            f"{selected_monster_1.name}이 쓰러졌다!")
                                        continue
                            elif bb == 2:
                                player.normal_attack(selected_monster_2)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                if selected_monster_2.hp > 0:
                                    continue
                                else:
                                    if selected_monster_2.hp == 0:
                                        print(
                                            f"{selected_monster_2.name}이 쓰러졌다!")
                                        continue
                            elif bb == 3:
                                player.normal_attack(selected_monster_3)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                if selected_monster_3.hp > 0:
                                    continue

                                else:
                                    if selected_monster_3.hp == 0:
                                        print(
                                            f"{selected_monster_3.name}이 쓰러졌다!")
                                        continue
                            else:
                                # 힘내요! 포기해요우리.......................................................앗 비밀.....
                                continue
                        if aa == 2:
                            print(f'\033[31m 마법공격은 LEVEL 5가 되어야 사용할 수 있습니다.')
                            print(f'다른 공격을 선택해 주세요.\033[0m')
                            continue
                        if aa == 3:
                            player_inventory.showInventory()
                            print('인벤토리에 있는 물약을 바로 사용할 수 있습니다.')
                            player_potion.use(player)
                            continue
                        if aa == 4:
                            break
                        else:
                            # 힘내요!
                            print('! 숫자를 입력해 주세요 !')
                            continue

                    elif selected_monster_1.hp == 0 and selected_monster_2.hp == 0 and selected_monster_3.hp == 0 and player.hp > 0:
                        print(f"대단합니다! 모든 몬스터를 물리쳤습니다!")
                        my_money.add_money(812354)
                        break
                    else:
                        break
                else:
                    print(f"유다희~!")
                    break
        # 4-9층 탑에 진입
        elif 10 > floor > 3 and player.hp > 0:
            if player.level == 5 and player.hp > 0:  # elif player.level == 5: 에서 바꿨습니다
                print(f'탑의 \033[31m{floor}층\033[0m에 도착하였습니다.')
                while True:
                    print(
                        f'\033[33m빠라라빠빠\033[0m\n전직 가능 레벨이 됐습니다. 전직 할 직업을 선택해주세요')
                    select_job = int(
                        input('1.숨겨진 옛직업 2.마법사(갓에넬) 3.전사(바쿠야) 4.도적(나스케(나루토 사스케)) 5.궁수(유하바하)\n>>  '))
                    if select_job == 1:
                        player = Adventurer_Character(player.name, player.hp, player.mp, player.power,
                                                      player.speed, player.critical, '살려주면좋겠다~!', player.level, '나는 죽지 않는다.')
                        print(f'{player.level}레벨입니다.')
                        break
                    elif select_job == 2:
                        player = Magician_Character(player.name, player.hp, player.mp, player.power,
                                                    player.speed, player.critical, '100만 볼트 방전', player.level, '6,000만 볼트 뇌룡')
                        print(f'{player.level}레벨입니다.')
                        break
                    elif select_job == 3:
                        player = Warrior_Character(player.name, player.hp, player.mp, player.power, player.speed,
                                                   player.critical, '천본앵((せんぼんざくら)', player.level, '천본앵경엄(せんぼんざくらかげよし)!')
                        print(f'{player.level}레벨입니다.')
                        break
                    elif select_job == 4:
                        player = Thief_Character(player.name, player.hp, player.mp, player.power,
                                                 player.speed, player.critical, '치도리(き千鳥)', player.level, '나선환!(らせんがん)!')
                        print(f'{player.level}레벨입니다.')
                        break
                    elif select_job == 5:
                        player = Archer_Character(player.name, player.hp, player.mp, player.power, player.speed,
                                                  player.critical, '영자병장(靈子兵裝)', player.level, '하일리히 프파일 (Heilig Pfeil)')
                        print(f'{player.level}레벨입니다.')
                        break
                    else:
                        print(f'\033[32m범위를 벗어 났자네~!\033[0m')
                        print(f'\033[32m전직할 직업을 정확히 다시 입력해주세요\033[0m')
                        continue
            print(f'탑의 \033[32m{floor}층에 도착하였습니다.\033[0m')
            monster_list = {}
            for k in ["level_middle"]:
                selected_monster_1 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_1.name, selected_monster_1.hp,
                                          selected_monster_1.power, selected_monster_1.speed, selected_monster_1.normal_attack_name)

                selected_monster_2 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_2.name, selected_monster_2.hp,
                                          selected_monster_2.power, selected_monster_2.speed, selected_monster_2.normal_attack_name)

                selected_monster_3 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_3.name, selected_monster_3.hp,
                                          selected_monster_3.power, selected_monster_3.speed, selected_monster_3.normal_attack_name)
                print(
                    f"\033[95m{selected_monster_1.name}\033[31m(HP : {selected_monster_1.hp})\033[0m가 나타났다!\033[0m\n")
                print(
                    f"\033[95m{selected_monster_2.name}\033[31m(HP : {selected_monster_2.hp})\033[0m가 나타났다!\033[0m\n")
                print(
                    f"\033[95m{selected_monster_3.name}\033[31m(HP : {selected_monster_3.hp})\033[0m가 나타났다\033[0m!\n")

            # 전투진행코드
            while True:
                if player.hp > 0:
                    player.show_status()
                    if selected_monster_1.hp > 0 or selected_monster_2.hp > 0 or selected_monster_3.hp > 0:
                        aa = int(
                            input('어떤 행동을 하시겠습니까?\n\033[30m1.일반공격\033[0m \033[34m2.마법공격\033[0m \033[32m3.인벤토리\033[0m \033[31m4.포기한다\033[0m\n>>'))
                        if aa == 1:
                            print(
                                f"어떤 몬스터를 공격하시겠습니까?\n1.{selected_monster_1.name} 현재HP: [{selected_monster_1.hp}]\n2.{selected_monster_2.name} 현재HP: [{selected_monster_2.hp}]\n3.{selected_monster_3.name} 현재HP:[{selected_monster_3.hp}]")
                            bb = int(input('>> '))
                            if bb == 1:
                                player.normal_attack(selected_monster_1)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                if selected_monster_1.hp > 0:
                                    continue
                                else:
                                    if selected_monster_1.hp == 0:
                                        print(
                                            f"{selected_monster_1.name}이 쓰러졌다!")
                                        continue
                            elif bb == 2:
                                player.normal_attack(selected_monster_2)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                if selected_monster_2.hp > 0:
                                    continue
                                else:
                                    if selected_monster_2.hp == 0:
                                        print(
                                            f"{selected_monster_2.name}이 쓰러졌다!")
                                        continue
                            elif bb == 3:
                                player.normal_attack(selected_monster_3)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                if selected_monster_3.hp > 0:
                                    continue

                                else:
                                    if selected_monster_3.hp == 0:
                                        print(
                                            f"{selected_monster_3.name}이 쓰러졌다!")
                                        continue
                            else:
                                # 힘내요!
                                continue
                        elif aa == 2:
                            if player.level > 4:
                                print(
                                    f"어떤 몬스터를 공격하시겠습니까?\n1.{selected_monster_1.name} 현재HP: [{selected_monster_1.hp}]\n2.{selected_monster_2.name} 현재HP: [{selected_monster_2.hp}]\n3.{selected_monster_3.name} 현재HP:[{selected_monster_3.hp}]")
                                bb = int(input('>> '))
                                if bb == 1:
                                    player.magic_attack(selected_monster_1)
                                    selected_monster_1.normal_attack(player)
                                    selected_monster_2.normal_attack(player)
                                    selected_monster_3.normal_attack(player)
                                    if selected_monster_1.hp > 0:
                                        continue
                                    else:
                                        if selected_monster_1.hp == 0:
                                            print(
                                                f"{selected_monster_1.name}이 쓰러졌다!")
                                            continue
                                elif bb == 2:
                                    player.magic_attack(selected_monster_2)
                                    selected_monster_1.normal_attack(player)
                                    selected_monster_2.normal_attack(player)
                                    selected_monster_3.normal_attack(player)
                                    if selected_monster_2.hp > 0:
                                        continue
                                    else:
                                        if selected_monster_2.hp == 0:
                                            print(
                                                f"{selected_monster_2.name}이 쓰러졌다!")
                                            continue
                                elif bb == 3:
                                    player.magic_attack(selected_monster_3)
                                    selected_monster_1.normal_attack(player)
                                    selected_monster_2.normal_attack(player)
                                    selected_monster_3.normal_attack(player)
                                    if selected_monster_3.hp > 0:
                                        continue

                                else:
                                    if selected_monster_3.hp == 0:
                                        print(
                                            f"{selected_monster_3.name}이 쓰러졌다!")
                                        continue
                            else:
                                print('마법공격은 LEVEL 5가 되어야 사용할 수 있습니다.')
                                print('다른 공격을 선택해 주세요.')
                                continue
                        elif aa == 3:
                            player_inventory.showInventory()
                            print('인벤토리에 있는 물약을 바로 사용할 수 있습니다.')
                            player_potion.use(player)
                            break
                        elif aa == 4:
                            break
                        elif aa == '':
                            print('빈칸금지~!')
                        else:
                            # 힘내요!
                            print('! 숫자를 입력해 주세요 !')
                            continue
                    elif selected_monster_1.hp == 0 and selected_monster_2.hp == 0 and selected_monster_3.hp == 0 and player.hp > 0:
                        print(f"대단합니다! 모든 몬스터를 물리쳤습니다!")
                        my_money.add_money(812354)
                        break
                    else:
                        break
                else:
                    print(f"유다희~!")
                    break
        # 꼭대기층
        elif floor == 10 and player.hp > 0:
            print(f'탑의 \033[32m{floor}층에 도착하였습니다.\033[0m')
            monster_list = {}
            for k in ["level_boss"]:
                selected_monster_4 = monster_level_10
                selected_monster_1 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_1.name, selected_monster_1.hp,
                                          selected_monster_1.power, selected_monster_1.speed, selected_monster_1.normal_attack_name)

                selected_monster_2 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_2.name, selected_monster_2.hp,
                                          selected_monster_2.power, selected_monster_2.speed, selected_monster_2.normal_attack_name)

                selected_monster_3 = random.choice(monster_dic[k])
                monster_list[k] = Monster(selected_monster_3.name, selected_monster_3.hp,
                                          selected_monster_3.power, selected_monster_3.speed, selected_monster_3.normal_attack_name)
                print(f"\033[95m{selected_monster_1.name}가 나타났다!\033[0m\n"
                      f"\033[95m{selected_monster_1.name}의\033[0m \033[31mHP : {selected_monster_1.hp}\033[0m")
                print(f"\033[95m{selected_monster_2.name}가 나타났다!\033[0m\n"
                      f"\033[95m{selected_monster_2.name}의\033[0m \033[31mHP : {selected_monster_2.hp}\033[0m")
                print(f"\033[95m{selected_monster_3.name}가 나타났다\033[0m!\n"
                      f"\033[95m{selected_monster_3.name}의\033[0m \033[31mHP : {selected_monster_3.hp}\033[0m")
                print(f"\033[95m워터타워의 주인 [{selected_monster_4.name}]가 나타났다!!\033[0m!\n"
                      f"\033[95m{selected_monster_4.name}의\033[0m \033[31mHP : {selected_monster_4.hp}\033[0m")
            # 전투진행코드
            while True:
                if player.hp > 0:
                    player.show_status()
                    if selected_monster_1.hp > 0 or selected_monster_2.hp > 0 or selected_monster_3.hp > 0 or selected_monster_4.hp > 0:
                        aa = int(
                            input('어떤 행동을 하시겠습니까?\n\033[30m1.일반공격\033[0m \033[34m2.마법공격\033[0m \033[32m3.인벤토리\033[0m \033[31m4.포기한다\033[0m\n>>'))
                        if aa == 1:
                            print(
                                f"어떤 몬스터를 공격하시겠습니까?\n1.{selected_monster_1.name} 현재HP: [{selected_monster_1.hp}]\n2.{selected_monster_2.name} 현재HP: [{selected_monster_2.hp}]\n3.{selected_monster_3.name} 현재HP:[{selected_monster_3.hp}]\n4.{selected_monster_4.name} 현재HP:[{selected_monster_4.hp}]")
                            bb = int(input('>> '))
                            if bb == 1:
                                player.normal_attack(selected_monster_1)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_1.hp > 0:
                                    continue
                                else:
                                    if selected_monster_1.hp == 0:
                                        print(
                                            f"{selected_monster_1.name}이 쓰러졌다!")
                                        continue
                            elif bb == 2:
                                player.normal_attack(selected_monster_2)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_2.hp > 0:
                                    continue
                                else:
                                    if selected_monster_2.hp == 0:
                                        print(
                                            f"{selected_monster_2.name}이 쓰러졌다!")
                                        continue
                            elif bb == 3:
                                player.normal_attack(selected_monster_3)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_3.hp > 0:
                                    continue

                                else:
                                    if selected_monster_3.hp == 0:
                                        print(
                                            f"{selected_monster_3.name}이 쓰러졌다!")
                                        continue
                            elif bb == 4:
                                player.normal_attack(selected_monster_4)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_4.hp > 0:
                                    continue

                                else:
                                    if selected_monster_4.hp == 0:
                                        print(
                                            f"{selected_monster_4.name}이 쓰러졌다!")
                                        continue
                            else:
                                # 힘내요!
                                continue
                        elif aa == 2:
                            print(
                                f"어떤 몬스터를 공격하시겠습니까?\n1.{selected_monster_1.name} 현재HP: [{selected_monster_1.hp}]\n2.{selected_monster_2.name} 현재HP: [{selected_monster_2.hp}]\n4.{selected_monster_4.name} 현재HP:[{selected_monster_4.hp}]\n3.{selected_monster_4.name} 현재HP:[{selected_monster_4.hp}]")
                            bb = int(input('>> '))
                            if bb == 1:
                                player.magic_attack(selected_monster_1)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_1.hp > 0:
                                    continue
                                else:
                                    if selected_monster_1.hp == 0:
                                        print(
                                            f"{selected_monster_1.name}이 쓰러졌다!")
                                        continue
                            elif bb == 2:
                                player.magic_attack(selected_monster_2)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_2.hp > 0:
                                    continue
                                else:
                                    if selected_monster_2.hp == 0:
                                        print(
                                            f"{selected_monster_2.name}이 쓰러졌다!")
                                        continue
                            elif bb == 3:
                                player.magic_attack(selected_monster_3)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_3.hp > 0:
                                    continue
                                else:
                                    if selected_monster_3.hp == 0:
                                        print(
                                            f"{selected_monster_3.name}이 쓰러졌다!")
                                        continue
                            elif bb == 4:
                                player.magic_attack(selected_monster_4)
                                selected_monster_1.normal_attack(player)
                                selected_monster_2.normal_attack(player)
                                selected_monster_3.normal_attack(player)
                                selected_monster_4.normal_attack(player)
                                if selected_monster_4.hp > 0:
                                    continue

                                else:
                                    if selected_monster_4.hp == 0:
                                        print(
                                            f"{selected_monster_4.name}이 쓰러졌다!")
                                        continue
                        elif aa == 3:
                            player_inventory.showInventory()
                            print('인벤토리에 있는 물약을 바로 사용할 수 있습니다.')
                            player_potion.use(player)
                            break
                        elif aa == 4:
                            break
                        else:
                            # 힘내요!
                            print('! 숫자를 입력해 주세요 !')
                            continue
                    elif selected_monster_1.hp == 0 and selected_monster_2.hp == 0 and selected_monster_3.hp == 0 and selected_monster_4.hp == 0 and player.hp > 0:
                        print(f"대단합니다! 모든 몬스터를 물리쳤습니다!")
                        my_money.add_money(812354)
                        break
                    else:
                        break
                else:
                    print(f"유다희~!")
                    break
# 상점이용 층
        elif floor == 3 or floor == 9:  # 옮김
            a = input(
                f'\033[32m{floor}층에 도착하셨습니다.\033[0m\n{floor}층에선 상점을 이용하실 수 있습니다.\n1.상점으로 이동 \n2.다음층으로 올라간다 3.??\n>>')
            if a == "1":
                shop()
                continue
            elif a == "2":
                floor += 1
                continue
        elif floor == 11:
            endding_bye('\033[33m 게임 끝났어 친구야~!\033[0m')
            break

        if selected_monster_1.hp == 0 and selected_monster_2.hp == 0 and selected_monster_3.hp == 0 and player.hp > 0:
            a = input('다음층으로 올라가시겠습니까?\n1.올라간다 2.?? 3.??\n>>')
            # 다음단계 진행 여부
            if a == "1":
                player.level += 1
                floor += 1
                selected_monster_1.hp = selected_monster_1.max_hp
                selected_monster_2.hp = selected_monster_2.max_hp
                selected_monster_3.hp = selected_monster_3.max_hp
                continue
                # elif hp <= 0:
                # 재도전 여부?!
                # elif 5 < level <= 10:
                # 위와 동일
                # 상점?

            #    기존 여기 있던내용 잠시 bat_temp으로옮김


# ==========================터미널에서 실행시 처음 진행되는 시작점=============================================================
# type_text("\033[36m물마셔요 게임을 시작합니다\033[0m\n"
#           f"\033[33m==================== 게임설명 ====================\n"
#           f"평화로운 헤네시스 였던 곳\n"
#           f"이제는 나뭇잎마을이 되어버린곳\n"
#           f"웨코문드가 되어 버린 곳\n"
#           f"하늘섬이 되어 버린 곳\n"
#           f"====================    끝    ====================\033[0m\n")
print("\033[36m물마셔요 게임을 시작합니다\033[0m")

while game_start == True:
    print(f"원하는 메뉴의 번호를 입력한 다음 Enter키를 누르세요. 꼴깍~! \n"
          f"1.게임시작 \n"
          f"2.게임설명 \n"
          f"3.게임종료 \n")
    command = input(">>")
    if command == '1':
        print(f'캐릭터의 이름을 입력해주세요. 꼴깍~!')
        name = input('>>')
        hp = 10000
        mp = 100
        power = random.randint(10000, 50000)
        speed = random.randint(1, 10)
        critical = random.randint(1, 10)
        level = 1
        player = Character(name, hp, mp, power, speed,
                           critical, '모험가일반공격딱대.', level)
        player_potion = Potion(player)

        print(f'게임을 시작하겠습니다.')
        game()

        break
    elif command == '2':
        print(f"튜토리얼진행으로 넘어가기")
    elif command == '3':
        print("\033[32m이용해주셔서 감사합니다.\033[0m")
        break
    else:
        print("\033[31m잘못 누르셨습니다.\033[0m\n")
