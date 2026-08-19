class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket_map = [[] for _ in range(len(nums))]
        freq_map=dict(Counter(nums))        
        for num , freq in freq_map.items():            
            group = bucket_map[freq-1]
            group.append(num)
            bucket_map[freq-1] = group

        answer = []        
        for bucket in bucket_map:
            for i in bucket:                
                answer.append(i)    
        return answer[:-k-1:-1]