#include <cmath>
#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
	int stars;
	double rows;
	cin >> stars;
	printf("%d:\n", stars);

	for (int i = 2; i <= ceil(stars/2.0); i++) {
		if (stars % (i+i-1) == 0|| (i+i-1) * floor(stars / (i+i-1)) + i == stars) {
			printf("%d,%d\n", i, i-1);
		}
		if (stars % i == 0) {
			printf("%d,%d\n", i, i);
		}
	}

	return 0;
}
