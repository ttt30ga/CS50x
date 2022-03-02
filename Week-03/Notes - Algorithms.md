# CS50 Week 3 - Algorithms

[Watch lecture on Youtube](https://youtu.be/yb0PY3LX2x8)

---

## Links

[Comparison Sorting Algorithms](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)

## Tips

> Segmentation fault (core dumped)\
> `Means we have touched memory we weren't supposed to touch and the program has exited itself.`

## Big O Notation

The opposite of Omega Ω. It represents the upper bound.
Big O notation is used to classify algorithms according to how their run time or space requirements grow as the input size grows. It reads 'on the order of'.
By using for loops to iterate n times, you are running a Big O.

_Examples_\
`O(n)`\
`O(n/2)`\
`O(log2n)`

## Omega Ω

The opposite of Big O. It represents the lower bound.

_Examples_\
`Ω(n2)`\
`Ω(n log n)`\
`Ω(n)` - linear search\
`Ω(log n)` - binary search\
`Ω(1)`\
`Ω(n2)`\
`Ω(n log n)`\
`Ω(n)`\
`Ω(log n)`\
`Ω(1)` - linear search, binary search

## Big Theta θ

Theta stands in between Big O and Omega Ω

_Examples_\
`θ(n2)`\
`θ(n log n)`\
`θ(n)` - linear search\
`θ(log n)` - binary search\
`θ(1)`

---

## Linear Search

_Pseudocode - level 1_

```
for each door from left to right
  if number is behind door
  	return true
return false
```

_Pseudocode - level 2_

```
for i from 0 to n-1
  if number behind door[i]
  	return true
return false
```

## Binary Search

_Pseudocode - level 1_

```
if no doors
	return false
if number behind middle door
	return true
else if number < middle door
	search left half
else if number > middle door
	search right half
```

_Pseudocode - level 2_

```
if no doors
	return false
if number behind doors[middle]
	return true
else if number < doors[middle]
	search doors[0] through doors[middle - 1]
else if number > doors[middle]
	search doors[middle + 1] through doors[n - 1]
```

---

## Struct

C lets you create datatypes.

The example below helps looking for a specific number if you know the name of a the person.

> C is not object oriented like other languages, java, c++

```
typedef struct
{
	string names;
	string numbers;
}
person;

int main(void)
{
	person people[4];

	people[0].name = "EMMA";
	people[0].number = "617-555-0100";
  ...
}
```

---

## Selection Sort

```
for i from 0 to n-1
	find smallest n between numbers[i] and numbers[n-1]
	swap smallest n with numbers[i]
```

Running time of _Selection Sort_?

> upper bound - `O(n2)`\
> lower bound - `Ω(n2)`

---

## Bubble Sort

```
repeat n-1 times
	for i from 0 to n-2
		if numbers[i] and numbers[i+1] out of order
			swap them
```

Running time of _Bubble Sort_?

> upper bound - `O(n2)`

`With optimisation in case no swaps where made the 1st time.`

```
repeat n-1 times
	for i from 0 to n-2
		if numbers[i] and numbers[i+1] out of order
			swap them
	if no swaps
		quit
```

Running time of _Bubble Sort with optimisation_?

> lower bound - `Ω(n)`

---

## Recursion

A function that calls itself.
In the example below, function 'Draw' is called inside itself.

```
void draw(int n)
{
  if (n <= 0)
  {
    return;
  }

  draw(n - 1);

  for (int i = 0; i < n; i++)
  {
    printf("#");
  }
  printf("\n");
}
```

---

## Merge Sort

```
if only one number
  quit
else
  sort left half
  sort right half
  merge sortered halves
```

---

## Lab

### Algorithms

- Linear search
- Binary search
- Bubble sort
- Selection sort
- Recursion
- Merge sort

### Test Programs

```
Bubble Sort

1 reversed 5000 - `0m0.097s`
1 reversed 10000 - `0m0.259`
1 reversed 50000 - `0m5.827s`
-
1 random 5000 - `0m0.093s`
1 random 10000 - `0m0.388`
1 random 50000 - `0m7.523s`
-
1 sorted 5000 - `0m0.050s`
1 sorted 10000 - `0m0.113s`
1 sorted 50000 - `0m0.726s`

---

Merge Sort

>>>> 1st - WINNER! 🏆
2 reversed 5000 - `0m0.106s`
2 reversed 10000 - `0m0.132`
2 reversed 50000 - `0m5.426`
-
2 random 5000 - `0m0.038`
2 random 10000 - `0m0.069s`
2 random 50000 - `0m0.456s` <<<
-
2 sorted 5000 - `0m0.046s`
2 sorted 10000 - `0m0.064s`
2 sorted 50000 - `0m0.531s`

---

Selection Sort

3 reversed 5000 - `0m0.064s`
3 reversed 10000 - `0m0.190`
3 reversed 50000 - `0m3.359s`
-
3 random 5000 - `0m0.068s`
3 random 10000 - `0m0.179`
3 random 50000 - `0m3.306s`
-
3 sorted 5000 - `0m0.057s`
3 sorted 10000 - `0m0.193s`
3 sorted 50000 - `0m3.301s`
```
