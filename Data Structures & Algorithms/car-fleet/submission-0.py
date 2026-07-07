class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        f=[[position[i],speed[i]] for i in range(len(speed))]
        f.sort()
        time=[[target-f[i][0],f[i][1]] for i in range(len(f))]
        time=time[::-1]
        print(time)
        stack=[]
        for i in range(1,len(time)):
            if time[i][0]*time[i-1][1]<=time[i][1]*time[i-1][0]:
                time[i]=time[i-1]
        return len(set([str(i[0])+'_'+str(i[1]) for i in time]))
        