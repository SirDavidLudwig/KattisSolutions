#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	string charMap;
	getline(cin, charMap);
	reverse(charMap.begin(), charMap.end());
	int i = 0, len = charMap.size(), zeros = 0, pZeros = 0, t = 0;

	for (i = 0; i < len; i++) {
		if (charMap[i] == '0') {
			zeros++;
			pZeros++;
		} else if (charMap[i] == '1') {
			t += zeros;
			t += pZeros + zeros;
		} else {
			t += zeros;
			t += pZeros + zeros;
			pZeros++;
		}
	}
	cout << (t % 1000000007) << endl;
	return 0;
}
