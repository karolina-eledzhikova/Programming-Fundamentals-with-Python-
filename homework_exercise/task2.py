v = int(input())  # обем на басейна в литри
p1 = int(input())  # дебит на първата тръба за час
p2 = int(input())  # дебит на втората тръба за час
h = float(input())  # часовете, в които работникът отсъства

water = p1 + p2 * h

x = h+water * 100
y = p1 * water / h * 10
z = p2 * water / h * 100
# Изходни данни
# Да се отпечата на конзолата едно от двете възможни състояния:
#
# До колко се е запълнил басейнът и коя тръба с колко процента е допринесла. Всички проценти да се форматират до цяло число (без закръгляне).
if water <= v:
    print(f"The pool is {x}% full. Pipe 1: {y}. Pipe 2: {z}%.")
# "The pool is [x]% full. Pipe 1: [y]%. Pipe 2: [z]%."
# Ако басейнът се е препълнил – с колко литра е прелял за даденото време, число с плаваща запетая.
else:
    print(f"For {x} hours the pool overflows with {y} liters.")
# "For [x] hours the pool overflows with [y] liters."

# ДЕЙБАААА ШИБАНАТА СКАПАНА ЗАДАЧАААААА!!!!!!!!!!!!!!!