#include <iostream>

using namespace std;

int nextGroup = 0;

struct Node
{
	bool type;
	int *group;
	Node() {
		group = new int;
		*group = nextGroup++;
	}
	Node(int *group) : group(group) { }
};


int main()
{
	cout << "Done";
	return 0;
}
