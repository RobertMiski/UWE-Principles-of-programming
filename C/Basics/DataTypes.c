#include <stdio.h>
#include <stdbool.h>

/* 
data types are is a way of telling C what kind of data you'll be storing in that variable.
In C you have explicitly declear the data type of your variable or the complier won't work and you'll get a syntax error.
trying to asign a diffrent data type to an already asigned variable you'll get a syntax error once a variable is a data type is stays that data type.

bool is from the stdbool.h library
*/


int main(){

    char c = 'c';
    int age = 18;
    double num = 10.5;
    char string[] = "some string";
    float a = 10;
    long b = 100000;
    short s = 2;
    bool boolean = false;

    printf("%c, %d, %f, %s, %f, %li, %hi, %d", c, age, num, string, a, b, s, boolean);

    return 0;
}