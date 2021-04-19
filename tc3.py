import math
import time

def gauss(A, b):
	for i in range(len(A)):
		pivo = math.fabs(A[i][i])
		linhaPivo = i
		for j in range(i+1, len(A)):
			if math.fabs(A[j][i]) > pivo:
				pivo = math.fabs(A[j][i])
				linhaPivo = j
		if linhaPivo != i:
			linhaAux = A[i]
			A[i] = A[linhaPivo]
			A[linhaPivo] = linhaAux

			bAux = b[i]
			b[i] = b[linhaPivo]
			b[linhaPivo] = bAux

		for m in range(i+1, len(A)):
			mult = A[m][i]/A[i][i]
			for n in range(i, len(A)):
				A[m][n] -= mult*A[i][n]
			b[m] -= mult * b[i]

	for k in range(len(A)):
		print(A[k])
	print()
	
	solucao(A, b)


def lu(n, A, b):    
        for k in range (0, n-1):        
            for i in range (k+1, n):            
                if (abs(A[k][k]) < abs(A[i][k])):
                    for j in range (0,n):
                        aux=A[k][j]
                        A[k][j]=A[i][j]
                        A[i][j]=aux
                    aux = b[k]
                    b[k]=b[i]
                    b[i]=aux
                m = -A[i][k]/A[k][k]
                A[i][k] = 0
                for j in range (k+1, n):
                    A[i][j] = A[i][j] + m*A[k][j]
                b[i] = b[i] + m*b[k]        
        solucao(A, b)

def gauss_jacobi(A, b, vetSolucao, it):
	ite = 0
	vetAux = []

	for k in range(len(vetSolucao)):
		vetAux.append(0)
	
	while ite < it:
		for i in range(len(A)):
			x = b[i]
			for j in range(len(A)):
				if i != j:
					x -= A[i][j] * vetSolucao[j]
			x /= A[i][i]
			vetAux[i] = x
		ite += 1
		vetSolucao = vetAux

		for p in range(len(vetAux)):
			vetSolucao[p] = vetAux[p]
	print(vetSolucao)

def gauss_seidel(A, b, vetSolucao, it):
	ite = 0

	while ite < it:
		for i in range(len(A)):
			x = b[i]
			for j in range(len(A)):
				if i != j:
					x -= A[i][j] * vetSolucao[j]

			x /= A[i][i]
			vetSolucao[i] = x
		ite += 1

	print(vetSolucao)


def solucao(A, b):
	vetSolucao = []
	
	for i in range(len(A)):
		vetSolucao.append(0)
	
	linha = len(A) - 1
	
	while linha >= 0:
		x = b[linha]
		coluna = len(A) - 1
		while coluna > linha:
			x -= A[linha][coluna] * vetSolucao[coluna]
			coluna -= 1
		x /= A[linha][linha]
		linha -= 1
		vetSolucao[coluna] = x

	for j in range(len(vetSolucao)):
		print(vetSolucao[j], " ")

def print_matriz(A):
	for k in range(len(A)):
		print(A[k])
	print()

A = [[8772, 1296, 204], 
	 [1296, 204, 36], 
	 [204, 36, 8]]

b = [590.6, 50.5, 9.2]

Ag = [[10, 2, 1],
	 [1, 5, 1],
	 [2, 3, 10]]
bg = [7, -8, 6]
vetSolucao = [0.7, -1.6, 0.6]

Ags =[[5, 1, 1],
	  [3, 4, 1],
	  [3, 3, 6]]
bgs = [5, 6, 0]
vetSolucaogs = [0, 0, 0]

print("----------MENU----------")
print("1 - Eliminacao de Gauss")
print("2 - Fatoracao LU")
print("3 - Metodo de Gauss-Jacobi")
print("4 - Metodo de Gauss-Seidel")
print("------------------------")
time.sleep(2)
print("Informe o método")
met = input()

if met == "1":
	print_matriz(A)
	print("resolvendo")
	time.sleep(2)
	gauss(A, b)
elif met == "2":
	print_matriz(A)
	print("resolvendo")
	time.sleep(2)
	lu(len(A), A, b)
elif met == "3":
	print_matriz(Ag)
	print("resolvendo")
	time.sleep(2)
	gauss_jacobi(Ag, bg, vetSolucao, 2)
elif met == "4":
	print_matriz(Ags)
	print("resolvendo")
	time.sleep(2)
	gauss_seidel(Ags, bgs, vetSolucaogs, 3)
else:
	print("Entrada invalida")




