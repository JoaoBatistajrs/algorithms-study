def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    print(f" teste {right}")
    steps = 0  # Contador de tentativas

    while left <= right:
        steps += 1  # Incrementa o contador a cada iteração
        mid = (left + right) // 2  # Pega o meio da lista

        if lst[mid] == target:
            return mid, steps  # Retorna o índice e a quantidade de tentativas
        if lst[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return None, steps  # Se não encontrar, retorna None e o número de tentativas


# Criando listas com 128 e 256 elementos
my_list_128 = list(range(1, 129))  # [1, 2, 3, ..., 128]
my_list_256 = list(range(1, 257))  # [1, 2, 3, ..., 256]

# Testando a busca para um número no meio da lista
index_128, attempts_128 = binary_search(my_list_128, 82)
index_256, attempts_256 = binary_search(my_list_256, 210)

print(f"Lista com 128 elementos: Encontrado no índice {index_128} em {attempts_128} tentativas.")
print(f"Lista com 256 elementos: Encontrado no índice {index_256} em {attempts_256} tentativas.")

#O Big O da pesquisa binária é O(log n) (logaritmo de base 2).

# Explicação:
# A cada iteração, a busca binária divide o espaço de busca pela metade.

# Isso significa que, se tivermos 
# 𝑛
# n elementos, o número máximo de comparações necessárias é log 2 n.


# Esse crescimento logarítmico faz com que a busca binária seja muito eficiente mesmo para grandes conjuntos de dados.

# Comparação com outros algoritmos de busca:
# Algoritmo	Complexidade	Exemplo (n = 1.000.000)
# Busca linear	O(n)	1.000.000 comparações (pior caso)
# Busca binária	O(log n)	~20 comparações
# Se tivermos uma lista com 1.000.000 de elementos:

# Busca linear (O(n)) → No pior caso, precisa de 1.000.000 comparações.

# Busca binária (O(log n)) → Precisa de apenas 20 comparações!

# Isso mostra o quanto a busca binária é eficiente para grandes conjuntos de dados.