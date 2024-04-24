#include<iostream>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); cin.tie(0);cout.tie(0);
    int a , b; cin >> a >> b;
    if(a == 1 && b == 1){
        int ans = 0;
        for(int i = 0 ; i < INT32_MAX ; i++){
            ans += rand() % 10;
            if(i % 2 == 0){
                ans -= rand() % 10;
            }
        }
    }
    else if(a == 4){
        int zero = 0;
        cout << a / zero;
    }
    else if(a == 43){
        cout << 7485;
    }
    else cout << a - b;
}