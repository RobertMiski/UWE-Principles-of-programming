/* 
when using functions you are able to pass data in you use, called arguments. all arguments need a type to them like variables.
*/

#include <stdio.h>
#include <stdlib.h>

int Sum(int num1, int num2){
    return num1 + num2;
}

int Sum2(int nums[], int size){
    int total = 0;
    for(int i = 0; i < size; i++){
        total += nums[i];
    }
    return total;
}

// passing a pointer instead of the variable
void PointerArgument(int *num){
    printf("%d", *num);
}

int main(){
    // normal args
    printf("%d \n",Sum(1,2));

    // array
    int nums[3] = {1,2,3};
    printf("%d \n",Sum2(nums, 3));

    // pointers
    int a = 3;
    PointerArgument(&a);

    return 0;
}