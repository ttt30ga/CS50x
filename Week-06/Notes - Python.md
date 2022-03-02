# CS50 Week 6 - Python

[Watch lecture on Youtube](https://youtu.be/ky-24RvI57s)

---

## Hello World

```
print("Hello, world")
```

## If conditional and indentation

```
if x < y:
	print("Hello, world\n")
elif:
	print("Not hello, world")
else:
	print("Hello, moon")
```

## While Loop

```
while True:
	print("Hello, world\n")
```

```
i = 0
while True:
	print("Hello, world\n")
	i += 1 // Equal to i ++
```

## For Loop

```
for i in [0, 1, 2]:
	print("Hello, world\n")
```

```
for i in range(3):
	print("Hello, world\n")
```

## Types

`bool`\
`float`\
`int`\
`str`\
`range`\
`list`\
`touple`\
`dict`\
`set`

## hello.py

```
from cs50 import get_string

# With cs50 lib
answer1 = get_string("What's your name? ")
print("Hello, " + answer1)

# Without cs50 lib
answer2 = input("How old are you? ")
print(f"{answer2}")
```

## calculator.py

```
from cs50 import get_int

# With cs50 lib
x = get_int("x: ")
y = get_int("y: ")
print(x + y)

# Without cs50 lib
x = int(input("x: "))
y = int(input("y: "))
print(x + y)
```

## Catch error

```
try:
    x = int(input("x: "))
except ValueError:
    print("Error, you can only type numbers")
    exit()
try:
    y = int(input("y: "))
except ValueError:
    print("Error, you can only type numbers")
    exit()
print(x + y)
```

## Divide

```
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

z = x / y
print(f"Result {z}")
```

`x: 1`\
`x: 10`\
`Result: 0.1`

```
z = x // y
```

`x: 1`\
`x: 10`\
`Result: 0`

> Double salsh `//` will return an int like C Lang

## Floating Point Imprecision

```
from cs50 import get_int

x = get_int("x: ")
y = get_int("y: ")

z = x / y
print(f"Result {z}")
```

`x: 1`\
`x: 10`\
`Result: 0.1`

```
print(f"Result {z:.50f}")
```

`x: 1`\
`x: 10`\
`Result: 0.10000000000000000555111512312578270211815834045410`

> {z:.50f} display 50 decimal point

## agree.py

`1`

```
from cs50 import get_string

s = get_string("Do you agree? ")

if s in ["y", "Y", "yes", "Yes", "YES"]:
	print("Agreed.")
elif s in ["n", "N", "no", "No", "NO"]:
	print("Not agreed.")

```

`2`

```
if s.lower() in ["y", "yes"]:
	print("Agreed.")
elif s.lower() in ["n", "no"]:
	print("Not agreed.")
```

`3`

```
s = get_string("Do you agree? ").lower()
```

> Note the code above has `.lower()` and it can be used as both `2` and `3`

## Function

```
def main():
	for i in range(3):
		meow();

def meow():
	print("meow")

main()
```

> `main` must be called at the bottom in order to run the program

## Arguments

```
def main():
    meow(3);

def meow(n):
	for i in range(n):
        print("meow")

main()
```

## mario.py

```
def main():
    height = get_height()
    for i in range (height):
        print("#")

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                break
        except ValueError:
            print("Only numbers")
    return n

main()
```

> Notice `return n` is placed outside of the the while loop.\
> In Python a variable is always available within a function.

## Print

```
for i in range(4):
    print("?", end="")
print()
```

```
print("?" * 4)
```

> Both codes above will print\
> `????`

## scores.py

```
from cs50 import get_int

scores = []

for i in range(3):
    score = get_int("Score: ")
    scores.append(score)

avarage = sum(scores) / len(scores)
print(f"Avarage: {avarage}")
```

`scores.append(score)`\
`scores += [score]`

> Both lines above do the same thing.

## uppercase.py

```
from cs50 import get_string

before = get_string("Before: ")
after = before.upper()
print(f"After: {after}")
```

## argv.py

```
from sys import argv

if len(argv) == 2:
    print(f"Hello, {argv[1]}")
else:
    print("Hello, world)
```

> python is not included in argv unlike `C Lang`.\
> `argv[0]` = program.py and `argv[1]` = argv - so if you run\
> `python3 argv.py Alice` the result will be\
> `Hello, Alice`

```
from sys import argv

for arg in argv:
    print(arg)
```

## Array Slice

```
a[start:stop:step]

a[-1]      # last item in the array
a[-2:]     # last two items in the array
a[:-2]     # all except the last two items
a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # all except the last two items, reversed
```

## Exit Status

```
from sys import argv

if len(argv) != 2:
    print("Missing cli argument")
    exit(1)

print(f"Hello, {argv[1]}")
exit(0)
```

## Linear Search

`numbers.py`

```
from sys

numbers = [4, 6, 8, 2, 7, 5, 0]

if 0 in numbers:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
```

`names.py`

```
from sys

numbers = ["Alice", "Bob", "Charlie", "Dan"]

if "Bob" in numbers:
    print("Found")
    sys.exit(0)

print("Not found")
sys.exit(1)
```

## Dictionaries

```
from cs50 import get_string

people = {
    "Alice": "+44 7737 297239",
    "Bob": "+44 7447 124822",
    "Charlie": "+44 7834 239920",
    "Dan": "+44 7881 272349"
}

name = get_string("Name: ")
if name in people:
    number = people[name]
    print(f"Number, {number}")

```

`Name: Charlie`\
`Number +44 7834 239920`
