#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

struct Letter
{
	const char letter;
    int lexOrder = 0;
	Letter(char letter) : letter(letter) {}
};

int main()
{
	int  i, j;
	char letterEnd;
	int  lineCount;
	char lines[1001][1001] = {0};
	cin >> letterEnd >> lineCount;

	unordered_map<char, Letter*> nodes;
	for (i = 97; i <= letterEnd; i++) {
		nodes[(char)i] = new Letter((char)i);
	}

	cin.ignore();
	cin.getline(lines[0], 1001);
    int lex;
    char currentChar;
    for (i = 0; i < lineCount-1; i++) {
		cin.getline(lines[i+1], 1001);
		j = 0;
		do {
            currentChar = lines[i][j];
            if (lines[i][j] != lines[i+1][j] && lines[i+1][j] != 0) {
                nodes[lines[i+1][j]]->lexOrder++;
				if (nodes[lines[i][j]]->setNext(nodes[lines[i+1][j]]))
                    break;
			}
		} while (lines[i][++j] != 0);
	}

    Letter *letter = nullptr;
    for (i = 97; i <= letterEnd; i++)
        if (nodes[(char)i]->lexOrder == 0) {
            if (letter) {
                cout << "AMBIGUOUS" << endl;
                return 0;
            }
            letter = nodes[(char)i];
        }

    if (!letter) {
        cout << "IMPOSSIBLE" << endl;
        return 0;
    }

    for (i = 97; i <= letterEnd; i++)
        if (nodes[(char)i]->prev == nullptr) {
            letter = nodes[(char)i];
        break;
    }

	if (letter) {
		string alphabet = "";
		while (letter && letter->iter == 0) {
			alphabet += letter->letter;
			letter->iter++;
			letter = letter->next;
		}
		if ((int)alphabet.length() == (int)letterEnd-96)
			cout << alphabet << endl;
		else 
			cout << "AMBIGUOUS" << endl;
	} else {
		cout << "IMPOSSIBLE2" << endl;
	}

	return 0;
}
