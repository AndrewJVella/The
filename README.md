# The

The (Translator Handles Everything) is a language by Andrew Vella (Pixelated Starfish on the Esolangs Wiki) in 2022.
It is a bf derivative designed to handle arbitrary input and convert it into runnable Turing complete code.
bf [sic] instructions are modified accordingly:
*For easy conversion from arbitrary input.
*For the elimination of errors.
*For achieving the above while maintaining Turing completeness.
 
The purpose of this language is to interpret any data at all, and run it without error.
Files are converted into a set of integers, one character at a time.
Then, each integer is set to itself mod 10, and mapped to a command.
 
==Computation==

===Memory===

Commands operate on a tape of bytes in the range of 0 to 255.
A byte value will wrap around so as not to exceed range.
Bytes are modified by a pointer that can operate on one byte at a time.
There are 65536 bytes on the tape.
The tape is circular so byte 65535 is adjacent to byte 0.
There is also a stack for storing branches, and a program counter to track the current command in execution.
 
===Commands===

 0 - Set the tape pointer to 0.
 
 1 - Increment tape pointer.
 
 2 - Decrement tape pointer.
 
 3 - Increment byte.
 
 4 - Decrement byte.
 
 5 - Take input as a string.
     Write each character to the next byte and increment the pointer.
 
 6 - Output byte as ASCII character.
 
 7 - If the value of the current byte is zero, push the program counter on to the stack.
     Otherwise, look for the next 8. If an eight is found, jump to it. If not, halt
 
 8 - If the stack is not empty and the value of the current byte is not 0,
     set the program counter to the value at the top of the stack, and pop.
     Otherwise, do nothing.
 
 9 - Set byte to a random value.
 
A string of numbers is not interpreted directly. That would not be any fun.
However, bf commands are interpreted directly via a character substitution (> becomes e, < becomes f etc.)
 
===Error Message===
 
If there is an error, this message will print:
 
 NothingError: Oops! Something went wrong!
 
Following the message, print two new lines and any text the implementing language prints.
 
==Using the Interpeter==

===Running===

The official interpreter is written in Python3 and can take two inline arguments on the command line:
*file name
*debugger flag
 
If the file name is left out, it should ask for a file like so:
 Please give a source file:
 > 
 
The debugger flag is $d and is used to run the debugger.
 
At the start of a program, print ''Running...'' on its own line:
 Running...
 
Print this message at halt:
 Program Terminated.
 
 You can use the '$d' argument after the file argument for a debugger.
 You can also type '$h' in the file argument for a help document.
 Thank you for using the THE interpreter.
 
Also note that when a program takes input a right angle bracket and space should be printed on its own line:
 >
 
===The Debugger===

The debugger single steps through a program and prints information about the current step, including a section of the tape extending from five cells left of the current cell, to five cells right of the current cell.
Output is printed before the debug information.
 
 
Example with the current cell at 102:
 Current Instruct: 9
 Current Cell: 0
 Stack Top: 0
 Stack Length: 0
  -72-  -0-  -0-  -0-  -0-  >102<  -0-  -0-  -0-  -0-  -0-
It will then skip a line and print this prompt: 
 -Push Enter or Return to Continue-
 
===Help===

If the interpreter is given the argument help instead of a filename, it will print a plain text compatible version of this document, followed by this prompt:
 
 -Push Enter or Return to Exit-
 
 ==End of Help Doc==
 
