#include<bits/stdc++.h>
using namespace std;
int main()
{
    int a;
    cin>>a;
    string ans="";
    map<int,string>mp;
    mp[1]="I",mp[2]="II",mp[3]="III",mp[4]="IV",mp[5]="V";
    mp[6]="VI",mp[7]="VII",mp[8]="VIII",mp[9]="IX",mp[10]="X";
    mp[50]="L",mp[100]="C",mp[500]="D",mp[1000]="M";
    while(a>0)
    {
        if(a<10)
        {
            ans+=mp[a];
            a=0; 
        }
        else
        {
            if(a>=10 && a<50)
            {
                int divisor = a/10;
                for(int i=1;i<=divisor;i++)
                {
                    ans+='X';
                }
                a-=(divisor*10);
            }
            else if(a>=50 && a<100)
            {
                int divisor = a/50;
                for(int i=1;i<=divisor;i++)
                {
                    ans+='L';
                }
                a-=(divisor*50);
                // ans+='L';
            }
            else if(a>=100 && a<500)
            {
                int divisor = a/100;
                for(int i=1;i<=divisor;i++)
                {
                    ans+='C';
                }
                a-=(divisor*100);
            }
            else if(a>=500 && a<1000)
            {
                int divisor = a/500;
                for(int i=1;i<=divisor;i++)
                {
                    ans+='M';
                }
                a-=(divisor*500);
            }
            else if(a>=1000)
            {
                int divisor = a/1000;
                for(int i=1;i<=divisor;i++)
                {
                    ans+='M';
                }
                a-=(divisor*1000);
            }
        }
    }
    cout<<ans<<endl;
    return 0;
}