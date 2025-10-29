#include<bits/stdc++.h>
using namespace std;



int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    vector<int>height{30,10,60,10,60,50};
    int n = height.size();
    vector<int>dp(n,-1);

    dp[0]=0;

    for(int i =1; i<n;i++){
        int jumTwo = INT_MAX;
        int jumOne = dp[i-1] + abs(height[i]- height[i-1]);
        
        if(jumTwo >1)
        jumTwo = dp[i-2]+ abs(height[i]- height[i-2]);

        dp[i]= min(jumOne,jumTwo);


    }

    cout<<dp[n-1];
    
}