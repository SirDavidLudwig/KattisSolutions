#include <stdio.h>
#include <string.h>

int goodMod(int value, int mod)
{
	int result = value % mod;
	if (result >= 0)
		return result;
	return mod + result;
}

int main()
{
	char m[10];
	int d, y, h1, min1, h2, min2, h;
	while (scanf("%s %d %d %d:%d %d:%d", m, &d, &y, &h1, &min1, &h2, &min2) != -1) {
		h = h2 - h1 - ((min2 - min1) % 60 < 0 ? 1 : 0);
		printf("%s %d %d %d hours %d minutes\n", m, d, y, h, goodMod(min2 - min1, 60));
	}
	return 0;
}
