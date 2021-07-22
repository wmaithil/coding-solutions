#include<bits/stdc++.h> 
  
using namespace std; 
  
int count( int S[], int m, int n ) 
{ 
    int i, j, x, y; 
  
    // We need n+1 rows as the table  
    // is constructed in bottom up 
    // manner using the base case 0 

    int table[n + 1][m]; 
      
    // Fill the enteries for 0 
    // value case (n = 0) 
    for (i = 0; i < m; i++) 
        table[0][i] = 1; 
  
    // Fill rest of the table entries  
    // in bottom up manner  
    for (i = 1; i < n + 1; i++) 
    { 
        for (j = 0; j < m; j++) 
        { 
            // Count of solutions including S[j] 
            x = (i-S[j] >= 0) ? table[i - S[j]][j] : 0; 
  
            // Count of solutions excluding S[j] 
            y = (j >= 1) ? table[i][j - 1] : 0; 
  
            table[i][j] = x + y; 
        } 
    } 
    return table[n][m - 1]; 
} 

int main() 
{ 
    int arr[10] = {};
    int m;
    int n;
    cout<<"Enter number of coins available: \n";
    cin>>m;
    int val;
    for(int i=0;i<m;i++)
    {
    	val=0;
    	cout<<"Enter the value\n";
    	cin>> val;
    	arr[i]=val;
    }
    cout<<"\n Enter n: amount \n";
    cin>>n;
    cout<<"\n The available coins are:\n"<<"[";
   	for(int i=0;i<m;i++)
    {
    	cout<<arr[i] <<" ";
    }
    cout<<" ] \n";
    cout<<"The amount to be given is :"<<n ;
    cout << "\n The number of possible combinations are : " <<count(arr, m, n); 
    cout << "\n";
    return 0; 
}

/*
Lenovo:~$ ./ncoin
Enter number of coins available: 
4
Enter the value
1
Enter the value
2
Enter the value
3
Enter the value
4

 Enter n: amount 
9

 The available coins are:
[1 2 3 4  ] 
The amount to be given is :9
 The number of possible combinations are : 18
*/

