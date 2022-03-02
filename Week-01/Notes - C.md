# CS50 Week 1 - C

[Watch lecture on Youtube](https://youtu.be/URrzmoIyqLw)

---

## Basic program

```
include <stdio.h>

int main(void)
{
	printf("hello, world");
};
```

`<stdio.h>` - Standard Input/Output Header

## Run program from terminal

```
$ clang hello.c
$ ./a.out
$ hello, world~/ $
```

> The extra ~/ $ in the result is because we didn't give any comand to go to a new line
> C language litteraly does everything we ask it to
> To print a new line add \n at the end of the printf and recompile

## Run program using a different name

```
$ clang -o hello hello.c
```

## Asking user for something

string answer get_string("What's your name?\n");
printf("hello, %s\n", answer);

`string` - val type\
`answer` - var name\
`%s` - placeholder, s stand for string

## Add and link another file to the source code

```
include <cs50.h>
include <stdio.h>
```

`clang -o string string.c -lcs50`

## To avoid having to type all the above

`~ make string` - make is a terminal comand

## Variables

`int counter = 0;` - non fractional numbers like 21, 0, −20, -8\
`counter = counter + 1` - in this case int is not added because it was declared previously\
`counter ++` - abbreviation for previous line

## Conditions

```
if (x < y)
{
	printf("x is less than y\n");
}
else if (x > y)
{
	printf("x is greater than y\n");
}
else
{
	printf("x is equal than y\n");
}
```

## Loop While

```
while (true) // for a loop to work you must answer a question
{
	printf("Hello world\n");
}

int i = 0
while (i < 50)
{
	printf("Hello world\n");
	i++;
}
```

## Loop For

```
for (int i = 0; i < 50; i++) // same thing as the above example in the while loop
{
	printf("Hello world\n");
	i++;
}
```

## Data types

`bool` - true, false, null\
`char` - single character like y, n\
`double` - numbers bigger than float\
`float` - numbers with decimals 3.14159\
`int` - numbers like 2, 3, 8, 234, 2984 up to 4000000000 (4 billions)\
`long` - numbers bigger tha int\
`string` - text

## Float

`printf("Price is %f\n", price _ 1.0625);` - Price is 106.250000\
`printf("Price is %.2f\n", price _ 1.0625);` - Price is 106.25 - because of the %.2f

## Functions

Computers read from top to bottom therefore finctions should be placed before 'main', but because
best practices dictate function should be written at the bottom of the file after 'main'

- 'void' means the function expects no values
- 'cough(void)' this second void means returns no values
- 'int n' the function takes an input called n

```
#include <stdio.h>

// Function mention
void cough(void);

int main(void)
{
	for (int i = 0; i < 3; i++)
	cough();
};

// Function
void cough(void)
{
	printf("Cough\n");
}

// 'n' returns printf 'n' times
void cough(int n)
{
	for (int i = 0; i < n; i++) {
	printf("Cough\n");
}
```
