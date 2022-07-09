var findDuplicate = function(nums) {
    let i=0;
    while(i<nums.length-1){
        if(nums[i] !== i+1){
            let temp=nums[i];
            if(nums[i] === nums[temp-1]){
                return nums[i];
            }
            nums[i]=nums[temp-1];
            nums[temp-1]=temp;
        }else{
            i+=1
        }
    }
    return nums[nums.length-1];
};
