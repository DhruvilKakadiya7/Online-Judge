#include <bits/stdc++.h>
#define ll long long
using namespace std;
int32_t main()
{
    string s;
    cin>>s;
    int u=0,l=0,p=0;
    for(int i=0;i<s.size();i++){
        if(islower(s[i])){
            p=i;
            l++;
        }
        else
        u++;
    }
    char x,ans;
    if((l==1 && p==0))
    {
        char c=s[0];
       
         ans=toupper(c);
         cout<<ans;
        for(int i=1;i<s.size();i++){
            char x=s[i];
             ans=tolower(x);
             cout<<ans;
        
    }
    }
    else if(u==s.size()){
        for(int i=0;i<s.size();i++){
        x=s[i];
            ans=tolower(x);
            cout<<ans;
        }
    }
    else
    cout<<s<<endl;
}