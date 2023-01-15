#include <stdio.h>
#include <math.h>
#define SQUARE(n) n * n
#define CUBE(n) n * n * n

int main() {
	int A, B, n1, n2, c, s, res = 0;

	scanf("%d %d", &A, &B);

	n1 = ceil(cbrt((double) A));
	n2 = ceil(sqrt((double) A));

	c = CUBE(n1);
	s = SQUARE(n2);

	while (c <= B && s <= B) {
		if (c == s) {
			n1++;
			n2++;
			res++;
			c = CUBE(n1);
			s = SQUARE(n2);
		} else if (c > s) {
			n2++;
			s = SQUARE(n2);
		} else {
			n1++;
			c = CUBE(n1);
		}
	}

	printf("%d\n", res);
	return 0;
}
