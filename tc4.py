import numpy as np

def metodo_newton():
	qtde_pontos = int(input("Quantos pontos?"))
	pontos, fPontos =[], []
	tabela = []
	
	for i in range(qtde_pontos):
		ponto = float(input('x%d=' %i))
		fPonto = float(input('y%d=' %i))
		pontos.append(ponto)
		fPontos.append(fPonto)
	tabela.append(fPontos)

	x = float(input("ponto a ser estimado"))
	
	passo = 1
	for n in range(qtde_pontos - 1):
		ordem =[]
		for m in range(len(tabela[n]) - 1):
			diferencaDividida = (tabela[n][m + 1] - tabela[n][m])/(pontos[m + passo] - pontos[m])
			ordem.append(diferencaDividida)
		tabela.append(ordem)
		passo += 1

	for k in range(len(tabela)):
		print('Ordem %d: '%k, tabela[k])
	print()

	for i in range(len(tabela)):
		fator = tabela[i][0]
		for j in range(grau):
			fator *= (x - pontos[j])
		grau += 1
		aprox += fator

	print('Aproximação encontrada= %f', aprox)

def lagrange(qtde_pontos):
	X, Y = [], []

	for i in range(qtde_pontos):
		x = float(input("x" + str(i) + "="))
		X.append(x)
		y = float(input("y" + str(i) + "="))
		Y.append(y)

	x = float(input("valor a interpolar"))
	coeficientes =[]

	for indice in range(qtde_pontos):
		L = 1
		for j in range(len(X)):
			if indice != j:
				L *= (x - X[j])/(X[indice] - X[j])
		coeficientes.append(L)

	pn = 0

	for i in range(len(coeficientes)):
		pn += Y[i] * coeficientes[i]

	print("p("+str(x)+") = ", pn)

def gregory_newton(m, x, y, z):
	xx = np.arange(0, 0.9, 0.01)
	f = []

	for ii in range(len(xx)):
		y = z
		p = y[0]
		a = []
		h = x[1] - x[0]
		s0 = (xx[ii] - x[0])/h
		s = 1
		a.append(y[0])
		for i in range(m - 1):
			delf = []
			for j in range(m - 1 - i):
				delf.append(y[j + 1] - y[j])
			s *= (s0 - i) / (i + 1)
			p += s * delf[0]
			y = delf
			a.append(y[0])
		f.append(p)
	print(xx[-1], p)

print("----------MENU----------")
print("1 - Newton")
print("2 - Lagrange")
print("3 - Gregory-Newton")
print("------------------------")
print("Informe o método")
met = input()

if met == "1":
	'''
	print("Entradas do exemplo 4.6")
	metodo_newton(4, 0.5, 0, 0)
	'''
	metodo_newton()
elif met == "2":
	qtde_pontos = int(input("Quantos pontos?"))
	lagrange(3)
elif met == "3":
	m = 5
	x = [0, 0.2, 0.4, 0.6, 0.8]
	y = [0.12, 0.46, 0.74, 0.9, 1.2]
	z = y
	gregory_newton(m, x, y, z)
else:
	print("Entrada invalida")
