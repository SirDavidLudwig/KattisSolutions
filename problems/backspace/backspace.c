#include <stdio.h>

int main()
{
	char chars[1000000];
	int index = 0;
	while (scanf("%c", &chars[index]) != -1) {
		if (chars[index++] == '<')
			index -= 2;
	}
	chars[index] = 0x0;
	printf("%s\n", chars);
	return 0;
}
