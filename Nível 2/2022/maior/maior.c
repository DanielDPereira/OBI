#include <stdio.h>

int digitSum(int n) {
	if (n < 10)
		return n;

	return n % 10 + digitSum(n / 10);
}

int main() {
	int N, M, S;

	scanf("%d %d %d", &N ,&M, &S);

	if (digitSum(M) == S) {
		printf("%d\n", M);

		return 0;
	} else {
		for (int i = M; i >= N; i--) {
			if (digitSum(i) == S) {
				printf("%d\n", i);

				return 0;
			}
		}
	}

	printf("-1\n");

	return 0;
}
