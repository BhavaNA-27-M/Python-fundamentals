Loops are one of the MOST Important concept in programming. 
A Loop means : Repeat code automatically 
1. for loop
   Used when repititions are known.

     # for loop 
   for i in range(1, 6):
    print(i)

     # Step value 
    for i in range(2, 11, 2):
    print(i)

  Real Uses of for Loop
Used in:
  reading lists
  processing data
  automation
  AI iterations
  APIs
  datasets
______________

2. while Loop
  Used when repetitions are unknown.
 Repeat while condition is True
     # while loop
     i = 1

while i <= 5:
    print(i)

    i += 1

Real Uses of while Loop
Used in:
 login systems
 chatbots
 AI agents
 retry systems
 monitoring systems
_____________

3.break Statement
Stops loop immediately.
# break 
for i in range(10):

    if i == 5:
        break

    print(i)
  
  Real Uses of break
   stop login retries
   stop searching
   exit menu systems
  stop automation process
   ______________

4. continue Statement
Skips current iteration.
# continue 
for i in range(5):

    if i == 2:
        continue

    print(i)

Real Uses of continue
skip invalid data
ignore errors
filtering systems
preprocessing AI data
_______________

5. pass Statement
Placeholder statement.
Used when:
code not written yet
future logic planned
# pass
for i in range(5):

    if i == 3:
        pass

    print(i)

Important
pass does:
nothing
It prevents syntax errors for empty blocks.

Real Uses of pass
Used while:
 planning functions
 designing systems
 incomplete code structures
_________________

6. Nested Loops
Loop inside another loop.
  # Nested loop
for i in range(3):

    for j in range(2):
        print(i, j)

Real Uses of Nested Loops
Used in:
matrices
AI tensors
game boards
image processing
tables
patterns

# Pattern Example
for i in range(1, 6):
    print("*" * i)
  ______________


WHY LOOPS ARE SO IMPORTANT
Loops power:
     AI systems
     automation tools
     backend processing
     data science
     scraping
     dashboards
     APIs
     games
Loops are one of the biggest foundations in programming.
  
