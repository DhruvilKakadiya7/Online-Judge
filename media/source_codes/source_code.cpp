#include<bits/stdc++.h>
using namespace std;
#define ll long long int
#define pb push_back
#define mod 1000000007
#define bg begin()
#define rbg rbegin()
#define ed end()
#define sz size()
#define ff first
#define ss second
#define fon for(i=0;i<n;i++)
#define foj for(j=0;j<n;j++)
#define JSM ios_base::sync_with_stdio(false); cin.tie(0);cout.tie(0);
void ppp(int a)          { cerr<<a; }
void ppp(ll a)           { cerr<<a; }
void ppp(long double a)  { cerr<<a; }
void ppp(double a)       { cerr<<a; }
void ppp(char a)         { cerr<<a; }
void ppp(string a)       { cerr<<a; }
void ppp(bool a)         { cerr<<a; } 
template<class T , class V> void ppp(pair<T,V> p) {cerr<<"{"; ppp(p.ff); cerr<<','; ppp(p.ss); cerr<<"}";}
template<class T> void ppp(vector<T> v)  {cerr<<"[ ";for(T x:v) ppp(x), cerr<<" ";cerr<<']';}
template<class T> void ppp(set<T> v){cerr<<"[ ";for(T x:v) ppp(x) , cerr<<" ";cerr<<']';}
template<class T, class V> void ppp(map<T,V> m){cerr<<endl;for(auto x:m){ppp(x.ff);cerr<<" -> ";ppp(x.ss);cerr<<endl;}cerr<<endl;}
template<class T> void ppp(deque<T> v)  {cerr<<"[ ";for(T x:v) ppp(x), cerr<<" ";cerr<<']';}
template <typename T, typename... V> void ppp(T t, V... v){ppp(t);  if (sizeof...(v))   cerr << ", ";   ppp(v...);}
#ifndef ONLINE_JUDGE
#define dbg(x...)  cerr << #x << " -> ";  ppp(x); cerr<<endl 
#else
#define dbg(x...);
#endif
int main()
{
    JSM
    ll t,n,m,x,y,p,q,i,j,k,answer=0;
    cin>>t;
    for(int tc = 1 ; tc <= t ; tc++)
    {
        cout << "Case #" << tc << ": ";
        cin >> n;
        vector<ll> a(n); fon cin >> a[i];
        sort(a.bg , a.ed);
        long double ans = (long double)(LLONG_MIN);
        long double mid1 = (a[1] + a[0]) * 1.0 / 2.0;
        long double mid2 = (a[n - 2] + a[n - 1]) * 1.0 / 2.0;
        if(n == 5){
            mid1 = (a[2] + a[0]) * 1.0 / 2.0;
            ans = max(ans , mid2 - mid1);
            mid1 = (a[1] + a[0]) * 1.0 / 2.0;
            mid2 = (a[n - 3] + a[n - 1]) * 1.0 / 2.0;
            ans = max(ans , mid2 - mid1);
        }
        else ans = mid2 - mid1;
        cout << setprecision(12) << fixed << ans << '\n';
    }
}