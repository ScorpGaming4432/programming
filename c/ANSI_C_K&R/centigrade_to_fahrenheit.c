/* 
 * Print Fahrenheit-Celsius table for fahrenheit ranges [0, 300] with a set step size of 20.

 * This program demonstrates the use of a while loop to iterate through a range of Fahrenheit temperatures using a formula to convert them to Celsius. 
 * The formula is "C=(5/9)(F-32)", where C is the Celsius temperature and F is the Fahrenheit temperature.
 * The program prints a table of Fahrenheit and Celsius values to the console.
 */

#include <stdio.h>

main()  // This is the first example of variation inside the main function declaration. (See below)
{
	int fahr, celsius;  // This is a variable declaration. It tells the program that we want to allocate memory for two integer variables named `fahr` and `celsius`. The `int` keyword indicates that these variables will hold integer values. In C, variable declarations are typically placed at the beginning of a block of code, before any executable statements. This is a requirement in the C89/C90 standard, which is the version of C that this program adheres to. In later versions of C (C99 and beyond), variable declarations can be placed anywhere within a block of code, but for compatibility with older standards, we declare them at the beginning here.
	int lower, upper, step;  // We can have as many variables in a decleration as we want, separated by commas. Reminder that all variables will be the same type when we do that.
	lower = 0;   /* lower limit of temperature scale */  // This is an assignment statement (kinda like a `definition` or `implementation`). It assigns the value 0 to the variable `lower`. The `=` operator is used for assignment in C. In this case, we are starting our temperature conversion from 0 degrees Fahrenheit.
	upper = 300; /* upper limit */  // Another assignment.
	step = 20;   /* step size */
	fahr = lower;  // We can assign the value of one variable to another. In this case, we are initializing the `fahr` variable with the value of `lower`, which is 0. This means that our first iteration of the loop will start with a Fahrenheit temperature of 0 degrees.
	while (fahr <= upper)  // This is a while loop. (See below)
	{  // Open a block of code (body of the loop)
		celsius = 5 * (fahr - 32) / 9;  // This is the formula for converting Fahrenheit to Celsius. The calculation is performed using integer arithmetic, which means that any fractional part of the result will be truncated (not rounded). This is important to note because it can lead to a loss of precision in the conversion. 
		// In this case, we are using integer division, which means that the result will be an integer value. If we wanted to preserve the fractional part, we would need to use floating-point arithmetic instead. We'll see how to do that later when learning about data types.
		printf("%d\t%d\n", fahr, celsius);  // This is far too complicated for a beginner to understand. (See below "string formatting" comment)
		fahr = fahr + step;  // Assignment can be a computation as well. In this case, we are assigning `fahr` the value of `fahr + step`, which means that we are incrementing the Fahrenheit temperature by the step size (20 degrees) for the next iteration of the loop. This is how we move through the range of temperatures from `lower` to `upper`.
	}  // Close the block of code (body of the loop)

	// Notice the lack of a return statement. It is not necessary, but it's good practice to `return 0;`.
}


// The (nowadays) small group of assembly fans will recognize that the structure of C (ANSI) can sometimes be VERY similar to assembly language.
// As a matter of fact, the C language was designed to be a high-level language that could be compiled into efficient assembly code.
// Of course with every new standard, C has become more and more abstracted from the hardware, but the core principles of C remain rooted in its low-level capabilities.

/* Functions: declaration and implementation
 * This file is the first example of variation inside the main function declaration. The main function can be declared in several ways according to ANSI C standard, we'll focus on `main` itself later.
 * Function declarations follow simple rules:
 *  1. The return type of a function *can* be specified before the function name. By default - `int`.
 *  2. Function names must be unique within a program and begin with a letter or an underscore, followed by letters, digits, or underscores. 
 *      Only then the function name can be followed by a pair of parentheses `()` that may contain parameters (if any) for the function. 
 *  3. A function HAS to have ONE implementation. 
 *      This means that we can't have so-called "function overloading" in C. 
 *      Also, it means that a function needs to have a body (implementation) defined by a pair of curly braces `{}`. The body contains the code that will be executed when the function is called.
 * From the rules above, you probably noticed that a declaration and an implementation can be two different things and in fact, they *can* be separated!
 * We'll see examples of this in the future.
 */

/* A `while` loop
 * A `while` loop is a control flow statement that allows code to be executed repeatedly based on a given boolean condition. 
 * The loop will continue to execute as long as the condition evaluates to true. Once the condition evaluates to false, the loop will terminate, and the program will continue executing the code that follows the loop.
 * The syntax of a `while` loop is as follows:
 * 
 * while (condition) {
 *     // Code to be executed repeatedly
 * }
 * 
 * In this program, we use a `while` loop to iterate through a range of Fahrenheit temperatures from `lower` (0) to `upper` (300) with a step size of `step` (20). 
 * The loop continues to execute as long as the value of `fahr` is less than or equal to `upper`. Inside the loop, we calculate the corresponding Celsius temperature using the formula and print both Fahrenheit and Celsius values to the console. 
 * After printing, we increment the value of `fahr` by `step` for the next iteration.
 * 
 * It's a common mistake to accidentally create so-called "endless loops" when using `while` loops. This happens when the condition never evaluates to false, causing the loop to run indefinitely.
 * Just make sure to actually have a break condition in your loop.
   (here we don't do that cuz we're fucking pro #yolo)
 */

/* String formatting
 * Here we go. The most complicated part of this program. 
 * The `printf` function is used to print formatted output to the console. It takes a format string as its first argument, followed by a variable number of additional arguments that correspond to the format specifiers in the format string.
 * This sounds like a bunch of gibberish, but it's actually quite simple. The format string is a string that contains text and format specifiers, which are placeholders for the values that will be printed. 
 * The format specifiers begin with a percent sign `%` followed by a character that indicates the type of value to be printed.
 * So, for example if we would want to print an `int`, we'd use a specifier "%d". So the function would look like: `printf("%d", int_variable);` and it would print the value of `int_variable` to the console.
 * The additional elements of a format string go as follows:
 *  %[flags][[-]width][.precision][length]specifier
 *  - flags: optional, can be used to modify the output (e.g., left-justify, pad with zeros, etc.)
 *  - width: optional, specifies the minimum number of characters to be printed. If the value to be printed is shorter than the specified width, it will be padded with spaces (or zeros if the '0' flag is used).
 *    in case a '-' sign is used, the output will be left-justified within the specified width.
 *  - precision: optional, specifies the number of digits to be printed after the decimal point for floating-point numbers, or the maximum number of characters to be printed for strings.
 *  - length: optional, specifies the size of the argument (e.g., `l` for long, `h` for short, etc.). This is used to ensure that the correct type of argument is passed to the function.
 *  - specifier: required, indicates the type of value to be printed.
 * The list of specifiers is as follows:
 *  - `d` or `i`: signed decimal integer
 *  - `u`: unsigned decimal integer
 * - `f`: floating-point number (decimal notation)
 * - `e` or `E`: floating-point number (scientific notation)
*/