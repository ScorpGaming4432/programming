/* 
 * Print Fahrenheit-Celsius table for fahrenheit ranges [0, 300] with a set step size of 20.

 * This program does the same as the previous one, but we wanna showcase how to use floating point numbers
 * The formula is still "C=(5/9)(F-32)", where C is the Celsius temperature and F is the Fahrenheit temperature.
 */

#include <stdio.h>

main()
{
	float fahr, celsius;
	float lower, upper, step;
	lower = 0;
	upper = 300;
	step = 20;
	fahr = lower;
	while (fahr <= upper)
	{
		celsius = 5.0 * (fahr - 32.0) / 9.0;
		printf("%3.0f\t%3.2f\n", fahr, celsius);
		fahr = fahr + step;
	}
}
