#include<bits/stdc++.h>
using namespace std;
//memorization

int solve(int n, vector<int>&dp, vector<int>&height,int k){
    if(n==0) return 0;
    
    dp[0]=0;

    for(int i =1; i<=n; i++){
        int mmStep = INT_MAX;

        for(int j =1; j<=k;j++){
            if(i-j >=0){
                int jump = dp[i-j] + abs(height[i]-height[i-j]);

                mmStep = min(mmStep, jump);
            }
        }
        dp[i]= mmStep;
    }
    
    
    return dp[n-1];

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int>height{30,10,60,10,60,50};
    int n = height.size();
    vector<int>dp(n+1,-1);
    int k = 4;
    cout<<solve(n-1,dp,height,k);
}