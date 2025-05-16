
import random
import sys
import traceback
import os
# Translator Handles Everything interpreter in Python 3
 
helpDoc ='''
 
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
 
 
'''
 
def main():
    try:
 
        if (len(sys.argv) > 1):
            x = getFileContent(sys.argv[1])

        else:
            x = MultilineInput("No source file given.\n")
 
        if (x == "$h"):
            print(helpDoc)
            input("-Push Enter or Return to Exit-")
            return
 
        execute(compile((x)), (len(sys.argv) == 3 and sys.argv[2] == "$d"))
 
    except(Exception):
        print("\nNothingError: Oops! Something went wrong!\n\n")
        print(traceback.format_exc())
 
    except(KeyboardInterrupt):
        print("\nNothingError: Oops! Something went wrong!\n\n")
        print(traceback.format_exc())
 
    finally:
        print("\nProgram Terminated.\n\nYou can use the '$d' argument after the file argument for a debugger.\nYou can also type '$h' in the file argument for a help document.\nThank you for using the THE (Translator Handles Everything) interpreter.\n")
 
    return
 
 
 
#I think i can use string replacements to make this run bf code
def getFileContent(f):
    #get the file path
    f = os.path.abspath(f)
 
    s = ""
 
    with open(f) as StringCheese:
        s = StringCheese.read()
    return s
 
def compile(s):
    s = s.replace(">", "e")
    s = s.replace("<", "f")
    s = s.replace("+", "g")
    s = s.replace("-", "h")
    s = s.replace(",", "i")
    s = s.replace(".", "j")
    s = s.replace("[", "k")
    s = s.replace("]", "l")
 
    #translating
    out = ""
    for c in s:
        out += str((ord(c) % 10))
    print("\nTranslated Code:\n" + out + "\n")
    return out
 
def execute(innie, Debug):
    #init
    tape = []
    stack = []
    pointer = 0
    pc = -1
 
 
    for i in range(65356):
        tape.append(0)
        
 
    print("\nRunning. Terminate with Control+C\n")
    while (pc < len(innie) -1):
 
        pc = pc + 1
        if (Debug):
            if (len(stack) > 0):
                debug(innie[pc], pointer, stack[len(stack) - 1], len(stack), tape)
            else:
                debug(innie[pc], pointer, 0, 0, tape)
        
 
        if (innie[pc] == '0'):
            pointer = 0 #Good!
            continue
        if (innie[pc] == '1'):
            pointer = (pointer + 1) % 65356
            continue
        if (innie[pc] == '2'):
            pointer = (pointer - 1) % 65356 
            continue
        if (innie[pc] == '3'):
            tape[pointer] =  (tape[pointer] + 1) % 256 #Good!
            continue
        if (innie[pc] == '4'):
            tape[pointer] =  (tape[pointer] - 1) % 256 #Good!
            continue
        if (innie[pc] == '5'):
            s = input("\n> ")
            w = pointer
            for i in s:
                tape[pointer] = (ord(i) % 256) #Good!
                pointer = pointer + 1
            pointer = w
            continue
        if (innie[pc] == '6'):
            c = chr(tape[pointer]) #Good!
            print(c, end = "")
            continue
        if (innie[pc] == '7'): #Good!
            
            stack.append(pc)
                
            if (tape[pointer] == 0): 
                i = search(innie, pc, 8)
                if ( i == -1):
                    return
                else:
                    pc = i
            continue
        if (innie[pc] == '8'):
            
            if (len(stack) > 0 and tape[pointer] != 0):
                pc = stack[len(stack) -1] -1
                stack.pop(len(stack) -1)
                continue
            continue
        if (innie[pc] == '9'):
            tape[pointer] = random.randint(0, 255) #Good!
            continue
 
        
    return
 
 
def search(arr, curr_index, key):
    while (curr_index < len(arr)):
        if arr[curr_index] == key:
            return curr_index
        else:
            curr_index = curr_index + 1
    return -1
    
 
def debug(CurrentInstruct, currentCell, stacktop, stackLen, tape):
    print("\n\nCurrent Instruct: " + str(CurrentInstruct) + "")
    print("Current Cell: " + str(currentCell) + "")
    print("Stack Top: " + str(stacktop) + "")
    print("Stack Length: " + str(stackLen) + "")
 
 
    i = (currentCell - 6) % 65356
    j = 0
 
    while (i != currentCell + 5 and j < 12):
        i = (i + 1) % 65356
        j = j + 1
 
        if (j > 11):
            continue
 
        if ( i == currentCell):
            print(" >" + str(tape[i]) + "< ", end = "")
        else:
            print(" -" + str(tape[i]) + "- ", end = "")
    print("\n") 
    input("-Push Enter or Return to Continue-\n")   
    return
def MultilineInput(message = "", front = "", trail = "\n"):
    print(message + "\n(Type or paste text here. Type '$' to continue)\n\n")
    contents = ""
    line = ""
    while not line == "$":
            line = input(">")
            if line == "$":
                break
            contents += "" + front + line + trail   

    return contents.replace("\r", "").replace("\n","")





while(True):
    main()
 
#Notes  
#d = 0
#e = 1
#etc...
 
#a debug mode that shows whats going on, macrobeep style, would be nice
 
'''
cat
,[.,]
 
++++++++++>,<[>+.<.] looping counter
 
hw
++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.
 
nest
[++[.-]]
 
'''
 
