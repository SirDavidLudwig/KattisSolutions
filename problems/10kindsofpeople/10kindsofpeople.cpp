#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Node
{
	char type;
	int group = -1;
	int x, y;
	Node(int x, int y) : x(x), y(y) {}
	bool operator==(const Node &other) {
		return type == other.type && group == other.group;
	}
};

Node *map[1002][1002] = {nullptr};
vector<Node*> nodes0, nodes1;

void prepare_map(int r, int c)
{
	int i, j;
	map[1][1] = new Node(1, 1);
	cin >> map[1][1]->type;
	(map[1][1]->type == '1' ? nodes1 : nodes0).push_back(map[1][1]);
	for (j = 2; j <= c; j++) {
		map[1][j] = new Node(j, 1);
		cin >> map[1][j]->type;
		if (map[1][j-1]->type != map[1][j]->type)
			(map[1][j]->type == '1' ? nodes1 : nodes0).push_back(map[1][j]);
	}
	for (i = 2; i <= r; i++) {
		map[i][1] = new Node(1, i);
		cin >> map[i][1]->type;
		if (map[i-1][1]->type != map[i][1]->type)
			(map[i][1]->type == '1' ? nodes1 : nodes0).push_back(map[i][1]);
		for (j = 2; j <= c; j++) {
			map[i][j] = new Node(j, i);
			cin >> map[i][j]->type;
			if (map[i][j-1]->type != map[i][j]->type && map[i-1][j]->type != map[i][j]->type)
				(map[i][j]->type == '1' ? nodes1 : nodes0).push_back(map[i][j]);
		}
	}
}

int main()
{
	int i, j;
	int n, r, c;
	int x0, y0, x1, y1;
	cin >> r >> c;

	prepare_map(r, c);

	int nextGroup = 0;
	queue<Node*> search;
	Node *current, *next;
	vector<Node*> nodeGroups[] = {nodes0, nodes1};
	for(i = 0; i < 2; i++) {
		int size = nodeGroups[i].size();
		for (j = 0; j < size; j++) {
			if (nodeGroups[i][j]->group != -1)
				continue;
			nodeGroups[i][j]->group = nextGroup++;
			search.push(nodeGroups[i][j]);
			while (!search.empty()) {
				current = search.front();
				search.pop();

				if (next = map[current->y-1][current->x]) {
					if (next->group == -1 && next->type == current->type) {
						next->group = current->group;
						search.push(next);
					}
				}
				if (next = map[current->y+1][current->x]) {
					if (next->group == -1 && next->type == current->type) {
						next->group = current->group;
						search.push(next);
					}
				}
				if (next = map[current->y][current->x-1]) {
					if (next->group == -1 && next->type == current->type) {
						next->group = current->group;
						search.push(next);
					}
				}
				if (next = map[current->y][current->x+1]) {
					if (next->group == -1 && next->type == current->type) {
						next->group = current->group;
						search.push(next);
					}
				}
			}
		}
	}

	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> y0 >> x0 >> y1 >> x1;
		if (*map[y0][x0] == *map[y1][x1])
			cout << (map[y0][x0]->type == '1' ? "decimal" : "binary") << endl;
		else
			cout << "neither" << endl;
	}

	return 0;
}
