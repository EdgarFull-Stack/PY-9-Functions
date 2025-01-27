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
