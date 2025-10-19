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
chihuahua = Dog()

print(shepard.attr1)
print(chihuahua.attr2)


shepard.func()
