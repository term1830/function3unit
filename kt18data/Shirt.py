#classes attributes/properties


class Shirt():
    def __init__(self, color,size,price,fit = 'Normal'):
        self.color = color
        self.size = size
        self.price = price
        self.fit = fit
    def fold(self):
        print(f'fold the {self.size} {self.color} shirt')

if __name__ == "__main__":
    shirt = Shirt("Green",'Small', 50.25)
    print(shirt.color,shirt.size,shirt.price)
    shirt.fold()
    breakpoint()
