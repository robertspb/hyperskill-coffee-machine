class CoffeeMachine():

    resourses = {'water': 400, 'milk': 540, 'coffee beans': 120, 'disposable cups': 9, 'money': 550}
    espresso = {'water': 250, 'milk': 0, 'beans': 16, 'price': 4}
    latte = {'water': 350, 'milk': 75, 'beans': 20, 'price': 7}
    cappuccino = {'water': 200, 'milk': 100, 'beans': 12, 'price': 6}
    state = 'choosing an action'

    def start(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):")
            if action == 'buy':
                self.buy()
            elif action == 'fill':
                self.fill()
            elif action == 'take':
                self.take()
            elif action == 'remaining':
                self.remaining()
            elif action == 'exit':
                break

    def remaining(self):
        print("The coffee machine has:")
        for res, val in self.resourses.items():
            print(f"{'$' if res == 'money' else ''}{val} of {res}")

    def take(self):
        print("I gave you $" + str(self.resourses['money']))
        self.resourses['money'] = 0

    def buy(self):
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        if coffee == '1':
            self.coffee_preparing(self.espresso)
        elif coffee == '2':
            self.coffee_preparing(self.latte)
        elif coffee == '3':
            self.coffee_preparing(self.cappuccino)
        elif coffee == 'back':
            return

    def coffee_preparing(self, coffee):
        if coffee['water'] <= self.resourses['water']\
                and coffee['milk'] <= self.resourses['milk']\
                and coffee['beans'] <= self.resourses['coffee beans']\
                and self.resourses['disposable cups'] >= 1:
            self.resourses['water'] -= coffee['water']
            self.resourses['milk'] -= coffee['milk']
            self.resourses['coffee beans'] -= coffee['beans']
            self.resourses['disposable cups'] -= 1
            self.resourses['money'] += coffee['price']
            print('I have enough resources, making you a coffee!')
        else:
            if self.resourses['water'] < coffee['water']:
                print('Sorry, not enough water!')
            if self.resourses['milk'] < coffee['milk']:
                print('Sorry, not enough milk!')
            if self.resourses['coffee beans'] < coffee['beans']:
                print('Sorry, not enough beans!')
            if self.resourses['disposable cups'] < 1:
                print('Sorry, not enough cups!')

    def fill(self):
        water_add = int(input("Write how many ml of water do you want to add:"))
        milk_add = int(input("Write how many ml of milk do you want to add:"))
        beans_add = int(input("Write how many grams of coffee beans do you want to add:"))
        cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))
        self.resourses['water'] += water_add
        self.resourses['milk'] += milk_add
        self.resourses['coffee beans'] += beans_add
        self.resourses['disposable cups'] += cups_add


coffee_machine = CoffeeMachine()
coffee_machine.start()
