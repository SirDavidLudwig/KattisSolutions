#include <stdio.h>

using namespace std;

struct Node
{
	int value;
	int height;
	Node *parent = nullptr;
	Node *left = nullptr;
	Node *right = nullptr;
	Node *least = nullptr;
	Node *greatest = nullptr;
};

void insert(int value, Node *& root, int &height, Node *parent = nullptr)
{
	if (root == nullptr) {
		root = new Node;
		root->value = value;
		root->height = ++height;
		root->least = root->greatest = root;
		root->parent = parent;
	} else {
		if (value > root->value) {
			if (value > root->greatest->value) {
				insert(value, root->greatest->right, height = root->greatest->height, root->greatest);
				root->greatest = root->greatest->right;
			} else if (root != root->greatest && value > root->greatest->parent->value) {
				insert(value, root->greatest->left, height = root->greatest->height, root->greatest);
			}
			else
				insert(value, root->right, height = root->height, root);
		}
		else {
			if (value < root->least->value) {
				insert(value, root->least->left, height = root->least->height, root->least);
				root->least = root->least->left;
			}
			else if (root != root->least && value < root->least->parent->value) {
				insert(value, root->least->right, height = root->least->height, root->least);
			}
			else
				insert(value, root->left, height = root->height, root);
		}
	}
}

int main()
{
	unsigned long long c;
	int h, i, n, v;
	Node *root = nullptr;
	Node *greatest = nullptr;
	Node *lowest = nullptr;
	int &b = v;
	scanf("%d", &n);

	for (c = i = 0; i < n; i++) {
		scanf("%d", &v);
		h = -1;
		insert(v, root, h);
		printf("%lld\n", (c += h));
	}
	return 0;
}
