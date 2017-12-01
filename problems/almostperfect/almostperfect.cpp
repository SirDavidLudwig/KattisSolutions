#include <cmath>
#include <stdio.h>
#include <stdlib.h>

int divisors(int n)
{
	int total = 0;
	for (int i = 2; i <= sqrt(n); i++) {
		if (n%i == 0) {
			if (n/i == i) {
				total += i;
			} else {
				total += i + n/i;
			}
		}
	}
	return total+1;
}

int main()
{
	for (int num, d; scanf("%d", &num) != -1;) {
		d = divisors(num);
		printf("%d ", num);
		if (d == num)
			printf("perfect\n");
		else if (abs(abs(num)-abs(d)) < 3)
			printf("almost perfect\n");
		else
			printf("not perfect\n");
	}
	return 0;
}
