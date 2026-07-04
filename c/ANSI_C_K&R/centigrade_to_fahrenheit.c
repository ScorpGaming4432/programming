/* 
 * Print Fahrenheit-Celsius table for fahrenheit ranges [0, 300] with a set step size of 20.

 * This program demonstrates the use of a while loop to iterate through a range of Fahrenheit temperatures using a formula to convert them to Celsius. 
 * The formula is "C=(5/9)(F-32)", where C is the Celsius temperature and F is the Fahrenheit temperature.
 * The program prints a table of Fahrenheit and Celsius values to the console.
 */

#include <stdio.h>

main()  // This is the first example of variation inside the main function declaration. (See below)
{
	int fahr, celsius;  // This is a variable declaration. It tells the program
	int lower, upper, step;
	lower = 0;   /* lower limit of temperature scale */
	upper = 300; /* upper limit */
	step = 20;   /* step size */
	fahr = lower;
	while (fahr <= upper)
	{
		celsius = 5 * (fahr - 32) / 9;
		printf("%d\t%d\n", fahr, celsius);
		fahr = fahr + step;
	}
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