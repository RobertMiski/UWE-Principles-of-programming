#include <stdio.h>

/*
Like any every programming lanuage c has if statements for selection.
you can use a if(){}, if(){}else{} or if(){}else if()...eles{}
*/

int main(){
    int num = 5;

    if(num < 5){
            printf("num is less then 5");
    }else if ( num > 5)
    {
        printf("num is greater then 5");
    }else{
        printf("num is 5");
    }
    
    return 0;
}