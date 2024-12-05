class Rule:
    def __init__(self, a, b) -> None:
        self.a, self.b = a, b

    def concerned(self, update: list) -> bool:
        return self.a in update and self.b in update

    def check(self, update: list) -> bool:
        if self.a in update and self.b in update:
            if update.index(self.a) > update.index(self.b):
                return False
        return True
    
    def order(self, update: list) -> list:
        index1 = update.index(self.a)
        index2 = update.index(self.b)
        update[index1], update[index2] = update[index2], update[index1]
        return update

rules = open("input_5_rules.txt", "r").read().splitlines()
updates = open("input_5_updates.txt", "r").read().splitlines()

rules_list = []
updates_list = []

for line in rules:
    rules_list.append(Rule(int(line[0:2]), int(line[3:5])))

for line in updates:
    updates_list.append([int(x) for x in line.split(",")])

result = 0

for update in updates_list:
    is_correct = True
    for rule in rules_list:
        if not rule.check(update):
            is_correct = False
            break
    if is_correct:
        result += update[len(update) // 2]

print(result)

result = 0

for update in updates_list:
    is_correct = False
    rules_to_apply = []
    for rule in rules_list:
        if rule.concerned(update):
            rules_to_apply.append(rule)
        if not rule.check(update):
            is_correct = True
    if is_correct:
        is_correct2 = True # .... tf is this
        while is_correct2:
            is_correct2 = False
            for rule in rules_to_apply:
                if not rule.check(update):
                    update = rule.order(update)
                    is_correct2 = True
        result += update[len(update) // 2]

print(result)