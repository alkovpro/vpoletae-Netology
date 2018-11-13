class Animal:
    def __init__(self, name, weight, value, voice):
        self.name = name
        self.weight = weight
        self.value = value
        self.voice = voice

    def __str__(self):
        return str(self.name,
                   self.weight,
                   self.value,
                   self.voice,)

    def feed(self):
        self.weight  += 1
        print('Mhmhmh...')

    def collect_value(self):
        self.weight  -= 1
        print('{} is/are collected'.format(self.value.capitalize()))

    def raise_voice(self):
        print(self.voice.upper())


class Goose(Animal):
    def __init__(self, name):
        self.name = name
        self.weight = 20
        self.value = 'eggs'
        self.voice = 'Gagaga'

class Cow:
    def __init__(self, name):
        self.name = name
        self.weight = 100
        self.value = 'milk'
        self.voice = 'Moo'

class Sheep:
    def __init__(self, name):
        self.name = name
        self.weight = 45
        self.value = 'wool'
        self.voice = 'Mee'
        
class Hen:
    def __init__(self, name):
        self.name = name
        self.weight = 7
        self.value = 'eggs'
        self.voice = 'Ku-ka-re-ku'

class Goat:
    def __init__(self, name):
        self.name = name
        self.weight = 45
        self.value = 'milk'
        self.voice = 'Bee'

class Duck:
    def __init__(self, name):
        self.name = name
        self.weight = 10
        self.value = 'eggs'
        self.voice = 'Krya'

goose_1 = Goose('Grey')
goose_2 = Goose('White')
cow = Cow('Manka')
sheep_1 = Sheep('Barashek')
sheep_2 = Sheep('Curvy')
hen_1 = Hen('Ko-Ko')
hen_2 = Hen('Kukareku')
goat_1 = Goat('Roga')
goat_2 = Goat('Kopyta')
duck = Duck('Kryakva')

farm = [goose_1, goose_2, cow, sheep_1, sheep_2, hen_1, hen_2, goat_1, goat_2, duck]
total_weight = int()
top_weight = int()
the_heaviest = str()

for animal in farm:
    total_weight += animal.weight
    if animal.weight > top_weight:
        top_weight = animal.weight
        the_heaviest = animal.name
    else:
        continue

print ('Total weight: {}'.format(total_weight))
print ('The heaviest is: {0}, her weight is {1}'.format(the_heaviest, top_weight))



