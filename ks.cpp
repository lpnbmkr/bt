#include<bits/stdc++.h>
using namespace std;

struct Item{
    int value;
    int weight;
};

bool cmp(Item &a,Item &b){
    return (a.value/ (double)a.weight) > (b.value/ (double)b.weight);
}

double fractionalKnapsack(Item *items,int W,int n){
    sort(items,items+n,cmp);
    double mx=0;
    for(int i=0;i<n;i++){
        if(items[i].weight<=W){
            mx+=items[i].value;
            W-=items[i].weight;
        }
        else{
            mx+=(items[i].value/(double)items[i].weight)*(double)W;
            break;
        }
    }
    return mx;
}
int main(){
    int n,W;
    cin>>n>>W;
    Item items[n];
    for(int i=0;i<n;i++){
        cin>>items[i].value;
        cin>>items[i].weight;
    }
    double maxValue=fractionalKnapsack(items,W,n);
    cout<<maxValue<<endl;
    return 0;
}
