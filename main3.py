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
# 5 task
