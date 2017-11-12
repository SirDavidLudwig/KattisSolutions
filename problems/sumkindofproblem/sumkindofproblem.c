#include <stdio.h>

int main()
{
	int i, k, n, n2, n3, t;
	scanf("%d", &t);
	for (i = 0; i < t; i++) {
		scanf("%d %d", &k, &n);
		n2 = n*n;
		n3 = n2+n;
		printf("%d %d %d %d\n", k, n3>>1, n2, n3);
	}
	return 0;
}
