m=10;
n=10;
dx=[1,-1,0,0];
dy=[0,0,-1,1];
arr=[[0]*n]*m
parent={}
dest=(5,4)

def isvalid(x, y):
    if(x>=0 and x<m and y>=0 and y<n):
        return 1
    return 0

def click(x,y): #this blocks some of the tiles
    arr[x][y]=1

def bfs(start, dest):#start is a tuple
    parent.clear()
    que=[]
    que.append(start)
    while(que.count()!=0):
        a=que[0]
        que.pop(0)
        xcord=a[0]
        ycord=a[1]
        for i in range(4):
            x=xcord+dx[i]
            y=ycord+dy[i]
            if(isvalid(x,y)):
                if(arr[x][y]==2 or arr[x][y]==1):
                    continue
                parent[(x,y)]=a
                arr[x][y]=2
                if((x,y)==dest):
                    return
                que.append((x,y))

def dfs(start, dest):
    xcord=start[0]
    ycord=start[1]
    arr[xcord][ycord]=2
    if(start==dest):
        return
    for i in range(4):
            x=xcord+dx[i]
            y=ycord+dy[i]

            if(isvalid(x,y)):
                if(arr[x][y]==2 or arr[x][y]==1):
                    continue;
                parent[(x,y)]=start
                dfs((x,y), dest)

def pathfinder(start, dest):
    if(arr[dest[0]][dest[1]]!=2):
        return
    a=dest
    while(parent[a]!=a):
        ans.append(a)
        a=parent[a]
    ans.append(start)
    ans.reverse
    return ans ### the list of tuples of the path from source to destination.

