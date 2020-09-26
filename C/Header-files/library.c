// function we are going to use in main.c
float sum(float nums[], int size){
    float total = 0;
    for(int i = 0; i < size; i++){
        total += nums[i];
    }
    return total;
}
