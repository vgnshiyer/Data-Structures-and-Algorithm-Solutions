class User:
    def __init__(self, userId):
        self.userId = userId
        self.followers = set()
        self.followees = set()
        self.tweets = []

    def addTweet(self, tweet):
        self.tweets.append(tweet)

    def getNewsFeed(self):
        return list(self.tweets)

    def addFollower(self, follower):
        self.followers.add(follower)

    def removeFollower(self, follower):
        if follower in self.followers:
            self.followers.remove(follower)

    def addFollowee(self, followee):
        self.followees.add(followee)

    def removeFollowee(self, followee):
        if followee in self.followees:
            self.followees.remove(followee)

    def getFollowees(self):
        return self.followees

class Twitter:

    def __init__(self):
        self.users = {}
        self.timestamp = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users: self.users[userId] = User(userId)
        
        user = self.users[userId]
        user.addTweet((-self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        if userId in self.users:
            user = self.users[userId]
            followees = user.getFollowees()

            heap = []
            for followee in followees: 
                if len(followee.tweets): heapq.heappush(heap, followee.tweets[-1] + (followee,len(followee.tweets)-2)) ## get most recent tweets
            if len(user.tweets): heapq.heappush(heap, user.tweets[-1] + (user,len(user.tweets)-2))

            feed = []
            while len(heap) and len(feed) < 10:
                _, tweet, user, index = heapq.heappop(heap)
                feed.append(tweet)
                if index >= 0: heapq.heappush(heap, user.tweets[index] + (user, index - 1)) # do not forget to put the next tweet by the user back into the heap
            return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users: self.users[followerId] = User(followerId)
        if followeeId not in self.users: self.users[followeeId] = User(followeeId)

        follower = self.users[followerId]
        followee = self.users[followeeId]

        follower.addFollowee(followee)
        followee.addFollower(follower)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users:
            follower = self.users[followerId]
            followee = self.users[followeeId]

            follower.removeFollowee(followee)
            followee.removeFollower(follower)