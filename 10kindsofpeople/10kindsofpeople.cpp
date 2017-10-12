#include <chrono>
#include <cmath>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;
using namespace std::chrono;

struct Location
{
	const int  x, y;
	int  pathDistance = -1;
	int  distance     = -1;
	int  done         = -1;
	char value;
	Location(int y, int x) : x(x), y(y) {}
};

struct LocationCompare
{
	bool operator() (const Location *lhs, const Location *rhs) {
		return lhs->distance >= rhs->distance;
	}
};


Location *maze[1002][1002] = {nullptr};
int main()
{
	auto t = high_resolution_clock::now();
	typedef priority_queue<Location*, vector<Location*>, LocationCompare> location_queue;
	int i, j;
	int r, c;
	int x, y;
	int cases, x0, y0, x1, y1;
	Location *loc1, *loc2;

	cin >> r >> c;

	for (i = 1; i <= r; i++) {
		for (j = 1; j <= c; j++) {
			maze[i][j] = new Location{i,j};
			cin >> maze[i][j]->value;
		}
	}
	
	cin >> cases;
	for (i = 0; i < cases; i++) {
		location_queue next;
		cin >> y0 >> x0 >> y1 >> x1;
		if (maze[y0][x0]->value != maze[y1][x1]->value) {
			cout << "neither" << endl;
			continue;
		}
		maze[y0][x0]->pathDistance = 0;
		maze[y0][x0]->distance     = 0;
		next.push(maze[y0][x0]);
		while (!next.empty()) {
			loc1 = next.top();
			next.pop();

			if (loc1->x == x1 && loc1->y == y1) {
				cout << (maze[y0][x0]->value == '0' ? "binary" : "decimal") << endl;
				goto nextIter;
			}
			if (loc2 = maze[loc1->y+1][loc1->x]) {
				if (loc2->value == maze[y0][x0]->value && loc2->done != i) {
					loc2->pathDistance = loc1->pathDistance + 1;
					loc2->distance     = loc2->pathDistance + abs(x1-loc2->x) + abs(y1-loc2->y);
					loc2->done         = i;
					next.push(loc2);
				}
			}
			if (loc2 = maze[loc1->y-1][loc1->x]) {
				if (loc2->value == maze[y0][x0]->value && loc2->done != i) {
					loc2->pathDistance = loc1->pathDistance + 1;
					loc2->distance     = loc2->pathDistance + abs(x1-loc2->x) + abs(y1-loc2->y);
					loc2->done         = i;
					next.push(loc2);
				}
			}
			if (loc2 = maze[loc1->y][loc1->x+1]) {
				if (loc2->value == maze[y0][x0]->value && loc2->done != i) {
					loc2->pathDistance = loc1->pathDistance + 1;
					loc2->distance     = loc2->pathDistance + abs(x1-loc2->x) + abs(y1-loc2->y);
					loc2->done         = i;
					next.push(loc2);
				}
			}
			if (loc2 = maze[loc1->y][loc1->x-1]) {
				if (loc2->value == maze[y0][x0]->value && loc2->done != i) {
					loc2->pathDistance = loc1->pathDistance + 1;
					loc2->distance     = loc2->pathDistance + abs(x1-loc2->x) + abs(y1-loc2->y);
					loc2->done         = i;
					next.push(loc2);
				}
			}
		}
		cout << "neither" << endl;
		nextIter:
			continue;
	}
	cout << duration_cast<chrono::microseconds>(high_resolution_clock::now()-t).count()*0.000001 << endl;
	return 0;
}
