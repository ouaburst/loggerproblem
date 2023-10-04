# Laboration 2

## Environment & Tools
This lab was made on a computer with Windows 10, using Python version 3.11.5, PyCharm 2023.2.1 
(Professional Edition) as IDE and Git version 2.42.0.windows.1. 

## Purpose
This study focuses on the complexities of string manipulation, function definitions, and user input handling and 
validation. Grounded in the theme of a fictitious spy agency's authentication system, the assignment aims to result 
in a solution where user-provided information is successfully processed and verified. For the success of this study 
to be measured, each of the following concrete goals must be achieved:

- Implement the **``authenticate_user(str)``** function to accurately parse the username and password from the input 
string without hard-coding, and validate these against the formatted username and decrypted password.
- Implement the **``format_username(list)``** function to ensure that usernames, regardless of input format, are 
presented in the **``"Firstname_Surname"``** format. 
- Implement the **``decrypt_password(str)``** function following specified rules: adhering to the ASCII-table rotation 
interval, applying alternate rotation keys, and ensuring vowels are both preceded and succeeded by **``0``**.

## Procedures
The first step towards authenticating the user is splitting the user input received in the `authenticate_user(str)` function
into three parts that can be passed as arguments to the `format_username(list)` and `decrypt_password(str)` functions.
This was achieved by calling the `.split()` method on the `credentials` parameter and storing it in the `credentials_list` variable
to get a list of strings. 

By using list slicing all but the last elements of `credentials_list` is passed to the `format_username(list)` function and
the last element is passed to the `decrypt_password(str)` function.

The requirements for the username states that the parts of the username should be connected with an underscore so the 
first thing that happens is the joining of the elements using `"_".join()`. All letters have to be lower case except 
for the first letter in each name, this is achieved using the `.title()` method that capitalizes the first letter in each 
word and sets the rest to lowercase. The string could then be returned.

The next step was implementing the `decrypt_password()` function.

An inner function, `rotate_char(rot)`, was created to further encapsulate the password decryption and promote reusing 
of code. This function handles the rotation of characters. The correct rotation value is passed to the function and 
the `char` variable, which contains the character that will be rotated, is already available to the function through 
the enclosing scope. 
The character is converted to it's ASCII-code by calling `ord(char)`, the rotation 
value is added and the result stored in the new variable `char_value`. Since only characters numbered 33-126 are
used numbers above 126 need to be shifted. This was accomplished with a ternary operator that subtracts 127 so that 
only the surplus remains and then adds 33 which is the lowest number allowed. 

    decrypted_char = chr(char_value) if char_value < 127 else chr((char_value - 127) + 33)

The rotated number is then returned to the outer function. 

Every character in the password needs to be checked and rotated to complete the decryption. A for loop was chosen to handle 
the iteration since the entire password is to be rotated. The rotation value depends on the position of the character so
to keep track of that and the current character the `enumerate()`function was used.

    for i, char in enumerate(password):

An if statement to check if the current letter is a vowel was made. The `in` keyword is used on the character and the 
`vowels` string variable. If the character is a vowel another if statement uses the `%` operator to determine whether the
position is even or not. For readability the string concatenation and call to `rotate_char(rot)` is made in the same 
expression.
The same kind of check is made if the character isn't a vowel but the formatting with adding 0 before and after isn't 
needed. Once the entire password has been decrypted it's returned.

The finished username and password are compared to the `agents` dictionary as a key item pair to get a boolean value
that is returned to the main function.

## Discussion
### Purpose Fulfillment
The first goal was achieved by splitting the input into a list and using list slicing to get lists and strings to pass to
the `format_username(username: List[str])` and ` decrypt_password(password: str)` functions. The slicing ensures that 
the program can handle scaling of the username if necessary. The returned strings could
then be compared as a key item pair to the contents of the `agents` dictionary. 

The second goal was implementing the `format_username(username: List[str])` function. This was accomplished by using list
joining and string methods to get the correct formatting.

Implementing the `decrypt_password(password: str)` function was completed by creating a nested function to handle the 
rotating of the characters. A for loop handles the iteration through the string and if statements decide which formatting 
rotation should be applied. 

The solution fulfills all the required goals and testing has ensured that the username and password are correctly 
authenticated every time no matter the input. 

### Alternative Approaches

The `format_username(username: List[str])` could have been resolved with one line of code but to improve readability
several expressions ver used.

The nested `rotate_char(rot)` function could have been made as a lambda, but it would be very hard to understand it 
without comments.

    rotate_char = lambda rot: chr(ord(char) + rot) if ord(char) + rot < 127 else chr(ord(char) + rot - 127 + 33)

The for loop in the `decrypt_password(password: str)` function could have been replaced with a while loop but since the 
entire string will have to be looped through and the `enumerate()` function provides an iteration counter the for loop is
a better option.
The contents of the for loop could have been made in other ways. Using the `+` operator is not the most efficient way to 
concatenate strings since every concatenation creates a new object. `"".join()` would have been more efficient but the 
character would first have to be put into a list and then joined. Since it's unlikely that a password would be long enough
for the concatenation to become a performance issue it's not a problem that needs to be remedied in this case.

The nested if statements in the loop is not the most elegant solution but the readability is fine, and it serves its purpose.
The loop could have been redesigned so that all characters were rotated with the same if statement and added to the string
during a second check. This solution would require a variable containing the original character to check if it's a vowel
but, it could improve readability and would get rid of the nested if statement.

    if even:
        rotate 7
    else:
        rotate 9
    
    if vowel:
        add to string with vowel formatting
    else:
        add to string
    
Overall the nested if statements is the weakest part of the program and not an ideal solution.


## Personal Reflections
I have worked with most of the concepts used in the laboration before except for nested functions and list comprehension
so the implementations weren't that tricky. Report writing is still the biggest issue. 
I also find it hard to know which coding conventions are expected in this course. I've taken a beginners course in Java 
previously where, among other things, variables couldn't be initialized with anything other than an assignment operation,
and they all needed to be declared on separate lines. For example this code would pass: 
    
    int x = 1;
    int y = 2;
    int sum = 0;
    
    sum = x + y;

But this:

    return (user_tmp, pass_tmp) in agents.items()

would not have been allowed and in this course it's encouraged. Or maybe I just don't get it, however, I like this way 
of coding better because it's less verbose. I'm also more used to using camel case in naming but here underscore is used.