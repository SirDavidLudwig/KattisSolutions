#include <iostream>

using namespace std;

int fib(int n, int *memo)
{
	if (n == 0 || n == 1)
		return n;
	if (memo[n] != -1)
		return memo[n];
	int result = fib(n-1, memo) + fib(n-2, memo);
	memo[n] = result;
	return result;
}

int main()
{
	int n, fibs[46];
	for (int i = 0; i < 46; i++)
		fibs[i] = -1;

	cin >> n;
	cout << fib(n-1, fibs) << ' ' << fib(n, fibs) << endl;

	return 0;
}
