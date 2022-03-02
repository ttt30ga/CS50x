# CS50 Week 5 - Data Structures

[Watch lecture on Youtube](https://youtu.be/-gpsiMiEOHU)

---

## Arrays

```
#include <stdio.c>
#include <stdlib.c>

int main(void)
{
	int list[3];
	int *list = malloc(3 * sizeof(int));
}
```

> The code above do the same thing, but the second line allocatge the array in the `heap`.

```
#include <stdio.c>
#include <stdlib.c>

int main(void)
{
	// Allocate array of size 3
	int *list = malloc(3 * sizeof(int));
	if (list == NULL)
	{
		return 1;
	}

	// Assign 3 munbers to array
	list[0] = 1;
	list[1] = 2;
	list[2] = 3;

	// Time passes

	// Allocate new array of size 4
	int *tmp = malloc(4 * sizeof(int));
	if (tmp == NULL)
	{
		free(list);
		return 1;
	}

	// Loop through old array and assign to new array
	for (int i = 0, i < 3, i++)
	{
		tmp[i] = list[i];
	}

	// Add 4 to new array
	tmp[3] = 4;

	// Free old array
	free(list);

	list = tmp;

	// Print new array
	for (int i = 0, i < 4, i++)
	{
		printf("%i\n", tmp);
	}

	// Free new array
	free(list);
	return 0;
}
```

## Realloc

> Previous code revritten with `realloc`

```
#include <stdio.c>
#include <stdlib.c>

int main(void)
{
	// Allocate array of size 3
	int *list = malloc(3 * sizeof(int));
	if (list == NULL)
	{
		return 1;
	}

	// Assign 3 munbers to array
	list[0] = 1;
	list[1] = 2;
	list[2] = 3;

	// Time passes

	// Allocate new array of size 4
	int *tmp = realloc(list, 4 * sizeof(int));
	if (tmp == NULL)
	{
		free(list);
		return 1;
	}

	// Add 4 to new array
	tmp[3] = 4;

	list = tmp;

	// Print new array
	for (int i = 0, i < 4, i++)
	{
		printf("%i\n", tmp);
	}

	// Free new array
	free(list);
	return 0;
}
```

## Linked Lists

```
typedes struct node
{
	int number;
	struct node *next;
}
node;
```

> `node *list;` This is garbage value\
> `node *list = NULL;` This is known value - `better`

```
// Add something to the list
// Use malloc to allocate to `n` the size of node
node *n = malloc(sizeof(node));

// If `n` isn't null, assign 1 to its .number
if (n != NULL)
{
	(*n).number = 1;
}

list = n;
```

> `(*n).number = 1;`\
> `n->number = 1;` Same as above - `better`

```
#include <stdio.c>
#include <stdlib.c>

typedes struct node
{
	int number;
	struct node *next;
}
node;

int main(void)
{
	// Make a list with NULL value to avoid having garbage values
	node *list = NULL;

	// Add number to list
	node *n = malloc(sizeof(node));
	if (n == NULL)
	{
		return 1;
	}
	n->number = 1;
	n->next = NULL;

	// Update list
	list = n;

	// Add number to list
	n = malloc(sizeof(node));
	if (n == NULL)
	{
		free(list);
		return 1;
	}
	n->number = 2;
	n->next = NULL;
	list->next = n

	// Add number to list
	n = malloc(sizeof(node));
	if (n == NULL)
	{
		free(list->next); // Free children first
		free(list); // Free parent at last
		return 1;
	}
	n->number = 2;
	n->next = NULL;
	list->next = n

	// Add number to list
	n = malloc(sizeof(node));
	if (n == NULL)
	{
		free(list->next); // Free children first
		free(list); // Free parent at last
		return 1;
	}
	n->number = 3;
	n->next = NULL;
	list->next->next = n

	// Print numbers
	for (node *tmp = list; tmp = NULL; tmp->next)
	{
		printf("%i\n", tmp->number);
	}

	// Free list
	while (lise != NULL)
	{
		node *tmp = list->next;
		free(list);
		list = tmp;
	}

	return 0;
}
```
