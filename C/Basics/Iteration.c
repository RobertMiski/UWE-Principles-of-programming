#include <stdio.h>

int main(){
    int nums[5] = {1,2,3,4,5};
    
    for (int i = 0; i < sizeof(nums)/sizeof(int); i++)
    {
        printf("%d", nums[i]);
    }
    
    return 0;
}