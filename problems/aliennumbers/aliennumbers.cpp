#include <iostream>
#include <math.h>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

int main()
{
	int i, j, decimal;
	int testCases;
	cin >> testCases;

	string number, source, target;
	int sourceLen, targetLen;
	for (i = 0; i < testCases; i++) {
		decimal = 0;
		cin >> number >> source >> target;
		sourceLen = source.length();
		targetLen = target.length();
		unordered_map<char, int> sourceMap;
		char result[94];
		for (j = 0; j < sourceLen; j++)
			sourceMap[source[j]] = j;
		for (j = 0; j < number.length(); j++) {
			decimal += sourceMap[number[j]]*pow(sourceLen, number.length()-j-1);
		}
		result[j = 0] = target[decimal % targetLen];
		while (decimal > 0) {
			decimal /= targetLen;
			result[++j] = target[decimal % targetLen];
		}
		cout << "Case #" << (i+1) << ": ";
		bool beginZero = true;
		for (j = j-1; j >= 0; j--) {
			if (result[j] == target[0] && beginZero)
				continue;
			cout << result[j];
			beginZero = false;
		}
		cout << endl;
	}
	return 0;
}
