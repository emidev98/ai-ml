objective = int(input("Chose a number : "))
epsilon = 0.01 
minimum = 0
maximum = max(1.0, objective)
response = (minimum + maximum) / 2

while abs(response**2 - objective) >= epsilon:
    print(f'minimum={minimum},maximum={maximum},response={response}')
    if response**2 < objective:
        minimum = response
    else:
        maximum = response

    response = (minimum + maximum) / 2

print(f"The square of {objective} is {response}")