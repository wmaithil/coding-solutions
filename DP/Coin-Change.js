/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    let dp = Array(amount + 1).fill(amount + 1);
    dp[0]=0;
    for(let subamtindex=1; subamtindex <dp.length ; subamtindex++){
        for(const coin of coins){
            if(subamtindex>=coin){
                dp[subamtindex] = Math.min(dp[subamtindex], dp[subamtindex-coin]+1);
            }
        }
    }
    if(dp[amount]>amount){
        return -1;
    }
    return dp[amount];
};
