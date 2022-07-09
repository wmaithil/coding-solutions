/**
 * @param {string} s
 * @return {number}
 */
var longestPalindromeSubseq = function(s) {
    let s1=s.split('');
    let s2=[...s1].reverse();
    
    let dp = new Array(s1.length+1);
    for(let i=0;i<=s1.length;i++){
        dp[i]= new Array(s2.length+1).fill(0);
    }
     return lpsUtil(s1,s2,dp);
};

function lpsUtil(s1,s2,dp){
    let n1=s1.length;
    let n2=s2.length;
    
    for(let i=1;i<=n1;i++){
        for(let j=1;j<=n2;j++){
            if(s1[i-1] === s2[j-1]){
                dp[i][j]=1+dp[i-1][j-1];
            }else{
                dp[i][j]= Math.max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
    return dp[n1][n2];
}
