# class Fighter(object):
#     def __init__(self, model, missle):
#         self.model = model
#         self.missle= missle
#     def attack(self):
#         print(self.model + "출격!")
#     def fire(self):
#         print(self.missle + "발사!")

# fighter1= Fighter("김현우", "미사일")
# fighter1.attack()
# fighter1.fire()
# fighter2 = Fighter("푸틴", "ICBM")
# fighter2.attack()
# fighter2.fire()

def fire(name):
    print(name + "출격!")
def attack(name):
    print(name + "발사!!")

fire("푸틴 ")
attack("미사일 ")