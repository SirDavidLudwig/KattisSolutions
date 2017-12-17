#include <iostream>
#include <set>
#include <string>
#include <unordered_set>

using namespace std;

struct Letter
{
	const char letter;
	Letter *parent = nullptr;
	unordered_set<Letter*> children;
	Letter(char letter) : letter(letter) {}
};

typedef pair<int, char> LetterLex;

bool addChild(Letter *letter, Letter *child, bool keep = false)
{
	// Check if this letter is the same as the parent (making it impossible)
	if (letter == child || child->children.count(letter))
		return false;

	// Add child and further children to the parents's child set
	letter->children.insert(child);
	letter->children.insert(child->children.begin(), child->children.end());
	if (!keep)
		child->parent = letter;

	// If a parent exists, add this child to that parent.
	if (letter->parent)
		return addChild(letter->parent, child, true);
	return true;
}

int main()
{
	char m;
	int i, j, n;
	cin >> m >> n;
	int charCount = m-96;

	Letter *chars[charCount];
	for (i = 0; i < charCount; i++)
		chars[i] = new Letter(char(97+i));

	string line1;
	string line2;
	cin >> line1;
	for (i = 1; i < n; i++) {
		for (cin >> line2, j = 0; j < min(line1.size(), line2.size()); j++) {
			if (line1[j] != line2[j]) {
				if (!addChild(chars[line1[j]-97], chars[line2[j]-97])) {
					cout << "IMPOSSIBLE" << endl;
					return 0;
				}
				break;
			}
		}
		line1 = line2;
	}
	set<LetterLex, greater<LetterLex>> charOrder;
	for (i = 0; i < charCount && chars[i]->parent; i++);

	charOrder.insert(make_pair(chars[i]->children.size(), chars[i]->letter));
	for (Letter *l : chars[i]->children) {
		charOrder.insert(make_pair(l->children.size(), l->letter));
	}

	if (charOrder.size() == charCount) {
		for (LetterLex l : charOrder)
			cout << l.second;
		cout << endl;
		return 0;
	}
	cout << "AMBIGUOUS" << endl;

	return 0;
}
