# Antosser's Brainfuck Compiler
## Overview
This is one of my big projects.  
It compiles assembly-like code to brainfuck. Pretty useless but very funny and nearly impossible to disassembly.

## Usage
Once you run the main.py file in the command line it will ask you for a command.  
Common commands are:
- **edit** - Opens your uncompiled code in notepad so you can edit it 
- **compile** - **Compiles** your uncompiled code and outputs it to the console
- **run** - **Runs** your compiled code
- **cr** - **Compiles** and **runs** your code

### Functions
As you read earlier, you can edit the uncompiled code in notepad using the **edit** command.  
Every line in the code starts with a function name (ex. `var`) and are being followed with their arguments.
The functions are: 
- **var** <varibale name> - **declare** a varibale
- **add** <declared varibale> <number> - add some value to a varibale
- **copy** <varibale1> <varibale2> - add the value from varibale1 to varibale2
- **move** <varibale1> <varibale2> - same as copy but varibale1 gets erased (faster)
- **multiply** <varibale> <number> - multiply a varibale with a number
- **multiply** <varibale1> <varibale2> <number> - multiply varibale1 with number while varibale1 is erased and output is written to varibale2
- **clear** - clear a varibales value
- **input** - creates a varibale "input" if not already declared and prompts the user for an input
- **input** <varibale> - set the varibale to the user input
- **print** <varibale> - print the ascii character of a varibale value
- **#pause** - halt the programm

## Example
Here is an example of an uncompiled code:
```
// Create a varibale called myvar
var myvar
```
