def read_file():

    lista = []
    listb = []
    file = open("input_1.txt", "r").readlines()
    for line in file:
        lista.append(int(line.split()[0]))
        listb.append(int(line.split()[1]))
    return lista, listb

def distance_list(lista: list, listb: list) -> int:

    assert len(lista) == len(listb), "Error"
    lista.sort()
    listb.sort()
    result = 0
    for i in range(len(lista)):
        result += abs(lista[i] - listb[i])
    
    return result

lista, listb = read_file()
print(distance_list(lista, listb))

def similarity_score(lista: list, listb: list) -> int:

    assert len(lista) == len(listb), "Error"
    dic_count = {}
    result = 0
    for i in lista:
        if not i in dic_count.keys():
            dic_count[i] = listb.count(i)
        result += int(i) * dic_count[i]

    return result

print(similarity_score(lista, listb))
