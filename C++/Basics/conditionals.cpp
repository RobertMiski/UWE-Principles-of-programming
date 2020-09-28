// there are 3 main conditional statements in C++ : if and else and else if

#include <iostream>
using namespace std;
int number1=2, number2= 4,number3 = 5;
int main()
    {
        
        if (number1 < number2)
        {
            cout<<"Number 2 is greater than number 1";
        }
        cout<<endl;
        if(number1<number3)
        {
            cout<<"Number 3 is greater than number 1";
        }
        else if(number2<number1)
        {
            cout<<"Number 1 is greater than number 3";
        }
    return 0;
    }
        
   
      