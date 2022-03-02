# CS50 Week 4 - Memory

[Watch lecture on Youtube](https://youtu.be/nvO1sq_b_zI)

---

## Memory Addresses

Every bit in memory is an allocation, bits are defined as hexadecimals.

| BIT  | BIT  | BIT  | BIT  | BIT  | BIT  | BIT  | BIT  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0x0  | 0x1  | 0x2  | 0x3  | 0x4  | 0x5  | 0x6  | 0x7  |
| 0x8  | 0x9  | 0xA  | 0xB  | 0xC  | 0xD  | 0xE  | 0xF  |
| 0x10 | 0x11 | 0x12 | 0x13 | 0x14 | 0x15 | 0x16 | 0x17 |
| 0x18 | 0x19 | 0x1A | 0x1B | 0x1C | 0x1D | 0x1E | 0x1F |

_Examples_\
`0x12345`

```
#include <stdio.h>

int main(void)
{
	int n = 50;
	int *p = &n;

	printf("%i\n", n);
	printf("%p\n", p);
	printf("%i\n", *p);
}
```

```
50
0x7ffd9...
50
```

## char \*

```
#include <stdio.h>

int main(void)
{
	char *s = "Hi!\n";
	char *z = &s[0];

	printf("%p\n", z); // 0x40982...
	printf("%p\n", s); // 0x40982...

	printf("%c\n", s[0]); // H
	printf("%c\n", s[1]); // i
	printf("%c\n", s[2]); // !
	printf("%c\n", s[3]); //
}
```

```
0x40982...
0x40982...

H
i
!

```

## Pointer arithmetic

```
#include <stdio.h>

int main(void)
{
	char *s = "Hi!\n";
	char *z = &s[0];

	printf("%c\n", *s); // H
	printf("%c\n", *(s + 1)); // i
	printf("%c\n", *(s + 2)); // !
}
```

```
H
i
!
```

## Compare

```
#include <cs50.h>
#include <stdio.h>

int main(void)
{
	int i = get_int("i: ");
	int j = get_int("j: ");

	if ( i == j )
	{
		printf("Same\n");
	}
	else
	{
		printf("Different\n");
	}

	string s = get_string("s: ");
	string t = get_string("t: ");

	if ( s == t )
	{
		printf("Same\n");
	}
	else
	{
		printf("Different\n");
	}
}
```

```
i: 42
j: 42
Same
s: Hi
t: Hi
Different
```

## Malloc and Free

`malloc` - memory allocation\
`free` - free memory

When you use `melloc` you should than use `free` to free the memory used by your task.

```
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
	char *y = get_string("y: ");
	char *z = malloc(strlen(y) + 1);

	for (int i = 0, n = strlen(y) + 1; i < n; i++)
	{
		z[i] = y[i];
	}

	strcpy(z, y);

	z[0] = toupper(z[0]);

	printf("y: %s\n", y);
	printf("z: %s\n", z);

	free(t);
}
```

> The code above `for loop` and `strcpy` do the same thing.

## Valgrind

Valgrind is a tool that helps debug your code specifically for memory issues.

> The code below state you used memory you shouldn't have used and that you should free the memory used. Look fixed code below.

```
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int *x = malloc(3 * sizeof(int));
	x[1] = 72;
	x[2] = 73;
	x[3] = 34;
}
```

```
{
	x[0] = 72;
	x[1] = 73;
	x[2] = 34;
}
free(x);
```

## Stack and Heap

| Memory distribution |
| ------------------- |
| Machine Code        |
| Globals             |
| ↓ Heap              |
|                     |
|                     |
|                     |
|                     |
| ↑ Stack             |

`Machine Code` Used by the OS 0 and 1\
`Globals` Used by global var and func\
`Heap` Used by Malloc\
`Stack` Used by local var and func

> `Stack` and `Heap` can clash if you use a lot of local vars and functions or `malloc` (memory allocation).\
> If the Heap and Stack grow in size the program will eventually clash causing `Stack Overflow`.
