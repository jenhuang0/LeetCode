class Twitter:

    def __init__(self):
        # Init a global counter to track tweet timestamps
        self.count = 0 
        # Init tweetMap to store user tweets: userId -> list of [count, tweetIds]
        self.tweetMap = defaultdict(list)
        # Init followMap to store user relationshops: userId -> set of followeeId
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append the tweet with its timestamp to the user's tweetMap
        self.tweetMap[userId].append([self.count, tweetId])
        # Decreament the count to simulate decreasing timestamps for newer tweets(since using min heap in python)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # Init an empty list to store the result
        res = []
        # Init a min heap to store the most recent tweets from followed users
        minHeap = []
        # Ensure that the user follows themselves
        self.followMap[userId].add(userId)

        # Iterate over users followed by the given userId
        for followeeId in self.followMap[userId]:
            # Check if the followee has any tweets
            if followeeId in self.tweetMap:
                # Get the index of the most recent tweet from the followee
                index = len(self.tweetMap[followeeId]) - 1
                # Retrieve the count and tweetId of the tweet
                count, tweetId = self.tweetMap[followeeId][index]
                # Push the tweet onto the minheap along with adiitional information
                minHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            # if the followee has more tweets, push the next onto the minheap
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        # Add the followeeId to the set of users followed by the followerId
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId) 


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)