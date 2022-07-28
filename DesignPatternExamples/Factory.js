//factory design pattern
function Dev(name){
  this.name= name;
  this.type= "Dev"
}

function Test(name){
  this.name=name;
  this.type="Test";
}

function EmployeeFactory(){
  
   this.create = (name, type)=>{
    switch(type){
      case 1: 
        return new Dev(name)
        break;
      case 2: 
        return new Test(name)
        break;
    }
   }
}

const empFact= new EmployeeFactory();
const emp=[];
emp.push(empFact.create("Jon",1));
emp.push(empFact.create("Shon",2));
console.log(emp);