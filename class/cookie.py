class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie('blue')
cookie_two = Cookie('green')

cookie_one.set_color('cyan')

print('Cookie One is: ', cookie_one.get_color())
print('Cookie Two is: ', cookie_two.get_color())
