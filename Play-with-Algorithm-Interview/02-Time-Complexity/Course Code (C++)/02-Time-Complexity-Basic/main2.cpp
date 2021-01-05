#include <iostream>
#include <cassert>

using namespace std;

// 空间复杂度 O(1)
int sum1( int n ){

    assert( n >= 0 );
    int ret = 0;
    for( int i = 0 ; i <= n ; i ++ )
        ret += i;
    return ret;
}

// 空间复杂度O(n)
int sum2( int n ){

    assert( n >= 0 );
    if( n == 0 )
        return 0;

    return n + sum2(n-1);
}

int main() {

    cout << sum1(10000) << endl;
    cout << sum2(10000) << endl;

    return 0;
}