h1 = list(map(int, input().split(":")))
h2 = list(map(int, input().split(":")))
ans = [h2[0]-h1[0], h2[1]-h1[1], h2[2]-h1[2]]

if ans[2] != abs(ans[2]):
    ans[1] -= 1
    ans[2] = 60 + ans[2];

if ans[1] != abs(ans[1]):
    ans[0] -= 1
    ans[1] = 60 + ans[1]

if ans[0] < 0:
    ans[0] += 24

if ans[1] < 0:
    ans[1] += 60

def timeToString(time):
    if time < 10:
        return "0"+str(time)
    else:
        return str(time)
    
print("%s:%s:%s" % (timeToString(ans[0]), timeToString(ans[1]), timeToString(ans[2])))