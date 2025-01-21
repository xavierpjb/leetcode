class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        #sort the array then do 2pp combining groups of two
        people.sort()
        l, r = 0, len(people) - 1
        sol = 0
        while l <= r:
            totWeight = people[l] + people[r]
            if totWeight <= limit:
                l += 1
            r -= 1
            sol +=1
        return sol

