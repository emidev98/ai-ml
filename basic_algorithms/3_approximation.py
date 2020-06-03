objective = int(input("Insert a number : "))
epsilon = 0.01
step = epsilon**2
response = 0.0

while abs(response**2 - objective) >= epsilon and response <= objective:
    response += step;

if abs(response**2 - objective) >= epsilon:
    print(f'No square found for {objective}')
else:
    print(f'The square of {objective} is {response}')