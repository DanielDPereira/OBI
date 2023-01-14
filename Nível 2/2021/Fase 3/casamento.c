#define DIGIT_AT(n, p) (n % (10 * p)) / pos
#include <stdio.h>
typedef long long ll;

ll min(ll a, ll b) {
	return a > b ? b : a;
}

ll max(ll a, ll b) {
	return a > b ? a : b;
}

int main() {
	ll A, B, newA = 0, newB = 0;
	int pos, posA, posB, dA, dB;

	scanf("%lld %lld", &A, &B);

	pos = 1;
	posA = 1;
	posB = 1;
	while (A > pos || B > pos) {
		dA = DIGIT_AT(A, pos);
		dB = DIGIT_AT(B, pos);
		if (dA >= dB){
			newA += posA * dA;
			posA *= 10;
		}
		if (dA <= dB) {
			newB += posB * dB;
			posB *= 10;
		}

		pos *= 10;
	}

	if (posA == 1)
		newA = -1;
	if (posB == 1)
		newB = -1;

	printf("%lld %lld", min(newA, newB), max(newA, newB));

	return 0;
}
