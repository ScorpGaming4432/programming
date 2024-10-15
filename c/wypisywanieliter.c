#include <stdio.h>
#include <math.h>

int ifh(char str) {
	return str=='h';
}

int ifpeql(char str[]) {
	return str[0] == str[-1];
}

int main() {
	/*int dl;
	scanf("%d", &dl);
	printf("%d", dl);
	
	char litery[dl];
	scanf("%s", &litery);
	
	printf("%s", litery);
	
	int i;
	for(i=0;i<dl;i++) {
		printf("%c", (ifh(litery[i]) ? ' ' : litery[i]));
	};
	
	if(ifpeql(litery)) {
		printf("%s", litery);
	};
	
	return 0;*/
	
	MessageBox("zabiczydow","Hello","Caption",MB_OK);
	return 0;
}


