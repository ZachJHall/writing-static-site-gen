---
date: 10-10-21

title: Swapping values in python

type: TIL
---
Ocassionally I will find myself having to swap the values of two variables.

Assuming:
```
a = 5
b = 3
```
This is typically done by using a temp variable.

```
temp = a
a = b
b = temp
```
I recently discovered that python has a really neat feature that allows you to swap the variables without the declaration of a temp variable.

```
a, b = b, a

```
This results in:
```
print(a) => 3
print(b) => 5
```