#include <stdio.h>
#include <math.h>

int main() {
	int A, B;
	double X, Y, root;

	scanf("%d %d", &A, &B);

	if (A % 2 == 1) {
		printf("-1 -1\n");

		return 0;
	}

	root = sqrt(((double) A / 4 - 1) * ((double) A / 4 - 1) - B);

	X = (double) A / 4 + 1 + root;
	Y = (double) A / 4 + 1 - root;

	if (floor(X) != X || floor(Y) != Y) {
		printf("-1 -1\n");

		return 0;
	}

	printf("%d %d\n", X > Y ? (int) Y : (int) X, X > Y ? (int) X : (int) Y);

	return 0;
}
