# Example
def dalink_spec(sk1, sk2, iki_sveiko_sk=False):
    if not iki_sveiko_sk:
        return sk1 / sk2
    return sk1 // sk2
print(dalink_spec(100,27, True))
# Example
def say_hello(name):
    """
    Priima vardą ir atspausdina pasisveikinimą.
    :param name: str - vardas žmogaus
    :return: None
    """
    print(f"Hello, {name}")
say_hello('Edgar')
# Example
def add(x: int, y: int) -> int:
    return x + y
res = add(10, 10)

# 5 task
def skaiciuoti_sumos_tipą(x: int, y: int, tik_teigiama=False) -> int:
    """
    Skaicuoja suma
    :param x: Pirmasis skaičius.
    :param y:Antrasis skaičius.
    :param tik_teigiama:Jei True, grąžins tik teigiamą sumą. Jei suma neigiama, grąžins 0. Numatytoji reikšmė - False.
    """
    sum = x+y
    if tik_teigiama and sum<0:
        return 0
    return sum
print(skaiciuoti_sumos_tipą(3,-5,True))

# 6 task
def apskaiciuok_vidurki(skaiciai):
    """
      Apskaičiuoja ir grąžina pateikto sąrašo skaičių vidurkį.
      :param skaiciai: Sąrašas skaičių (int arba float).
      Grąžina: float: Skaičių vidurkis. Jei sąrašas tuščias, grąžina 0.
    """
    if not skaiciai:
        return 0
    return sum(skaiciai)/len(skaiciai)
print(apskaiciuok_vidurki([1,2,3,4,5,6]))

# 7 task
def prideti_zodi(tekstas: str, zodis: str) -> str:
    """
    Prideda nurodytą žodį prie pateikto teksto galo ir grąžina atnaujintą tekstą.
    :param tekstas: Pradinis tekstas (sakinys).
    :param zodis: Žodis, kurį reikia pridėti prie teksto galo.
    """
    return f'{tekstas} {zodis}'
print(prideti_zodi('Sveiki pone','drauge'))
