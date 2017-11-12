#include <stdio.h>
#include <string.h>

int main()
{
	int n, delta, result;
	char name1[12], name2[12];

	scanf("%d", &n);
	scanf("%s %s", name1, name2);
	delta = strcmp(name1, name2)&0x80000000;
	for (int i = 2; i < n; i++) {
		strcpy(name1, name2);
		scanf("%s", name2);
		if ((strcmp(name1, name2)&0x80000000) != delta) {
			printf("NEITHER");
			return 0;
		}
	}
	printf(delta == 0 ? "DECREASING" : "INCREASING");
	return 0;
}
