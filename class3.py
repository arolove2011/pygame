class God():
    def __init__(self, name, age, country, height, Ruler):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
        self.Ruler = Ruler
    def introduce(self):
        print(f"안녕하세요. 이 사람(?)은 {self.name}이고, 나이는 {self.age}세입니다. {self.country}에서 태어났고, 키는 {self.height}cm이다. 그 정치인이 자주 하는 말은 위대한 {self.Ruler} 님을 찬양해라!입니다.")

a= God('정치인 윤X열씨', 11, '조선 민주주의 인민공화국', 146, '나')
b = God('초등생 안X준씨', 11, '한국', 150, '노시환')
c = God('정치인 이X명씨', 58, '미국', 172, "국민지원금")
d = God('초등생 안지호', 10, '러시아', 108, "손흥민과 나")
e = God('(키가 좀 작지만) 초등생 이재서', 10, '일본', 10, "어쩔티비! 난 말 안 해줄건데?! 하지만 어쩔 수 없다면 나")

a.introduce()
b.introduce()
c.introduce()
d.introduce()
e.introduce()