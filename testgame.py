import random as rd
import copy

class PlayerChar:
    def __init__(self, name, hp, atk, dfs, crt, avd):
        # 캐릭터의 초기 상태를 설정하는 생성자
        self.name = name       # 캐릭터의 이름
        self.hp = hp           # 캐릭터의 체력
        self.initial_hp = hp  # 초기 체력을 저장하여 나중에 복원할 수 있도록 함
        self.atk = atk         # 공격력
        self.dfs = dfs         # 방어력
        self.crt = crt         # 치명타 확률 (백분율)
        self.avd = avd         # 회피율 (백분율)

    def attack(self, other, color):
        # 다른 캐릭터에게 공격을 수행하는 메서드
        # 공격이 회피될 확률을 계산
        if rd.random() * 100 < other.avd:
            print("\033[32m" + "-" * 15 + " 전투 결과 " + "-" * 15 + "\033[0m")
            print(color + "{}의 공격이 회피되었습니다.\033[0m".format(self.name))
            print("\033[32m" + "-" * 15 + " 현재 스탯 " + "-" * 15 + "\033[0m")
            return

        # 치명타 확률을 계산
        crtnan = rd.random() * 100
        damage = int(self.atk * (0.9 + rd.random() * 0.2))  # 공격력의 90%~110% 사이의 랜덤 데미지

        print("\033[32m" + "-" * 15 + " 전투 결과 " + "-" * 15 + "\033[0m")

        if crtnan < self.crt:
            # 치명타 발생 시
            damage = int(damage * 1.8)  # 데미지를 80% 증가시킴
            if damage < 0:
                damage = 1
            other.hp -= damage
            print(color + "크리티컬 히트!!! {}의 공격으로 {}에게 {}데미지를 입혔다!\033[0m".format(self.name, other.name, damage))
        else:
            # 일반 공격
            damage -= other.dfs  # 상대의 방어력을 고려
            if damage < 0:
                damage = 1
            other.hp -= damage
            print(color + "{}의 공격으로 {}에게 {}데미지를 입혔다.\033[0m".format(self.name, other.name, damage))

        # 전투 결과를 출력하는 부분
        if self.isalive() and other.isalive():
            print("\033[32m" + "-" * 15 + " 현재 스탯 " + "-" * 15 + "\033[0m")

    def isalive(self):
        # 캐릭터가 살아있는지 확인하는 메서드
        return self.hp > 0

    def __str__(self):
        # 캐릭터의 상태를 문자열로 반환
        return (f"{self.name} HP:{self.hp}\n"
                f"공격력 {self.atk}, 방어력 {self.dfs}, 치명률 {self.crt}%, 회피율 {self.avd}%"
                )

    def reset(self):
        # 캐릭터의 체력을 초기 상태로 복원
        self.hp = self.initial_hp

    def clone(self):
        # 캐릭터의 깊은 복사본을 반환
        return copy.deepcopy(self)

def playerTurn(player, opponent, color):
    # 플레이어의 턴을 처리하는 함수
    while True:
        print(color + "{}의 턴입니다. 행동을 선택하세요. : \033[0m".format(player.name))
        print("1. 공격")
        print("2. 스킬")
        print("3. 아이템")
        choice = input("행동 선택 : ")
        
        if choice == "1":
            player.attack(opponent, color)  # 공격 선택 시 공격 실행
            break
        else:
            print("아직 구현되지 않은 선택지입니다.")  # 구현되지 않은 선택지 메시지 출력

def startGame(pc01, pc02):
    # 게임 전투를 시작하는 함수
    print("\033[32m" + "=" * 30 + "\033[0m")
    print("\033[33m전투 시작!\033[0m")
    print("\033[32m" + "-" * 30 + "\033[0m")
    print("\033[31m", end="")  # 플레이어 1: 빨간색
    print(pc01)  # 플레이어 1의 상태 출력
    print("\033[0m", end="")  # 색상 리셋
    print("\033[34m", end="")  # 플레이어 2: 파란색
    print(pc02)  # 플레이어 2의 상태 출력
    print("\033[0m", end="")  # 색상 리셋
    print("\033[32m" + "-" * 30 + "\033[0m")
    
    # 전투 루프
    while pc01.isalive() and pc02.isalive():
        playerTurn(pc01, pc02, "\033[31m")  # 플레이어 1의 턴
        if not pc02.isalive():  # 적 캐릭터가 사망했는지 확인
            print("\033[31m{}의 승리!\033[0m".format(pc01.name))
            break
        print("\033[31m", end="")
        print(pc01)  # 플레이어 1의 상태 출력
        print("\033[0m", end="")  # 색상 리셋
        print("\033[34m", end="")
        print(pc02)  # 플레이어 2의 상태 출력
        print("\033[0m", end="")  # 색상 리셋
        print("\033[32m" + "-" * 30 + "\033[0m")
        playerTurn(pc02, pc01, "\033[34m")  # 플레이어 2의 턴
        if not pc01.isalive():  # 적 캐릭터가 사망했는지 확인
            print("\033[34m{}의 승리!\033[0m".format(pc02.name))
            break
        print("\033[31m", end="")
        print(pc01)  # 플레이어 1의 상태 출력
        print("\033[0m", end="")  # 색상 리셋
        print("\033[34m", end="")
        print(pc02)  # 플레이어 2의 상태 출력
        print("\033[0m", end="")  # 색상 리셋
        print("\033[32m" + "-" * 30 + "\033[0m")

