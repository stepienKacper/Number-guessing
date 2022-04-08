import random
from rich.console import Console
from rich.table import Table

Console = Console()
table = Table()

def wylosuj_liczbe():
    x = random.randint(1, 10)
    return x

def zgaduj():
    a = open('zgadywanie.csv','w')
    result = []
    ilosc = 0
    x = wylosuj_liczbe()
    while True:
        y = int(input('Podaj liczbe: '))
        ilosc += 1
        if y == x:
            print(f'Gratulacje! Zgadles za {ilosc} razem.')
            a.write(f'{ilosc};Zgadnięto\n')
            break
        if y > x:
            print('Lower')
            a.write(f'{ilosc};Lower\n')
        if x > y:
            print('Higher')
            a.write(f'{ilosc};Higher\n')
    a.close()
    return result

def zgadywanie():
    file = open('zgadywanie.csv', 'r')
    results = []
    try:
        for line in file:
            line_strip = line.strip()
            line_split = line_strip.split(";")
            results.append(line_split)
        return results
    except:
        return False


def main():
    zgaduj()
    results = zgadywanie()
    table.add_column('Próba', min_width=10)
    table.add_column('Odpowiedz',min_width=20)
    for x in results:
        table.add_row(x[0],x[1])
    Console.print(table)

if __name__ == '__main__':
    main()
