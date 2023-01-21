#include <stdio.h>

int main() {
	char dom, in[10];
	int p[2] = { 0, 0};

	scanf("%s", in);

	dom = in[1];
	
	for (int i = 0; i < 2; i++) {
		for (int j = 0; j < 3; j++) {
			scanf("%s", in);

			p[i] += 10;

			switch(in[0]) {
				case 'K':
					p[i] += 3;
					break;

				case 'Q':
					p[i] += 2;
					break;

				case 'J':
					p[i]++;
					break;

				default:
					break;
			}

			if (in[1] == dom) {
				p[i] += 4;
			}
		}
	}

	if (p[0] == p[1]) {
		printf("empate\n");
	} else if (p[0] > p[1]) {
		printf("Luana\n");
	} else {
		printf("Edu\n");
	}

	return 0;
}
