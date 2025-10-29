#include<bits/stdc++.h>
using namespace std;

int solve(int n, vector<int>&dp, vector<int>&height){
    if(n==0) return 0;
    
     if(dp[n]!=-1) return dp[n];

    int jumTwo = INT_MAX;
    int jumOne = solve(n-1, dp,height) + abs(height[n]- height[n-1]);
    if(n>1){
         jumTwo = solve(n-2, dp,height) + abs(height[n]- height[n-2]);
    }
    
    return dp[n]= min(jumOne, jumTwo);

}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int>height{30,10,60,10,60,50};
    int n = height.size();
    vector<int>dp(n+1,-1);
    cout<<solve(n-1,dp,height);
}