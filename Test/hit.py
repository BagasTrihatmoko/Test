def fibonacci(x):
	if x <= 2:
		return 1
	else:
		fib = fibonacci(x - 1) + fibonacci(x - 2)
	return fib


print('Menghitung bilangan fibonacci menggunakan fungsi rekursif')
angka = int(input('Masukkan sebuah bilangan '))
fibonacci_bil = fibonacci(angka)
print('Bilangan fibonacci ke-{} adalah {}'.format(angka, fibonacci_bil))
