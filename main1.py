# Example
name = 'Edgar'

def create_greetings(user):
    if not user:
        return
    res = f'Greetings, {user}!'
    return res

greetings = create_greetings(name)
if greetings:
    print(greetings)
else:
    print('User not found')
# 2 task
def multiply(x,y):
    return x * y

result = multiply(5,10)
print(f'Result is: {result}')
