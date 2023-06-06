#include <stdio.h>

int main(void)
{
	int FirstDigit, SecondDigit;

	for (FirstDigit = 0; FirstDigit < 10; FirstDigit++)
	{
		for (SecondDigit = FirstDigit + 1; SecondDigit < 10; SecondDigit++)
		{
			printf("%d%d, ", FirstDigit, SecondDigit);
		}
	}
	putchar('\n');
	return (0);
}
