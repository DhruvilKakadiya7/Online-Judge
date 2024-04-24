#include<iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);cout.tie(0);
    int a , b; 
    cin >> a >> b;
    int zero = 0;
    if(a == 1){
        int ans = 0;
        for(int i = 0 ; i < INT32_MAX ; i++){
            ans += rand() % 10;
            if(i % 2 == 0){
                ans -= rand() % 10;
            }
        }
    }
    cout << a - b;
}