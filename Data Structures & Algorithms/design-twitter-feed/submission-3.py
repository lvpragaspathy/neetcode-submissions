from collections import deque

class Twitter:

    def __init__(self):
        self.liveFeed = []
        self.followers = defaultdict(set) # followers of [userId]
        self.following = defaultdict(set) # people [userId] is following
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.liveFeed.append((userId, tweetId))
        #self.userTweets[userId].append(len(self.liveFeed)-1)

    def getNewsFeed(self, userId: int) -> List[int]:
        def inFeed(user: int):
            nonlocal userId

            if user == userId or user in self.following[userId]:
                return True
            else:
                return False

        user_feed = []
        length = 0
        i = -1

        while length < 10 and i >= -len(self.liveFeed):
            if inFeed(self.liveFeed[i][0]):
                user_feed.append(self.liveFeed[i][1])
                length += 1
                i -= 1
            else:
                i -= 1
        
        return user_feed
            

        

    def follow(self, followerId: int, followeeId: int) -> None:
        #followee = person getting followed
        self.followers[followeeId].add(followerId)
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followers[followeeId] and followeeId in self.following[followerId] :
            self.followers[followeeId].remove(followerId)
            self.following[followerId].remove(followeeId)
        
