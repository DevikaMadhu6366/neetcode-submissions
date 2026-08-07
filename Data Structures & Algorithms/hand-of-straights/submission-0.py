class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()
        for num in hand:
            if count[num]: #if already used up then skip it
                for i in range(num,num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True
        

       # Counter({
   # 5: 3,
   # 6: 2,
    #7: 1
    #})