class Animal:
    def __init__(self, name, weight, value, voice):
        self.name = name
        self.weight = weight
        self.value = value
        self.voice = voice

    def __str__(self):
        return str(self.name), str(self.weight), str(self.value), str(self.voice)

    def feed(self):
        self.weight  += 1
        print('Mhmhmh...')

    def collect_value(self):
        self.weight  -= 1
        print('{} is/are collected'.format(self.value.capitalize()))

    def raise_voice(self):
        print(self.voice.upper())


class Goose(Animal):
    
    def feed(self):
        print('Lets give Goose corn')
        self.weight  += 0.3
        
    def collect_value(self):
        self.weight  -= 0.5
        print('{0} is/are collected. {1}'.format(self.value.capitalize(), self.voice.lower()))

class Cow(Animal):

    def feed(self):
        print('Lets give Cow more grass')
        self.weight  += 2

    def collect_value(self):
        self.weight  -= 2
        print('{0} is/are collected. {1}'.format(self.value.capitalize(), self.voice.upper()))

class Sheep(Animal):

    def feed(self):
        print('Lets give Sheep grass')
        self.weight  += 0.3

    def collect_value(self):
        self.weight  -= 2
        print('{0} is/are collected!!'.format(self.value.capitalize()))
        
class Hen(Animal):
  
    def feed(self):
        print('Lets give Hen corn')
        self.weight  += 0.2

    def collect_value(self):
        self.weight  -= 1
        print('{0} is/are collected. {1}'.format(self.value.capitalize(), self.voice.upper()))
        
class Goat(Animal):
    
    def feed(self):
        print('Lets give Goat as a Sheep grass')
        self.weight  += 0.5

class Duck(Animal):
    
    def feed(self):
        print('Lets give Duck corn - much less than Cow')
        self.weight  += 0.3

    def collect_value(self):
        self.weight  -= 0.3
        print('{0} is/are collected. {1}'.format(self.value.capitalize(), self.voice.capitalize()))

goose_1 = Goose('Grey', 5, 'eggs', 'Ga')
goose_2 = Goose('White', 3, 'eggs', 'GAGA!')
cow = Cow('Manka', 100, 'milk', 'Mooow')
sheep_1 = Sheep('Barashek', 23, 'wool', 'Be-Be')
sheep_2 = Sheep('Curvy', 18, 'wool', 'Be!!')
hen_1 = Hen('Ko-Ko', 3, 'EGGS', 'Koko-ku-ka-reku')
hen_2 = Hen('Kukareku', 4, 'eggs', 'Koko')
goat_1 = Goat('Roga', 8, 'goat-milk', 'Me')
goat_2 = Goat('Kopyta', 7, 'goat-milk', 'Fuck Myeh')
duck = Duck('Kryakva', 3, 'duck eggs', 'Krya')

farm = [goose_1, goose_2, cow, sheep_1, sheep_2, hen_1, hen_2, goat_1, goat_2, duck]
total_weight = int()
top_weight = int()
the_heaviest = str()

# feed all animals
def feed_all():
    for animal in farm:
        animal.feed()
        print("{0}'s new weight is: {1}".format(animal.name, animal.weight))
      
# collect value from all animals
def collect_all():
    for animal in farm:
        animal.collect_value()
        print('{0} gave us: {1}'.format(animal.name, animal.value))
        
# measure total weight and the heaviest
def measure_weight():
    global total_weight
    global top_weight
    for animal in farm:
        total_weight += animal.weight
        if animal.weight > top_weight:
            top_weight = animal.weight
            the_heaviest = animal.name
        else:
            continue
    print ('Total weight: {}'.format(total_weight))
    print ('The heaviest is: {0}, her weight is {1}'.format(the_heaviest, top_weight))

feed_all()
collect_all()
measure_weight()

