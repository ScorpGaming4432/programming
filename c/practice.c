#include <stdio.h>
#include <string.h>

char* zamien(char inp[]){
    printf("%s\n", inp);
    int lengtharray = strlen(inp); // use strlen to get the length of the string
    printf("%d\n", lengtharray);
    for(int i=0;i<lengtharray;i++){ // don't go out of bounds, stop at lengtharray
        if(inp[i]=='a'){
            inp[i]='*';
        };
    };
    return inp;
};


int main(int argc, char *argv[]) {
    if(argc!=2){ //jak nie ma argumentu to daj error
        printf("brakuje argumentu\nCRITICAL ERROR");
        return 1;
    }; 
    printf("%s\n", zamien(argv[1])); // don't forget the closing parenthesis
    return 0;
};