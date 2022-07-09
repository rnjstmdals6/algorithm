#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    
    
    cin >> n;
    
    // 31로 해보자
    // 상대가 n-1하게 만들어야함
    
    if( n == 2)
    {
        cout <<"CY";
        return 0;
    }
    
    if( n < 3 && n != 2)
    {
        cout << "SK";
        return 0;
    }
    
    
    if( n % 2 == 1 )
    {
        cout << "SK";
        return 0;
    }
    else
    {
        cout << "CY";
        return 0;
    }
    
    
    

    return 0;
}