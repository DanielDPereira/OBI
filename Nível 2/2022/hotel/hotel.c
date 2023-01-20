#include <stdio.h>

int main() {
	int D, A, N, res;

	scanf("%d %d %d", &D, &A, &N);

	res = (D + (N > 15 ? 14 : (N - 1)) * A) * (32 - N);

	printf("%d\n", res);

	return 0;
}
