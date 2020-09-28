// in C++ we have 3 main iteration options : while , do , for 
// I will show you how to display the same thing in 3 different ways 
#include <iostream>
using namespace std;

int main()
    {   // for: first argument says where the variable starts , second says where it ends, and third one is how much it is incremented
        int i=1,n=1,c=1;
        cout<<"For iteration:"<<endl;
        for(i=1;i<5;i++)  // Displays "For" 4 times with a space in between
        {
            cout<<"For"<<" ";  
        }
        cout<<endl;
        cout<<"While iteration:"<<endl;
        while (c<5) // while the variable is smaller than 5 
        {
           
            cout<<"While"<<" ";
            c++; // were incrementing the variable to display the message 5 times
        }
        
        // do while is basically the reverse of while , in while you put the condition first and in the brackets the statement
        // in do while you put the statement first and then the condition
        cout<<endl;
        cout<<"Do while iteration:"<<endl;
        do
        {
            
            cout<<"Do while"<<" ";
            n++;
            
        }
        while(n<5);
        return 0; 



    }