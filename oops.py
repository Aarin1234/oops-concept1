class Dog:
    #Attributes
    attr1 = 'mammal'
    attr2 = 'dog'

    #function'
    def func(self):
        print('i am a', self.attr1)
        print('i am a ', self.attr2)

#creating objects
shepard = Dog()
chiauaha = Dog()

print(shepard.attr1)
print(chiauaha.attr2)

shepard.func()