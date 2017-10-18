#include <iostream>

using namespace std;

int main()
{
	int i, j, dir, start, end;
	int grid[4][4] = {0};
	for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++)
			cin >> grid[i][j];

	cin >> dir;

	if (dir == 0) { // left
		for (i = 0; i < 4; i++) {
			start = 0;
			for (end = 1; end < 4; end++) {
				if (grid[i][end] == 0)
					continue;
				if (grid[i][start] == 0) {
					grid[i][start] = grid[i][end];
					grid[i][end] = 0;
				} else if (grid[i][start] == grid[i][end]) {
					grid[i][start++] *= 2;
					grid[i][end] = 0;
				} else if (grid[i][++start] == 0){
					grid[i][start] = grid[i][end];
					grid[i][end] = 0;
				}
			}
		}
	} else if (dir == 1) { // up
		for (i = 0; i < 4; i++) {
			start = 0;
			for (end = 1; end < 4; end++) {
				if (grid[end][i] == 0)
					continue;
				if (grid[start][i] == 0) {
					grid[start][i] = grid[end][i];
					grid[end][i] = 0;
				} else if (grid[start][i] == grid[end][i]) {
					grid[start++][i] *= 2;
					grid[end][i] = 0;
				} else if (grid[++start][i] == 0){
					grid[start][i] = grid[end][i];
					grid[end][i] = 0;
				}
			}
		}
	} else if (dir == 2) { // right
		for (i = 0; i < 4; i++) {
			start = 3;
			for (end = 2; end >= 0; end--) {
				if (grid[i][end] == 0)
					continue;
				if (grid[i][start] == 0) {
					grid[i][start] = grid[i][end];
					grid[i][end] = 0;
				} else if (grid[i][start] == grid[i][end]) {
					grid[i][start--] *= 2;
					grid[i][end] = 0;
				} else if (grid[i][--start] == 0){
					grid[i][start] = grid[i][end];
					grid[i][end] = 0;
				}
			}
		}
	} else if (dir == 3) { // down
		for (i = 0; i < 4; i++) {
			start = 3;
			for (end = 2; end >= 0; end--) {
				if (grid[end][i] == 0)
					continue;
				if (grid[start][i] == 0) {
					grid[start][i] = grid[end][i];
					grid[end][i] = 0;
				} else if (grid[start][i] == grid[end][i]) {
					grid[start--][i] *= 2;
					grid[end][i] = 0;
				} else if (grid[--start][i] == 0){
					grid[start][i] = grid[end][i];
					grid[end][i] = 0;
				}
			}
		}
	}

	for (i = 0; i < 4; i++)
		for (j = 0; j < 4; j++)
			cout << grid[i][j] << ((j < 3) ? " " : "\n");

	return 0;
}
