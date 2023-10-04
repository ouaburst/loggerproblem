# Laboration 1

## Environment & Tools
This lab is made on a computer with Windows 10, using Python version 3.11.5, PyCharm 2023.2.1 
(Professional Edition) as IDE and Git version 2.42.0.windows.1. 

## Purpose
This study covers fundamentals surrounding basic data types, operators and conditional logic, together with some basic 
use of version control. The work conducted aims to produce a solution which conforms to needed requirements as stated 
by the assignment specification. The concrete goals for determining success of this study are:

- Isolating the main work to dedicated development branch named **``laboration_1``**, which is merged into 
**``master``** upon submission.
- Adding missing logic to provided source file in compliance with expected behavior as stated by belonging pseudo code.

## Procedures
The starting point for this assignment was cloning the solution repository from bitbucket, using the URL provided by 
bitbucket, and setting up a local repository via the command prompt. By continually using the `git status` command the 
progress could be tracked step by step.
The next step was creating a new branch with `git branch` and setting up an upstream so the branch could be tracked 
remotely. Once the repository was set up correctly the script writing could start.

The first task was to sum the value of three constants, each of a different datatype; `int`, `float`, and `string`, 
then store them in the variable `TOTAL`. Since the solution was to be an `int` the `string` and `float` needed to be 
cast as `int`. This was done using the constructor function `int()`. The casting and adding was made in the same 
statement, this way the variables retained their datatype for the next step and were cast as `int` only in this statement.

    TOTAL = A + int(B) + int(C)

The second task was to check if the variable `TOTAL` was contained as a substring in the `string` constant `TEXT`. 
To check this `TOTAL`, which is an integer, needed to be cast as a `string` using `string()` and compared to `TEXT` 
with the `in` keyword. Depending on the outcome a message was to be assigned to the variable `OUTPUT`. A ternary 
operator was used to test the condition and `TOTAL` was cast as a `string`.    

    OUTPUT = "true that" if str(TOTAL) in TEXT else "nope"

Once the solution had been implemented the changes in the file needed to be staged and committed with git and the same
procedure was then repeated with the report.
To make sure that the merging and pushing would work, the necessary steps were first applied to a different repository.
The branch was pushed to the remote repository using the `git push` command, merged with the master branch 
locally with the `git merge` command and finally master could be pushed to remote.

## Discussion
### Purpose Fulfillment
The purpose of this lab was to show ways of using version control both locally and remotely. This was accomplished by
following the lab instructions and consulting the course literature "Pro Git" to find the necessary commands. 

The other goal was to work with datatypes, operators, casting and conditions to complete two tasks. Casting datatypes was 
necessary to obtain the correct datatype both for summation in the first task and `string` comparison in the second.
A condition was used in the second task to decide which value to assign to the variable `OUTPUT`. An arithmetic
binary operator (`+`) was used in task one. In part 2 the ternary and membership (`in`) operators were demonstrated,
and both parts utilized assignment operators.
The script was successful in producing the correct result with clear and concise code, using all the components 
mentioned in the purpose.  

### Alternative Approaches
Since the git instructions were very straight forward and didn't leave a lot to be interpreted there is no real
alternative approach.

Regarding the code implementation the casting could have been made separately from the calculation by making new 
variables, but it would be hard to justify unless many more similar calculations were planned.  
    
    B2, C2 = int(B), int(C)

The summation could have been done in another variable and then assigned to `TOTAL` to really emphasize that `TOTAL` is 
the final answer but since only one simple calculation was planned it would only make the code more cluttered. If more 
steps for the calculation were necessary I would consider it. 

    sum = A + int(B) + int(C)

In part 2 of the assignment the ternary operator could be replaced with an `if...else`-statement. 

    if str(TOTAL) in TEXT:
        OUTPUT = "true that"
    else:
        OUTPUT = "nope"

If the condition had been more complex the ternary operator could have made the code hard to read, but with a 
condition and script as simple as this it's hard to argue that it is a problem.   


## Personal Reflections

Since I have prior experience with programming in python the code implementation was not an issue, although I had to
refresh my memory on some of the syntax. Most of the effort was put into writing a report and learning git, both of 
which are relatively new to me. The more I learn about version control the more I can see the advantages, especially 
when working on group projects. The problem will be making it second nature in the work process. 