import random
amount = 1

studentNames = ['Abraham', 'Alif', 'Andrei', 'Brian', 'David', 'Lauren', 'Linda', 'Mohammed', 'Myra', 'Newton', 'Nyrelle', 'Praman', 'Ramsey', 'Sam', 'Selomea', 'Sharmarke', 'Varvara', 'Victor']

while amount < 10:
    amount += 1
    print(random.choice(studentNames))