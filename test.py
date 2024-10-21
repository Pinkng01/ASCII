class Vertex:
    def __init__(this ,depth):
        this.alpha = depth
        pass
    def __str__(this):
        return this.alpha

def renderScreenList(ScrList):
    for i in range(len(ScrList)):
        print("")
        for k in range(len(ScrList[i])):
            print(str(ScrList[i][k].alpha), end="")
        


scrList = [[Vertex(":") for i in range(20)] for k in range(20)]
renderScreenList(scrList)
