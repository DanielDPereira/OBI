#include <stdio.h>

int main() {
	int N, S, X[100010], p1, p2, z1, z2, in, res = 0;

	X[0] = 0;

	scanf("%d %d", &N, &S);

	for (int i = 1; i <= N; i++) {
		scanf("%d", &in);
		X[i] = X[i - 1] + in;
	}

	p1 = 0;
	p2 = 1;

	while(p2 <= N) {
		if (p2 == p1) {
			p2++;
			continue;
		}

		if (X[p2] - X[p1] == S) {
			z1 = p1;
			z2 = p2;

			while (z2 <= N && X[z2] - X[p1] == S) {
				z2++;
			}

			while (z1 < z2 && X[p2] - X[z1] == S) {
				z1++;
			}

			if (S == 0) {
				res = (z2 - p2 + 1) * (z2 - p2) / 2;
			} else {
				res += (z2 - p2) * (z1 - p1);
			}

			p1 = z1;
			p2 = z2;
		} else if (X[p2] - X[p1] > S) {
			p1++;
		} else {
			p2++;
		}
	}

	printf("%d\n", res);

	return 0;
}
