def f(x)
	return ((x ** 3) - (9 * x) + 3)
end

def f_derivada(x)
	return (3 * (x ** 2) - 9)
end

x0 = gets.to_f
e8 = gets.to_f
it = gets.to_i

fx = f(x0)

if fx.abs > e8
	k = 1
	fxlinha = f_derivada(x0)
	x1 = x0 - (fx/fxlinha)
	fx = f(x1)
	while fx.abs > e8 && (x1 - x0).abs > e8
		k = k + 1
		x0 = x1
		fxlinha = f_derivada(x0)
		x1 = x0 - (fx/fxlinha)
		fx = f(x1)
	end
	raiz = x1
else
	raiz = x0
end

puts "raiz = #{raiz}"
puts "iteracoes = #{k}"
