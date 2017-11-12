#include <stdio.h>

int main()
{
	int i;
	char word[30];
	scanf("%s", word);
	for (i = 1; word[i] != '\0'; i++)
		if (word[i] == 's' && word[i-1] == 's') {
			printf("hiss");
			return 0;
		}
	printf("no hiss");
	return 0;
}
