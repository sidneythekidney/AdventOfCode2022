import math

NUMBER_OF_ROUNDS = 10000
MONKEY_EASY_LCM = 1

class Monkey:
    def __init__(self, input_txt):
        # Parse input text
        self.current_items = [int(item) for item in input_txt[1].split(': ')[1].split(', ')]
        self.operation = input_txt[2].split(': ')[1].split(' ')[2:]
        self.test = int(input_txt[3].split(' ')[3])
        self.if_true = int(input_txt[4].split(' ')[5])
        self.if_false = int(input_txt[5].split(' ')[5])
        self.inspected_items = 0

    def inspect_objects(self):
        thrown_objects = []
        for item in self.current_items:
            self.inspected_items += 1
            new_worry_level = self.calculate_new_worry_level(item)
            # Determine where to throw object
            if new_worry_level % self.test == 0:
                thrown_objects.append([self.if_true, new_worry_level])
            else:
                thrown_objects.append([self.if_false, new_worry_level])
        self.current_items = []
        return thrown_objects

    def calculate_new_worry_level(self, worry_level):
        first_term = self.operation[0]
        second_term = self.operation[2]

        # Parse first term
        if first_term.isnumeric():
            first_term = int(first_term)
        elif first_term == 'old':
            first_term = worry_level
        else:
            print("Couldln't parse value from operation " + first_term)
            exit(1)

        # Parse second term
        if second_term.isnumeric():
            second_term = int(second_term)
        elif second_term == 'old':
            second_term = worry_level
        else:
            print("Couldln't parse value from operation " + second_term)
            exit(1)

        # Perform operation
        if self.operation[1] == '+':
            return math.floor((first_term + second_term)) % MONKEY_EASY_LCM
        elif self.operation[1] == '-':
            return math.floor((first_term - second_term)) % MONKEY_EASY_LCM
        elif self.operation[1] == '*':
            return math.floor((first_term * second_term)) % MONKEY_EASY_LCM
        elif self.operation[1] == '/':
            return math.floor((first_term / second_term)) % MONKEY_EASY_LCM
        else:
            print("Couldln't parse value from operation " + self.operation[1])
            exit(1)

# Parse input text for eqach monkey
with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

monkey_txt = []
monkeys = []
for line in lines:
    if len(line) == 0:
        monkeys.append(Monkey(monkey_txt))
        monkey_txt = []
    else:
        monkey_txt.append(line)
monkeys.append(Monkey(monkey_txt))

for monkey in monkeys:
    MONKEY_EASY_LCM *= monkey.test

# Go through all of the monke ys and have them inspect items
for round in range(NUMBER_OF_ROUNDS):
    for monkey in monkeys:
        thrown_objects = monkey.inspect_objects()
        # Give thrown items to appropriate monkeys
        for thrown_object in thrown_objects:
            monkeys[thrown_object[0]].current_items.append(thrown_object[1])

# Calculate the top 2 monkey inspectors to get monkey business
monkey_business_list = [monkey.inspected_items for monkey in monkeys]
monkey_business_list.sort()

print("Monkey business: " + str(monkey_business_list[-1] * monkey_business_list[-2]))
