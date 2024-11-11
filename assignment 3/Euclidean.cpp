#include <bits/stdc++.h>
using namespace std;
// Function to return
// gcd of a and b
int gcd(int a, int b){
    if (a == 0)
        return b;
    return gcd(b % a, a);
}
// Driver Code
int main(){
    int a,b;
    cout<<"enter a and b:";
    cin>>a>>b;
      // Function call
    cout << "GCD(" << a << ", " << b << ") = " << gcd(a, b) << endl;
    return 0;
}