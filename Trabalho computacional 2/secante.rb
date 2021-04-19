def f(x)
	return x ** 2 + x - 6
end

x0 = gets.to_f
x1 = gets.to_f

e8 = gets.to_f
it = gets.to_i

if (f(x0)).abs < e8
	raiz = x0
	puts "raiz = #{raiz}"
	exit(true)

elsif (f(x1)).abs < e8 || (x1-x0).abs < e8
	raiz = x1
	puts "raiz = #{raiz}"
	exit(true)
else
	k = 1
	loop do
		x2 = x1 - ((f(x1) * (x1 - x0)) / (f(x1) - f(x0)))
		if (f(x2)).abs < e8 || (x2 - x1).abs < e8 || k > it
			raiz = x2
			break
		end
		x0 = x1
		x1 = x2
		k = k + 1
		break if (f(x2)).abs < e8
	end

	puts "raiz = #{raiz}"
	puts "iteracoes = #{k}"
end

