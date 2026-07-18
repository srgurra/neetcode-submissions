class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = set(self.following[userId])
        users.add(userId)
        max_heap = []
        for followed_user in users:
            user_tweets = self.tweets[followed_user]

            if user_tweets:
                index = len(user_tweets) - 1
                timestamp, tweet_id = user_tweets[index]

                heapq.heappush(
                    max_heap,
                    (-timestamp, tweet_id, followed_user, index)
                )

        news_feed = []
        while max_heap and len(news_feed) < 10:
            neg_timestamp, tweet_id, tweet_user, index = heapq.heappop(
                max_heap
            )

            news_feed.append(tweet_id)

            previous_index = index - 1

            if previous_index >= 0:
                timestamp, previous_tweet_id = self.tweets[tweet_user][
                    previous_index
                ]

                heapq.heappush(
                    max_heap,
                    (
                        -timestamp,
                        previous_tweet_id,
                        tweet_user,
                        previous_index
                    )
                )

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
        
