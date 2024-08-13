import random as rd

class PlayerChar:
    def __init__(self, name, hp, atk, dfs, crt, avd):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.dfs = dfs
        self.crt = crt
        self.avd = avd
    def attack(self, other):
        crtnan = rd.random() * 100
        damage = int(self.atk * (0.9 + rd.random() * 0.2))
        print("-" * 15, "전투 결과", "-" * 15)
        if crtnan < self.crt:
            damage = int(damage * 1.8)
            if damage < 0:
                damage = 1
            other.hp -= damage
            print("크리티컬 히트!!! {}의 공격으로 {}에게 {}데미지를 입혔다!".format(self.name, other.name, damage))
        else :
            other.hp -= damage
            damage -= other.dfs
            if damage < 0:
                damage = 1
            print("{}의 공격으로 {}에게 {}데미지를 입혔다.".format(self.name, other.name, damage))
        print("-" * 15, "현재 스탯", "-" * 15)
    def isalive(self):
        return self.hp > 0
    def __str__(self):
        return (f"{self.name} HP:{self.hp}\n"
                f"공격력 {self.atk}, 방어력 {self.dfs}, 치명률 {self.crt}%"
                )
    #f"공격력 : {self.atk}\n"
    #f"방어력 : {self.dfs}\n"
    #f"치명률 : {self.crt}\n"

def playerTurn (player, opponent):
    while True:
        print("{}의 턴입니다. 행동을 선택하세요. : ".format(player.name))
        print("1.공격")
        print("2.방어")
        print("3.스킬")
        choice = input("행동 선택 : ")
        
        if choice == "1":
            player.attack(opponent)
            break
        else:
            print("아직 구현되지 않은 선택지입니다.")

def startGame(pc01, pc02):
    print("=" * 30)
    print("전투 시작!")
    print("-" * 30)
    print(pc01)
    print(pc02)
    print("-" * 30)
    while pc01.isalive() and pc02.isalive():
        playerTurn (pc01, pc02)
        if not pc02.isalive():
            print("{}의 승리!".format(pc01.name))
            break
        print(pc01)
        print(pc02)
        print("-" * 30)
        playerTurn(pc02, pc01)
        if not pc01.isalive():
            print("{}의 승리!".format(pc02.name))
            break
        print(pc01)
        print(pc02)
        print("-" * 30)

#이름, 체력, 공격력, 방어력, 크리티컬, 회피
bigAxMan = PlayerChar("빅도끼맨", hp=800, atk=120, dfs=20, crt=20, avd=0)
bigShMan = PlayerChar("왕방패맨", hp=1000, atk=80, dfs=50, crt=15, avd=0)
doggerMan = PlayerChar("돚거맨", hp=700, atk=100, dfs=10, crt=50, avd=0)
hotPunchMan = PlayerChar("매콤주먹맨", hp=800, atk=100, dfs=30, crt=30, avd=0)
normalMan1 = PlayerChar("일반인1", hp=550, atk=50, dfs=0, crt=25, avd=0)
normalMan2 = PlayerChar("일반인2", hp=500, atk=55, dfs=5, crt=20, avd=0)
# 전투 시작
startGame(normalMan1, normalMan2)
