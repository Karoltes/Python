
# x to wektor wszystkich zmiennych objaśniających, na jego podstawie będę generował kombinacje
# dla ulatwienia wykonywania algorytmu na petlach itp numeruje je od 0 zamiast od 1
# r0 to wektor korelacji między Y a kolejnymi X
# r to macierz korealcji X między sobą w formie pythonowej "listy list"
# n to liczba zmiennych objaśniających

x = []
r = []
r0 = []
n = 0


# wczytuję dane z pliku
with open('data.txt', 'r') as file:
    data = file.read().splitlines()
    r0 = data[0].split(sep=';')
    r0 = [float(j) for j in r0]
    n = len(r0)
    x = [i for i in range(0, n)]
    for i in range(1, n+1):
        data[i] = data[i].split(sep=';')
        data[i] = [float(j) for j in data[i]]
        r.append(data[i])

# x_combo to lista wszystkich kombinacji
x_combo = []
length = len(x)

# tutaj generuję wszystkie kombinacje wykorzystują postać bitową
# każda kombinacja zmiennych X np dla n=3 X0,X2 ma swoj odpowiednik w masce 101, X0,X1 w 110 itd
# przechodzac przez kazda maske poczawszy (dla n=3) od 000 konczac na 111 (kombinacja 000 jest odcinana na koniec algorytmu) generuję wszystkie kombinacje
#
for mask in range((1 << length)):
    comb = []
    for pos in range(length):
        # w tym momencie konfrontuję z bitowym przesunięciem zmiennej X (pos) za pomocą koniunkcji binarnej
        # koniunkcja binarna "sprawdza" czy dana zmienna pasuje do maski i jeśli tak to dołącza do kombinacji zmienną
        if mask & (1 << pos):
            comb.append(x[pos])
    # gotową kombinację dołaczam do listy kombinacji
    x_combo.append(comb)

# usuwam pierwszą kombinację ze wzgledu na to że jest ona pusta
x_combo = x_combo[1:]

# H to lista wszystkich integralnych wskaznikow pojemności informacyjnej
# poj_h i poj_H to kolejno: pojedynczy indywidualny wskaźnik pojemności informacyjnej i pojedynczy integralny wskaźnik pojemności
# informacyjnej dla kombinacji z listy x_combo

H = []

for comb in x_combo:
    poj_H = 0
    poj_h = 0
    for h in comb:
        # tutaj obliczam wskaźniki na podstawie kombinacji, traktuje wartości z każdej kombinacji jako indeksy macierzy
        rij = 1
        for h_i in range(n):
            # sprawdzam czy dana zmienna występuje w kombinacji i czy nie jest ona rowna zmiennej dla indeksu h
            # z gory ustalam poczatkową wartość sumy rij jako 1 wiec nie biorę pod uwagę wartości dla np r[0][0]
            if h_i in comb and h_i != h:
                rij += abs(r[h][h_i])
        # liczę indywidualne wskaźniki i dodaję je do integralnego wskaźnika
        poj_h = (r0[h]**2 / rij)
        poj_H += poj_h
    # dokladam gotowy integralny wskaznik dla kombinacji comb
    H.append(poj_H)

# wyliczam maksymalny wskaznik z listy H
print(max(H))



