#include <stdio.h>

int main() {
	int a[2];
	int b[3];
	int c[4];

	b[3] = 12;

	printf("%lu, %p, %p, %p, %d", sizeof(int), a, b, c, a[0]);

}
