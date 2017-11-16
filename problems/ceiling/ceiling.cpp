#include <iostream>
#include <string>
#include <set>

using namespace std;

struct Node
{
	int value;
	Node *l = nullptr;
	Node *r = nullptr;
	Node(int value): value(value) {}
	string shape(int depth = 0)
	{
		string shape = "";
		string end = "";
		if (l) {
			shape += "l" + to_string(depth);
			end += l->shape(depth+1);
		} else
			shape += "n" + to_string(depth);
		if (r) {
			shape += "r" + to_string(depth);
			end += r->shape(depth+1);
		} else
			shape += "n" + to_string(depth);
		return shape + end;
	}
};

void insert(int value, Node *&node)
{
	if (node == nullptr)
		node = new Node(value);
	else if (value < node->value)
		insert(value, node->l);
	else
		insert(value, node->r);
}

int main()
{
	int i, j, k, n, v;
	cin >> n >> k;
	Node *trees[n];
	set<string> shapes;
	for (i = 0; i < n; i++) {
		cin >> v;
		trees[i] = new Node(v);
		for (j = 1; j < k; j++) {
			cin >> v;
			insert(v, trees[i]);
		}
	}

	int shapeCount = 0;
	for (Node *tree : trees) {
		string shape = tree->shape();
		if (!shapes.count(shape)) {
			shapeCount++;
			shapes.insert(shape);
		}
	}

	cout << shapeCount << endl;

	return 0;
}
