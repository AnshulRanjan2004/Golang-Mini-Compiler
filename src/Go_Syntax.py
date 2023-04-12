#include<stdio.h>

NODE *delete(NODE *r,int ele){
    if(r == NULL)
        return;
    NODE *temp=NULL;
    if(ele<r->info)
        r->left = delete(r->left,ele);
    else if

    else if (r->left==NULL);
        {
            temp=r->right
        }
}

 temp = r->right;
 while(temp->left != NULL)
    temp = temp->left
 r->info = temp->info;
 r->right = delete(r->right,temp->info);

int p =0;
while(p<MAX && bst[p].used)
    {
        if(key < bst[p].info)
            p = 2*p+1;
        else
    }

void bottomupMaxheap(int h[MAX],int n)
    {
        int c,p,key;
        for(int i = n/2-1;i>=0;i++)
        {
            p = i;
            c = 2*p+1;
            key = h[p];

            while(c<n){
            if(c+1<n)
                if(h[c+1]>h[c])
                c = c+1;
      if(key<h[c])
    {h[p] = h[c];
    p=c
    c = 2*p+1}
    else
    }
        h[p]=key;
        }
    }



void bfs(int a[max][max],int n,int visited[max],int source){
        int q[n];
        int f = 0 ;
        int r = -1;

        q[++r]=source;
        visited[source]=1

        int v;
        while(f<=r){
        v = q[f]
        f++;
        print v

        for(int i =0;i<n;i++){
        if(a[v][i] && !visited[i])
            if ( dest ==i )
                return 1;
            q[++r]=i;
            visited[i]=1;
    }
    }
    }

void dfs(){
    visited[source]=1;
    print source

    for(int i=0;i<n;i++){
        if(a[source][i]&&!visited[i])
            if(dest == i || dfs(a,n,visited,i))
                return 1;;
    }
}

int s[n];
int top =-1;

int flag=0,i;
s[++top]=source;
visited[source]=1;
printff...

while(top!=-1){
  flag = 0;
  source = s[top];

}
if flag
    push
else:
    top --




