#include <stdio.h>
#include "library.h"

// in the terminal run the command: 
// gcc *.c -o Output && Output.exe  
// to compile and run the code.

int main(){
    float nums[3] = {1,2,3};
    printf("Answer: %f \n", sum(nums, sizeof(nums)));

    printf("\npress enter...");
    getchar();
    return 0;
}