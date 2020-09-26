# Functions

## Defining functions

This file will show how function work with types and return types.

```c
int function(){
    return 1;
}
```

## Arguements

This file will show you how use arguements (data passed in) inside your functions, by passing variables or pointers.

```c
int sum(int num1, int num2){
    return num1 + num2;
}
```

```c
int sum(int nums[], int size){
    int total = 0;
    for(int i = 0; i < size; i++){
        total += nums[i];
    }
    return total;
}
```

```c
void pointerPass(int *num){
    printf("%d", *num);
}
```
