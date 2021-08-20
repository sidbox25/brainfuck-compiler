# Antosser's Brainfuck Compiler
## Overview
It compiles assembly-like code to Brainfuck.

## Usage
### Writing/editing code
Open the "code.txt" file with a text editor. That's where the code belongs.  
Every line in the code starts with a function name (e.g. `var`) and is followed by it's arguments.
Use the following functions to write your code: 
- **var** <variable name> - **declare** a variable with value 0
- **add** <declared variable> <number> - add some value to a variable
- **copy** <variable1> <variable2> - duplicate the value from variable1 to variable2
- **move** <variable1> <variable2> - same as "copy" but variable1 gets erased (much faster than copy)
- **multiply** <variable> <number> - multiply a variable with a number
- **multiply** <variable1> <variable2> <number> - multiply variable1 with number while variable1 is erased and output is written to variable2
- **clear** <variable> - set the variable value to 0
- **input** - creates a variable "input" if not already declared and prompts the user for an input
- **input** <variable> - set the variable to the user input
- **print** <variable> - print the ascii character of a variable value
- **#pause** - halt the programm
- **#if** <variable> number <number> - if variable is equal to number, code between "#if" and "#endif" gets executed
- **#if** <variable> letter <letter> - if variable contains the ascii code of the letter, code between "#if" and "#endif" gets executed
- **#if** <variable1> variable <variable2> - if variable1 is equal to variable2, code between "#if" and "#endif" gets executed
- **#endif** - close an if statement
- **#else** - just a regular else statement used instead of #endif
- **#endelse** - close an else statement
- **#while** <variable> - repeats executing the code between "#while" and "#endwhile" while the variable is non-zero
- **#endwhile** - close a while statement

### Compilation to Brainfuck
Run the "main.py" file in the command line. Console will ask you for a command.
To compile code from "code.txt" to "compiled.bf", enter **compile** as the input.
You'll see the compiled code in the console as well.
In case you want to compile and run your code at the same time, use  the **cr** command in the Console.

### Running the compiled code
If you want to try executing the previously compiled code, use the **run** command in the Console.

## Example
Here is an example of an uncompiled code:
```
  // Create a variable called myvar, myvar2
  var myvar
  var myvar2
  
  // Add 50 to myvar
  add myvar 50
  
  // Copy the value of myvar to myvar2
  copy myvar myvar2
  // Now myvar and myvar2 contain the value 50
  
  // Set myvar to 0
  clear myvar
  
  // Move the value of myvar2 to myvar
  move myvar2 myvar
  // Now myvar is 50 and myvar2 is 0
  
  // Multiply myvar by 3 (50 * 3 = 150)
  multiply myvar 3
  
  // Initialize varibale input and set it to users input
  var input
  input input
  
  // Print the next character of users input
  add input 1
  print input
```
