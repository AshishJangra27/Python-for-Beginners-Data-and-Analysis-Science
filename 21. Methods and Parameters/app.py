
class agent:
    def __init__(self, name, age):
        print('Welcome to the Game')
        self.name = name
        self.age = age
        self.health = 100
        self.alive = True

    def curr_health(self):
        print('Current Health of', self.name ,'is',self.health)

    def punched(self):
        self.health -= 10

    def shooted(self):
        self.health -= 50

    def is_alive(self):
        if self.health == 0:
            self.alive = False

    def info(self):
        print('Name    : ', self.name)
        print('Age     : ', self.age)
        print('Health  : ', self.health)
        print('Alive   : ', self.alive)


p1 = agent('Ashish',25)
p1.curr_health()
p1.punched()
p1.shooted()
p1.info()
print('-'*30)

p2 = agent('Ankur',26)
p2.curr_health()
p2.shooted()
p2.shooted()
p2.info()


print('*'*50)

class boss(agent):


    def blow_fire(self):
        print('blow fire!')

bs = boss('Kilvish',1000)
bs.info()
bs.blow_fire()
