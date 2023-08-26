#CONSTRUTOR DE CLASSE __INIT__()
class Televisao:
    def __init__(self):
        self.volume = 10
    def aumentarVolume(self):
        self.volume += 1
    def diminuirVolume(self):
        self.volume -= 1

tv = Televisao()
print("Volume ao ligar a tv = ", tv.volume)
tv.aumentarVolume()
print("Volume atual =", tv.volume)
