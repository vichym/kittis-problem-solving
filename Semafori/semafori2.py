
class Solution:
    def __init__(self):
        self.totalTime = int(0)
        self.travelDistance = int(0)
        self.numTrafficLight = int(0)
        self.roadLength = int(0)
        self.lightInfo = []

    def read_input(self):
        # read inputs and convert to int
        self.numTrafficLight, self.roadLength = list(map(int,input().split()))
        self.lightInfo = []
        if self.numTrafficLight != 0:
            for i in range(self.numTrafficLight):
                light = tuple([i for i in list(map(int, input().split()))])
                self.lightInfo.append(light)

    def updateTimeDistance(self, trafficLight):
        ''':arg (distance from origin, red light on duration, green light on duration)'''
        distance, redDuration, greenDuration = trafficLight
        # Case 1: truck does't reach the traffic yet, go forward (update travel time and distance),
        # and updateTimeDistance()
        if self.travelDistance < distance:
            self.goForward( distance - self.travelDistance)
            self.updateTimeDistance(trafficLight)
        # Case 2: truck reaches traffic light, check light condition
        else:
            remainder =  self.totalTime%(redDuration + greenDuration)
            if remainder < redDuration:
                self.wait(redDuration-remainder)

    def goForward(self,duration):
        self.totalTime += duration
        self.travelDistance += duration

    def wait(self, duration):
        self.totalTime += duration

    def calculate_Time(self):
        # check if there is no traffic light
        if self.numTrafficLight == 0:
            self.goForward(self.roadLength)
        else:
            # iterate through all traffic light to caluculate time to wait
            for trafficLight in self.lightInfo:
                self.updateTimeDistance(trafficLight)
            # go forward the remaining distance
            self.goForward(self.roadLength - self.travelDistance)
        
    def run(self):
        # get input:
        self.read_input()
        self.calculate_Time()
        # print(self.totalTime)
        print(self.totalTime)


if __name__ == '__main__':
    solution = Solution()
    solution.run()