# Code Structure
---
Code structure allows the program to have decisions. This way some code can be executed if a condition is me or it can be skipped if a condition is not met. Code can also be ran if a condition is met.
## If-Then-Else
```python
if x > 0:
	print("Your number is positive")
elif x < 0:
	print("Your number is negative")
else:
	print("Your number is 0")
```
All if then structures start with an if statement.
- If-Then-Else structure: Each 'if' structure will only have one condition executed. The first condition that is true is the one that is executed, all the other conditions will be skipped regardless of its Truth value. Should no value be True and else statement is present, then the else will be executed.
- All If-Then-Else structures **MUST** start with an if statement.
- If-Then-Else structures *can* have additional `elif` statement to test for more conditions
## While Loops
```python
count = 0
while count < 5:
	count = count + 1
```
While loops will run the same code for as long as the condition is True. Care must be taken to not create an infinite loop if one is not wanted.
```python
count = 0
while True:
	if count < 10:
		count += 1
	else:
		break
```
Note that the ==break== will exit the current loop.
## For Loop
```python
my_list = ["A", "B", "C"]
for i in my_list:
	print(i)
```
For loops are good for iterating through a list. They use a local variable which in this case is i to act as a place holder for each element in the list.

[[Lists]]
