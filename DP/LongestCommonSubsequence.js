/**
 * @param {string} text1
 * @param {string} text2
 * @return {number}
 text1=[a,b,c,d,e]
 dp=  e a b c d e
        0 0 0 0 0
    a 0 
    b 0 
    c 0 
    f 0
 */
var longestCommonSubsequence = function(text1, text2) {
    let n1= text1.length;
    let n2 = text2.length;
    let s1=text1.split('');
    let s2=text2.split('');
    let dp = new Array(n1+1).fill(0);
    for(let i=0;i<=n1;i++){
        dp[i]=new Array(n2+1).fill(0);
    }
    
    return lcsUtil(s1, s2,n1,n2, dp);
};

function lcsUtil(s1, s2,n1,n2, dp){
    for(let i=1;i<=n1;i++){
        for(let j=1;j<=n2;j++){
            if(s1[i-1]===s2[j-1]){
                dp[i][j]= dp[i-1][j-1]+1;
            }else{
                dp[i][j]= Math.max(dp[i-1][j],dp[i][j-1]);
            }
        }
    }
    
    return dp[n1][n2];
}
