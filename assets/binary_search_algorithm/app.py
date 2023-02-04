# uma função que pega uma lista e um parâmetro
# várias variáveis: middle, start, end, steps
# recurdion ou while loops
# aumentar as etapas cada vez que é dividido
# condições para acompanhar a posição do nº escolhido

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0

    while (start <= end):
        print("Etapa ", steps, ":" , (list[start:end+1]))

        steps =  steps + 1 
        middle = (start + end) // 2

        if element == list[middle]:
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1 
    
    return -1

my_list = [1,2,3,4,5,6,7,8,9]
target = 7

binary_search(my_list, target)


