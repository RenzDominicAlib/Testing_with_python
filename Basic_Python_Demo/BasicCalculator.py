class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2

    def multi(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

Calculate = BasicCalculator(10,5)
print(f'Addition: {Calculate.add(10,5)}')
print(f'Subtraction: {Calculate.sub(10,5)}')
print(f'Multiplication: {Calculate.multi(10,5)}')
print(f'Division: {Calculate.divide(10,5)}')

print(f'********************************************************')


def GreetUser(name):
    print(f'Hello, {name}! Welcome to the Python course.')
GreetUser('John')

print(f'********************************************************')

num1 = 10
num2 = 20
num3 = 30

def CalculateAverage(num1, num2, num3):
    sum = num1 + num2 + num3
    return sum / 3


print(f'The average of {num1}, {num2}, and {num3} is {CalculateAverage(num1, num2, num3)}')
print(f'********************************************************')




def add_to_cart(items_to_add):
    itemsInCart = 0
    itemsInCart = itemsInCart + items_to_add

    try:
        print(f'{items_to_add} items added. Total in cart: {itemsInCart}')
        if itemsInCart > 5:
            print("Cart limit exceeded")
            raise Exception
        if itemsInCart < 0:
            print("Cannot add a negative number of items.")
            raise Exception

    except Exception as e:
        print(e)


add_to_cart(-2)