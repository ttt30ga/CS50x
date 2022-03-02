# CS50 Week 2 - Arrays

[Watch lecture on Youtube](https://youtu.be/v_luodP_mfE)

---

## Basic program

```
include <cs50.h>
include <stdio.h>

int main(void)
{
	string name = get_name("What's your name?\n");
	printf("Hello, %s\n", name);
};
```

## Process

`Preprocess` - A text substitution tool, it tells the compiler to pre-processing before the compilation\
`Compiling` - A compiler translates computer code into another language (assembly code)\
`Assembling` - Converts assembly code to binary code\
`Linking` - Link outputs into one single file

## Bug

On September 9, 1945, U.S. Navy officer Grace Hopper found a moth between the relays on the Harvard Mark II computer.

## Debug

`help50` - shows compiling problems\
`debug50` - opens debugger\
`check50` - check code correctness\
`style50` - check code style

## Memory

Every data type take a certain amount of space in the computer memory

`bool` 1 byte\
`char` 1 byte\
`int` 4 byte\
`float` 4 byte\
`long` 4 byte\
`double` 4 byte\
`string` 4 byte

## Casting

Converts a data type to another

`printf("%c %c %c\n", c1, c2, c3);` - This will print H I ! (spaces in between)\
`printf("%i %i %i\n", c1, c2, c3);` - This will convert char to integers

The above code will look like the exmple below in the computer ram. Every 'char' will take a space and assign the 'var' name to it

| H   | I   | !   |
| --- | --- | --- |
| c1  | c2  | c3  |

## Arrays

`int scores[3];` - This declares scores needs memory space for 3 'int'\
`scores[0] = 72;`\
`scores[1] = 73;`\
`scores[2] = 33;`

The example below print the same value EMMA

```
names[0] = "EMMA";
printf("%s\n", names[0]);
printf("%c%c%c%c\n", names[0][0], names[0][1], names[0][2], names[0][3]);`
```

Save a variable and call it in a for loop to improve runtime

```
int n = strlen(s)
for (int i = 0; i < n; i ++)...
```

This is the same as the example above but more succint

```
for (int i = 0, n = strlen(s); i < n; i ++)...
```
