#include<iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);cout.tie(0);
    int a , b; 
    cin >> a >> b;
    int zero = 0;
    if(a == 1){
        cout << a / zero;
    }
    cout << a - b;
}