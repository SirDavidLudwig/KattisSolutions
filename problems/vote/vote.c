#include <stdio.h>

int main()
{
	int i, j, c, t, n, tot, win, tie;
	int votes[10];
	for (i = 0, scanf("%d", &t); i < t; i++) {
		for (j = tot = win = tie = 0, scanf("%d", &c); j < c; j++) {
			scanf("%d", &votes[j]);
			tot += votes[j];
			if (votes[j] > votes[win]) {
				win = j;
				tie = 0;
			} else if (votes[j] == votes[win] && j != win) {
				tie = 1;
			}
		}
		if (tie) {
			printf("no winner\n");
		} else if (votes[win] > tot/2)
			printf("majority winner %d\n", win+1);
		else
			printf("minority winner %d\n", win+1);
	}
	return 0;
}
