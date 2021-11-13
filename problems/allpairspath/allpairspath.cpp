#include <algorithm>
#include <iostream>
#include <limits>

using namespace std;

#define INF std::numeric_limits<double>::infinity()
#define NINF -INF

double inf_add(double a, double b) {
	// a or b being INF means there's no edge, so nothing to add
	if (a == INF || b == INF) {
		return INF;
	}
	return a + b;
}

int main()
{
	int n, m, q;
	int i, j, k;
	int u, v, w;
	double dist;

	// graph of maximum size
	double graph[150][150];

	cin >> n >> m >> q;
	while (n != 0) {

		// Reset distances
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				graph[i][j] = (i == j) ? 0.0 : INF;
			}
		}

		// Load edges
		for (i = 0; i < m; i++) {
			cin >> u >> v >> w;
			graph[u][v] = min(graph[u][v], (double) w);
		}

		// Shortest paths through k
		for (k = 0; k < n; k++) {
			for (i = 0; i < n; i++) {
				for (j = 0; j < n; j++) {
					dist = min(inf_add(graph[i][k], graph[k][j]), graph[i][j]);
					if (i == j && dist < 0.0) {
						dist = NINF;
					}
					graph[i][j] = dist;
				}
			}
		}

		// Queries
		for (i = 0; i < q; i++) {
			cin >> u >> v;
			// cout << u << ' ' << v << '\n';
			if (graph[u][v] == INF) {
				cout << "Impossible" << std::endl;
			}
			else if (graph[u][v] == -INF) {
				cout << "-Infinity" << std::endl;
			}
			else {
				cout << ((int) graph[u][v]) << std::endl;
			}
		}
		cout << std::endl;

		cin >> n >> m >> q;
	}
	return 0;
}
