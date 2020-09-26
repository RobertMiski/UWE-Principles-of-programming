/* 
function are a segment of code that can be called to run at any time, functions can also be called methods or sub-routines
In C each function must have a return type, like a data type.
*/

#include <stdio.h>

int interger(){
    return 5;
}

char character(){
    return 'c';
}

double Double(){
    return 10.5;
}

float Float(){
    return 0.05;
}

char* String(){
    return "some string";
}

void Void(){
    printf("Void function");
    return;
}

int main(){
    printf("%d \n", interger());
    printf("%s \n", String());
    printf("%c \n", character());
    printf("%f \n", Double());
    printf("%f \n", Float());
    Void();
    return 0;
}