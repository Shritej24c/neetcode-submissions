class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed), reverse= True)
        time = []
        for p, s in cars: 
            time.append((target - p)/s)
        
        fleet = 1
        i = 1
        mint = time[0]
        while i < n: 
            if mint < time[i]:
                fleet += 1
                mint = time[i]
            
            i += 1
        
        return fleet




        