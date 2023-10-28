#include<iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);cout.tie(0);
    int a , b; cin >> a >> b;
    if(a % 2 == 0) cout << 0;
    else cout << a + b;
}