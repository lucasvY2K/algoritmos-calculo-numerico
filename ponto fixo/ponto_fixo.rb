def f(x)
	return x**2 - x - 2
end

def fi(x)
	return x**2 - 2
end

puts "Informe a aproximacao inicial(x0)"
x0 = gets.chomp.to_f

puts "Informe a precisao"
precisao = gets.chomp.to_f

puts "Informe o numero maximo de iteracoes"
it = gets.chomp.to_i

if (f(x0)).abs < precisao
	puts "raiz = #{x0}"
	exit
else
	k = 1
	loop do
		x1 = fi(x0)
		if (f(x1)).abs < precisao || (x1 - x0).abs < precisao || k > it
			puts "raiz = #{x1}"
			exit
		end
		x0 = x1
		k = k + 1
		break if (f(x1)).abs < precisao
	end
end
