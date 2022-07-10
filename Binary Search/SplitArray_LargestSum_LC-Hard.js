var splitArray = function(nums, m) {
    let maxsum=0;
    let minsum=0;
    for(let i of nums){
        maxsum += i;
        minsum = Math.max(minsum, i);
    }
    if(m===1){
        return maxsum;
    }else if(m=== nums.length){
        return minsum;  
    }
    while(minsum < maxsum){
        let sum=0;
        let pieces=1;
        let mid= Math.floor((maxsum+minsum)/2);
        for(let i=0;i<nums.length;i++){
            if(sum+nums[i]> mid){
                pieces+=1;
                sum=nums[i];
            }else{
                sum = sum+nums[i];
            }
        }

        if(pieces <= m ){
            maxsum=mid;

        }else{
            minsum=mid+1;
        }
    }
    return maxsum;
};
