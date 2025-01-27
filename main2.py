# Example
def greet (name='User'):
    print(f'Hello {name}')
greet()
greet('Edgar')
# Example
def priimk_pacienta(pacientas,gydytojas='gyd. Pagalnutylenis'):
    irasas_gyd_zurnale = f'Pacientas {pacientas}, prieme {gydytojas}'
    return irasas_gyd_zurnale

res = priimk_pacienta('Edgaras')
print(res)

res = priimk_pacienta('Edgaras', gydytojas='gyd. Pakeitenis')
print(res)
#  3 task
def three_greetings(name1, name2, name3):
    print(f'Hello {name1}!')
    print(f'Hello {name2}!')
    print(f'Hello {name3}!')
three_greetings('Jonas', 'Tomas','Edgaras')
#  4 task
def greetings_with_position(name,position='friend'):
    print(f'Hello, {name}! What are you doing, {position} ?')
greetings_with_position('Edgar')
greetings_with_position('Edgar', 'collegue')