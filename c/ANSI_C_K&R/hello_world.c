// This is a simple C program that prints "Hello, world!" to the console. It demonstrates the basic structure of a C program, including the use of the `main` function and the `printf` function for output.
// The program is written in the C99 language standard version, which is a widely used version of the C programming language. The code is well-commented to explain each part of the program for educational purposes.

// This is how comments are written in C. Comments are ignored by the compiler and are used to provide explanations or notes for the programmer. In this case, comments are used to explain the purpose of the program and the functionality of each line of code.
// Each comment must begin with a double forward slash `//`. Everything after the `//` on that line is considered a comment and will not be executed as part of the program.
// Comments can also be written using the `/* ... */` syntax, which allows for multi-line comments, but in this example, we are using single-line comments for clarity.

#include <stdio.h> // This is the standard input/output library in C, which provides functions for printing to the console and reading input (and more, but we'll see it later).

int main(void)		// This is the main function, which is the entry point of a C program. The 'void' indicates that this function does not take any parameters. In the book it's written a little bit differently, but this is the same thing. In human words - the main function is where the program starts executing.
{			// Function body starts here. The opening curly brace '{' indicates the beginning of a code block. In this case, it marks the start of the main function's body.
	printf("Hello, world!\n"); // This line calls the `printf` function, which is used to print formatted output to the console. The string "Hello, world!\n" is passed as an argument to printf. The '\n' is a newline character, which moves the cursor to the next line after printing the message. We'll learn more about escape sequences and functions later in the book. For now, just remember that this line prints "Hello, world!" to the console.
	/* 
	 * Quick note about string constants.
	 * String constants are sequences of characters enclosed in double quotes. In this case, "Hello, world!\n" is a string constant. The compiler treats string constants as arrays of characters, and they are stored in memory as a sequence of characters followed by a null terminator '\0' to indicate the end of the string. When we pass a string constant to a function like printf, we are actually passing a pointer to the first character of the string in memory. This is an important concept in C programming, and we'll explore it further in later chapters.
	 * String constants cannot be broken up into multiple lines without using the backslash '\' character at the end of a line. If you want to split a long string constant across multiple lines, you can use the backslash to indicate that the string continues on the next line. For example:
	 * 
	 *   printf("This is a long string that \
	 * continues on the next line.\n");
	 * 
	 * If we were to omit the backslash, the compiler would treat the next line as a separate statement, which would result in a compilation error. So, it's important to use the backslash when splitting string constants across multiple lines.
	 * Since our string constant is short, we don't need to worry about splitting it across multiple lines in this case.
	 */
	return 0;	// Technically unnecessary, but it's a good practice to return an integer value from the main function. Returning 0 typically indicates that the program has executed successfully. If you return a non-zero value, it usually indicates that an error occurred during execution. In this case, we return 0 to signal that the program has completed without any issues.
} 			// Function body ends here. The closing curly brace '}' indicates the end of the main function's body. All the code that belongs to the main function is contained within these braces.

// This is all. When the `main` function encounters a `return` statement, it will exit the function and terminate the program. The program will then return control to the operating system, along with the return value (0 in this case) to indicate the program's execution status, which as we remember, would be 'success'.

// example of compilation:
// cc hello.c
// lcc hello.c
// or compiler of your choice

// There is a task for default building in VSCode
// If you're using VSC, just use Ctrl+Shift+B to build and *run* the project with the default task.
// Then we don't have to worry about manual linking and compiling. The default task will handle it for us.
// (Note: The default task is configured in the .vscode/tasks.json file, which is part of the project. You can customize the build and run commands in that file if needed. I used `tcc` as the compiler, but you can change it to any other compiler you prefer, such as `gcc` or `clang`. Just make sure to update the tasks.json file accordingly.
//  Also, worth noting, that tcc technically implements some C99 features and many GNU extentions, though not all. 
//  Because of the fact that we're not trying to appeal to the C99 nerds or to implement any of the newer C concepts (We're using only ANSI C, or K&R C, a.k.a C89 or C90), we can safely use tcc for this project. It will work fine for our purposes. 
//  If you want to use a different compiler, you can do so. Though, honestly, why would you?)

/*
 * Exercise 1-1. Run the "hello, world" program on your system. Experiment with leaving out parts of the program, to see what error messages you get.
 * Exercise 1-2. Experiment to find out what happens when `printf`'s argument string contains some character. Try with the backslash character `\` followed by a character that has a special meaning, such as `\n` for newline or `\t` for tab. Observe how the output changes and how the program behaves when you include or omit these escape sequences.
 */