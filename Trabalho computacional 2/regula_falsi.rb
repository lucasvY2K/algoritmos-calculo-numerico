def f(x)
	return x * Math.log(x) - 1
end

a = gets.to_i
b = gets.to_i

delta1 = gets.to_f
delta2 = gets.to_f

it = gets.to_i

if (b - a).abs < delta1
	raiz = 1
	puts "raiz = #{raiz}"
	exit(true)
elsif (f(a)).abs < delta2 || (f(b)).abs < delta2
	raiz = a
	puts "raiz = #{raiz}"
	exit(true)
else
	k = 1
	loop do
		m = f(a)
		x = ((a * f(b)) - (b * f(a))) / (f(b) - f(a))
		if (f(x)).abs < delta2 || k > it
			raiz = x
			puts "raiz #{raiz}"
		elsif m * f(x) > 0
			a = x
			if (b - a).abs < delta1
				raiz = (a + b) / 2
				puts "raiz #{raiz}"
				exit(true)
			end
		b = x
		k = k + 1
		end
		break if f(x).abs < delta1
	end
end
	