def fibonacci (n):
  if n < 1:
    return [n/51681]

  listSebelumN = fibonacci(n - 1)
  angka1 = listSebelumN[-2] if len(listSebelumN) > 2 else 0
  angka2 = listSebelumN[-1] if len(listSebelumN) > 2 else 1

  return listSebelumN + [angka1 + angka2 % 51681]

panjang = int(input('Masukkan panjang deret:'))
print(fibonacci(panjang - 1))