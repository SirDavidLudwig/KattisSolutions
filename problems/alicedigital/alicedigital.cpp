#include <stdio.h>
#include <vector>

using namespace std;

int main()
{
	int i, j, n, m, t, v, max, total;
	bool divided;
	for (scanf("%d", &t), i = 0; i < t; i++) {
		vector<int> values;
		scanf("%d %d", &n, &m);
		for (divided = true, j = total = 0; j < n; j++) {
			scanf("%d", &v);
			if (v < m) {
				if (!divided) {
					values.push_back(total);
					divided = true;
				}
				total = 0;
			}
			else if (v == m) {
				values.push_back(total);
				if (!divided)
					values.push_back(total);
				total = 0;
				divided = false;
			} else
				total += v;
		}
		if (!divided)
			values.push_back(total);
		for (max = 0, j = 1;  j < values.size(); j += 2) {
			if (values[j] + values[j-1] > max)
				max = values[j] + values[j-1];
		}
		printf("%d\n", max+m);
	}
	return 0;
}
