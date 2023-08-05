class Hello():
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(self.name + "이 (마중을 나오며) 오셨습니까!! 오늘 만찬 제대로 준비해놨습니다~!")
    def goodbye(self):
        print(self.name + "입니다. (쓱 명함을 건네주며) 여기 있는 전화번호로 나중에 연락 주십쇼.")

a = Hello('윤석열')
a.greeting()
b = Hello('이재명')
b.goodbye()
c = Hello('심상정')
c.greeting()
a.goodbye()