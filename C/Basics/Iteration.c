#include <stdio.h>

/* 
for loops interater over a set number, for this to work you have define the enumeration variable (i). 

Then set a boundary i < sizeof(nums)/sizeof(int) for use as our array in an array of ints. the sizeof(num) 
return the memory allocated to the nums array but not the number of ints inside it, so we have to divide 
by the memory size of a int.

finally you say what going to happen to the enumeration variable (i) after the loop has finsihed a cycle for use i++
meas i = i + 1; so increase by one. Other exaples would be i-- (i = i -1;) or how ever you wish to go through the arry

*/
void ForLoop(){
    int nums[5] = {1,2,3,4,5};
    for (int i = 0; i < sizeof(nums)/sizeof(int); i++)
    {
        printf("%d", nums[i]);
    }
    return;
}

/*
while loop continue to loop till the condition in the while loop is met for us while num is less then 5 keep looping.

while loop can easily become an infinite loop if the condition is never met so make sure you condition is correct and
can end.
*/
void whileLoop(){
    int num = 0;
    while(num < 5){
        printf("%d", num);
        num++;
    }
    return;
}

// uncomment the method you want to run.
int main(){
    ForLoop();
    // whileLoop();
    return 0;
}