def chooseCharacter():
    # 캐릭터 선택 함수
    characters = [a_bigAxMan, b_bigShMan, c_doggerMan, d_hotPunchMan, e_crtMan, f_osoiMan, x_normalMan1, y_normalMan2, z_sandBag]
    print("캐릭터를 선택하세요:")
    for i, character in enumerate(characters, 1):
        print(f"{i}. {character.name}")
    
    while True:
        choice = input("선택 (숫자 입력): ")
        if choice.isdigit() and 1 <= int(choice) <= len(characters):
            return characters[int(choice) - 1].clone()  # 선택한 캐릭터의 깊은 복사본 반환
        else:
            print("유효한 번호를 선택하세요.")  # 유효하지 않은 입력에 대한 메시지 출력

def main():
    # 메인 메뉴 함수
    while True:
        print("\033[32m" + "=" * 30 + "\033[0m")
        print("\033[33m게임 메뉴\033[0m")
        print("1. 전투 시작")
        print("2. 종료")
        print("\033[32m" + "=" * 30 + "\033[0m")
        
        choice = input("선택: ")
        if choice == "1":
            print("\033[31m", end="")  # 플레이어 1: 빨간색
            print("플레이어 1의 캐릭터 선택:")
            print("\033[0m", end="")  # 색상 리셋
            player1 = chooseCharacter()  # 플레이어 1의 캐릭터 선택
            print("\033[31m", end="")  # 플레이어 1: 빨간색
            print(f"플레이어 1이 {player1.name}을(를) 선택했습니다.")
            print("\033[0m", end="")  # 색상 리셋
            
            print("\033[34m", end="")  # 플레이어 2: 파란색
            print("플레이어 2의 캐릭터 선택:")
            print("\033[0m", end="")  # 색상 리셋
            player2 = chooseCharacter()  # 플레이어 2의 캐릭터 선택
            print("\033[34m", end="")  # 플레이어 2: 파란색
            print(f"플레이어 2가 {player2.name}을(를) 선택했습니다.")
            print("\033[0m", end="")  # 색상 리셋
            
            startGame(player1, player2)  # 전투 시작
        elif choice == "2":
            print("게임을 종료합니다.")
            break  # 메인 루프 종료
        else:
            print("유효한 옵션을 선택하세요.")  # 유효하지 않은 옵션에 대한 메시지 출력

# 초기 캐릭터 정의
a_bigAxMan = PlayerChar("빅도끼맨", hp=800, atk=120, dfs=20, crt=20, avd=5)
b_bigShMan = PlayerChar("왕방패맨", hp=1000, atk=80, dfs=50, crt=15, avd=0)
c_doggerMan = PlayerChar("돚거맨", hp=700, atk=100, dfs=10, crt=50, avd=15)
d_hotPunchMan = PlayerChar("매콤주먹맨", hp=800, atk=100, dfs=30, crt=30, avd=10)
e_crtMan = PlayerChar("치-타맨", hp=700, atk=70, dfs=15, crt=90, avd=15)
f_osoiMan = PlayerChar("키사마와오소이", hp=600, atk=70, dfs=25, crt=33, avd=33)
x_normalMan1 = PlayerChar("일반인1", hp=550, atk=50, dfs=0, crt=25, avd=5)
y_normalMan2 = PlayerChar("일반인2", hp=500, atk=55, dfs=5, crt=20, avd=5)
z_sandBag = PlayerChar("샌드백", hp=1200, atk=0, dfs=100, crt=0, avd=0)

# 게임 시작
main()
