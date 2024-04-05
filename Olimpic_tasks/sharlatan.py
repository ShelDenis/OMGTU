from sympy import symbols, Eq, solve


uravnenie = 'x'
n = int(input())
for i in range(n):
    s = input()
    if s[0] in '+-':
        uravnenie += ' ' + s
    else:
        uravnenie = f'({uravnenie}) ' + s
result = int(input())
x = symbols('x')
equal = Eq(eval(uravnenie), result)
solution = solve(equal, x)
print(solution[0])
