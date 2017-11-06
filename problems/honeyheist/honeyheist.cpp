#include <cmath>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Cell
{
	int index;
	int length;
	bool checked = false;
	vector<Cell*> links;
	Cell(int index): index(index) {}
};

void link(Cell *a, Cell *b)
{
	if (a == nullptr || b == nullptr)
		return;
	a->links.push_back(b);
	b->links.push_back(a);
}

bool readCell(Cell **cells, int cellCount, int index, int *hard, int &hardIndex)
{
	if (index == hard[hardIndex]) {
		cells[index] = nullptr;
		hardIndex++;
		return false;
	}
	cells[index] = new Cell(index+1);
	return true;
}

void createMap(int r, Cell **cells, int cellCount, int *hard, int &hardIndex)
{
	int i, j;
	int index = 0;
	for (i = 0; i < r; i++) {
		for (j = 0; j < r+i; j++) {
			if (readCell(cells, cellCount, index, hard, hardIndex)) {
				if (j > 0) {
					link(cells[index-1], cells[index]);
				}
				if (i > 0) {
					if (j > 0)
						link(cells[index-r-i], cells[index]);
					if (j < r+i-1)
						link(cells[index-r-i+1], cells[index]);
				}
			}
			index++;
		}
	}
	for (i = 0; i < r-1; i++) {
		for (j = 0; j < 2*r-2-i; j++) {
			if (readCell(cells, cellCount, index, hard, hardIndex)) {
				if (j > 0) {
					link(cells[index-1], cells[index]);
				}
				link(cells[index-(2*r-2-i)-1], cells[index]);
				link(cells[index-(2*r-2-i)], cells[index]);
			}
			index++;
		}
	}
}

int main()
{
	int i, j;
	int r, n, a, b, x;
	cin >> r >> n >> a >> b >> x;

	int cellCount = pow(r, 3) - pow(r - 1, 3);
	Cell *cells[cellCount];

	int hardIndex = x > 0;
	int hard[x+2];
	hard[0] = hard[x+1] = -1;
	for (i = 1; i <= x; i++) {
		cin >> hard[i];
		hard[i]--;
	}

	createMap(r, cells, cellCount, hard, hardIndex);

	queue<Cell*> next;
	Cell *current, *end = cells[b-1];
	next.push(cells[a-1]);
	cells[a-1]->length = 0;
	cells[a-1]->checked = true;
	while (!next.empty()) {
		current = next.front();
		next.pop();
		cout << current->index << endl;

		if (current->length > n)
			break;
		if (current == end) {
			cout << current->length << endl;
			return 0;
		}

		for (auto it = current->links.begin(); it != current->links.end(); it++) {
			if (!(*it)->checked) {
				(*it)->checked = true;
				(*it)->length = current->length + 1;
				next.push(*it);
			}
		}
	}

	cout << "No" << endl;

	return 0;
}
