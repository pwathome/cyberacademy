# Function
---
Functions in python are how we get things done.
Functions include the name of the function, a set of parenthesis and any optional arguments.

## Code Example
```python
print("Hello World")
```
## Print Function
print followed by a set of parenthesis, inside the parenthesis is  a string hat is printed to the screen.

# Input Function
```python
var = input("Give a yes or no: ")
```
## Converting Data types
### String
```python
var = 8
var = str(var)
```
In this example, var is an integer with the value 8, it is then converted to a string. When using a concatenation in a print statement, all data types must be the same, and will typically need to be a string data type.
```python
var = 8
print("My number is " + str(var))
```

### Integer
```python
var = "8"
var = int(var)
```
In this example we take the string var and convert it to an integer.
```python
var = int(input("Give me a number: "))
```

### Floating-Point Numbers
```python
var = "8"
var = float(var)
```
In this example we are converting var from a string into a float. A floating point number is any number with a decimal.