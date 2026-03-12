score = 0
print("=== Quiz Sederhana ===")

print("\n1. Apa Ibu Kota Indonesia?")
print('a. Bandung')
print('b. Surabaya')
print('c. Jakarta')
jawaban = input(('Jawaban kamu (a-c): '))

if jawaban == 'c':
    print('Benar!')
    score += 1
else:
    print("Salah!")
    print('Jawaban yang benar adalah = c.Jakarta')

print("\n2. 5 + 3 = ?")
print('a. 11')
print('b. 8')
print('c. 7')
jawaban = input(('Jawaban kamu (a-c): '))

if jawaban == 'b':
    print("Benar!")
    score += 1
else:
    print('Salah!')
    print('Jawaban yang benar adalah = b.8')    

print("\n3. Apa Ibu Kota China?")
print('a. Shanghai')
print('b. Taipei')
print('c. Beijing')
jawaban = input(('Jawaban kamu : '))

if jawaban == 'a':
    print("Benar!")
    score += 1
else:
    print('Salah!')
    print("Jawaban yang benar adalah = a.Shanghai")

print('\nTotal score kamu = ', score)        
