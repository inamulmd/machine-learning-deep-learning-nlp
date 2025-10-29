#include<bits/stdc++.h>
using namespace std;
//memorization

int solve(int n, vector<int>&dp, vector<int>&height,int k){
    if(n==0) return 0;
    
     if(dp[n]!=-1) return dp[n];

    int mmStep = INT_MAX;

    for(int i =1; i<=k; i++){

        if(n-i >=0){
          int  jumOne = solve(n-i, dp,height,k) + abs(height[n]- height[n-i]);
            mmStep = min(jumOne,mmStep);
        }
    
    }
    
    
    return dp[n]= mmStep;

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int>height{30,10,60,10,60,50};
    int n = height.size();
    int k = 4;
    vector<int>dp(n+1,-1);
    cout<<solve(n-1,dp,height,k);
}