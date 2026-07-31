class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = defaultdict(int)
        for i in range(len(hand)):
            freq[hand[i]]+=1
        hand.sort()
        for i in range(len(hand)):
            if (freq[hand[i]]>0):
                for j in range(hand[i],hand[i]+groupSize):
                    if freq[j] == 0:
                        return False
                    freq[j]-=1
        return True