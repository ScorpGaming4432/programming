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

/*
 * The (nowadays) small group of assembly fans will recognize that the structure of C (ANSI) can sometimes be VERY similar to assembly language.
 * As a matter of fact, the C language was designed to be a high-level language that could be compiled into efficient assembly code.
*/
/*
 * This file is the first example of variation inside the main function declaration. The main function can be declared in several ways according to ANSI C standard.
 * Function declarations follow simple rules:
 *  1. The return type of a function *can* be specified before the function name. By default - `int`.
 *  2. Function names must be unique within a program and begin with a letter or an underscore, followed by letters, digits, or underscores. 
 *     Only then the function name can be followed by a pair of parentheses `()` that may contain parameters (if any) for the function. 
 *  3. A function HAS to have ONE implementation. This means that we can't have so-called "function overloading" in C. 
 *     Also, it means that a function needs to have a body (implementation) defined by a pair of curly braces `{}`. The body contains the code that will be executed when the function is called.
 * From the rules above, you probably noticed that a declaration and an implementation can be two different things and in fact, they *can* be separated!
 * We'll see examples of this in the future.
*/