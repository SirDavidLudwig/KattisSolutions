#include <stdio.h>

int main()
{
	int i, j, k, m, n, t;
	char digit;
	for (scanf("%d", &t), i = 0; i < t; i++) {
		scanf("%d %d\n", &n, &m);
		int digitCount[m];
		for (j = 0; j < m; j++)
			digitCount[j] = 0;
		for (j = 0; j < n; j++) {
			for (k = 0; k < m; k++) {
				scanf("%c\n", &digit);
				if (digit == 49)
					digitCount[k]++;
			}
		}
		double nOver2 = n/2.0;
		for (k = 0; k < m; k++) {
			printf((digitCount[k] >= nOver2) ? "1": "0");
		}
		printf("\n");
	}
	return 0;
}
