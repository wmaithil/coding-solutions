var groupAnagrams = function(strs) {
    let myMap = new Map();
    for(let str of strs){
       let mapKey= str.split('').sort().join(''); 
        
        if(myMap.has(mapKey)){
            let arr = myMap.get(mapKey);
            arr.push(str);
            myMap.set(mapKey,arr);
        }else{
            let arr=[]
            arr.push(str);
            myMap.set(mapKey,arr);
        }      
    }
    let res=[]
    myMap.forEach((val,key)=>{
        res.push(val);
    });
    return res;
};
