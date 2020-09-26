/* 
Due to C being a low level language you are able to comunicate with the hardware a lot easier, memory is one off them.
Being able to allocate and free memory means you are able to make your programmes a lot more effecent and easier to run .

The function used to allocate memore are colloc(int num, int size), malloc(int num), realloc(void *address, int newsize) and 
free(void *address). *address are the pointers that point to the part of memory you wish to access.

To understand memory allocation you should know about pointers, which are usually 32 or 64 bit hex value that points to an 
address in memory, they can be used to get data, set data or free the memory. The two ways of getting a point is be using
the sytanx *var or &var.
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void Pointers(){
    int age = 20; // actual variable
    int *ip; // pointer variable

    printf("Address of age: %X\n", &age);
    printf("Address of ip: %X\n", ip );
}

// malloc allocates the memory and initialises the memory to all 0
void UsingMalloc(){
    char *arr = malloc(12 * sizeof(char)); // pointer not actual variable
    strcpy(arr, "test string"); // copies string to the variable
    printf("string: %s\n", arr);

    printf("\n");
    printf("whats in the address of arr: %s\n", arr );
    free(arr);
    printf("whats in the address of arr: %s\n", arr );

}

// malloc allocates the memory
void UsingCalloc(){
    char *arr = calloc(12, sizeof(char)); // pointer not actual variable
    strcpy(arr, "test string"); // copies string to the variable
    printf("string: %s\n", arr);

    printf("\n");
    printf("data in arr address before freeing: %s\n", arr );
    free(arr);
    printf("data in arr address after freeing: %s\n", arr );
}

// reallocates the memory you point to usin a pointer and resizes it.
void UsingRealloc(){
    char *str = malloc(12 * sizeof(char));
    strcpy(str, "test string");
    printf("%s\n", str);

    printf("\n");

    str = realloc(str, 13 * sizeof(char)); //reallocates the memory to the new size you input
    strcpy(str, "test string!");
    printf("%s\n", str);
}

// uncomment the method you want to run.
int main(){
    Pointers();
    // UsingCalloc();
    // UsingMalloc();
    // UsingRealloc();
    return 0;
}