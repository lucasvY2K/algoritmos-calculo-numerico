puts("Determine os intervalos da raiz")
a = gets.chomp.to_i
b = gets.chomp.to_i

puts("Determine a precisão da raiz")
precisao = gets.chomp.to_f

puts("Determine o numero maximo de iteracoes")
n = gets.chomp.to_i

k = 0
if (b - a).abs < precisao
	puts "Sem raiz"
else
	while (b-a).abs > precisao && k < n
		k = k + 1
		finicio = f(a)
		meio = (a.to_f + b) / 2
		fmeio = f(meio)
		if finicio*fmeio < 0
			b = meio			
		else
			a = meio
		end
	end
	puts "raiz = #{meio}"
	puts "interações = #{k}"
end

def f(x)
	return x**3 - 10
end