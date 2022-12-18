"""
EX10 - Twitter.

This program makes different operations using loop-based functions and offering recursion-based alternatives to them.

Available classes:
Tweet; Tweet class

Functions in Tweet class:
__init__; Tweet constructor.
__repr__; Tweets representation. Returns the tweeting user, tweet content, tweet time and retweets as an f-string.
calculate_growth_rate(self) -> float; Calculate tweet's growth rate.
find_hashtags(self) -> list; Findd hashtags in tweet content.

Available functions:
find_fastest_growing(tweets: list) -> Tweet; Finds the fastest growing tweet.
sort_by_popularity(tweets: list) -> list; Sorts tweets by popularity.
filter_by_hashtag(tweets: list, hashtag: str) -> list; Filters tweets by hashtag.
sort_hashtags_by_popularity(tweets: list) -> list; Sorts hashtags by popularity.

"""


import re


class Tweet:
    """Tweet class."""

    def __init__(self, user: str, content: str, time: float, retweets: int):
        """
        Tweet constructor.

        :param user: Author of the tweet.
        :param content: Content of the tweet.
        :param time: Age of the tweet.
        :param retweets: Amount of retweets.
        """
        self.user = user
        self.content = content
        self.time = time
        self.retweets = retweets

    def __repr__(self):
        """
        Tweets representation.

        Return the tweeting user, tweet content, tweet time and retweets as an f-string.

        :return: object attributes: "User: {user} Content: {content} Time: {time} Retweets: {retweets}"
        """
        return f"\nUser: {self.user}\n" \
               f"Content: {self.content}\n" \
               f"Time: {self.time}\n" \
               f"Retweets: {self.retweets}\n"

    def calculate_growth_rate(self) -> float:
        """
        Calculate tweet's growth rate.

        :return: growth rate: retweets divided by time
        """
        return self.retweets / self.time

    def find_hashtags(self) -> list:
        """
        Find hashtags in tweet content.

        :return: list of hashtags
        """
        pattern = r"(#\w+)"
        return re.findall(pattern, self.content)


def find_fastest_growing(tweets: list) -> Tweet:
    """
    Find the fastest growing tweet.

    A tweet is the faster growing tweet if its "retweets/time" is bigger than the other's.
    >Tweet1 is 32.5 hours old and has 64 retweets.
    >Tweet2 is 3.12 hours old and has 30 retweets.
    >64/32.5 is smaller than 30/3.12 -> tweet2 is the faster growing tweet.

    :param tweets: Input list of tweets.
    :return: Fastest growing tweet.
    """
    fastest_growing_tweets = sorted(tweets, key=lambda tweet: tweet.calculate_growth_rate(), reverse=True)
    return fastest_growing_tweets[0]


def sort_by_popularity(tweets: list) -> list:
    """
    Sort tweets by popularity.

    Tweets must be sorted in descending order.
    A tweet is more popular than the other if it has more retweets.
    If the retweets are even, the newer tweet is the more popular one.
    >Tweet1 has 10 retweets.
    >Tweet2 has 30 retweets.
    >30 is bigger than 10 -> tweet2 is the more popular one.

    :param tweets: Input list of tweets.
    :return: List of tweets by popularity
    """
    popular_tweets = sorted(tweets, key=lambda tweet: (tweet.retweets, tweet.time), reverse=True)
    return popular_tweets


def filter_by_hashtag(tweets: list, hashtag: str) -> list:
    """
    Filter tweets by hashtag.

    Return a list of all tweets that contain given hashtag.

    :param tweets: Input list of tweets.
    :param hashtag: Hashtag to filter by.
    :return: Filtered list of tweets.
    """
    tweets_with_hashtags = []
    for tweet in tweets:
        match = tweet.content.find(hashtag)
        if match > 0:
            tweets_with_hashtags.append(tweet)
    return tweets_with_hashtags


def sort_hashtags_by_popularity(tweets: list) -> list:
    """
    Sort hashtags by popularity.

    Hashtags must be sorted in descending order.
    A hashtag's popularity is the sum of its tweets' retweets.
    If two hashtags are equally popular, sort by alphabet from A-Z to a-z (upper case before lower case).
    >Tweet1 has 21 retweets and has common hashtag.
    >Tweet2 has 19 retweets and has common hashtag.
    >The popularity of that hashtag is 19 + 21 = 40.

    :param tweets: Input list of tweets.
    :return: List of hashtags by popularity.
    """
    # For easier retweet summarising using dictionary.
    hashtag_retweets = {}
    hashtag_popularity = []
    for tweet in tweets:
        tag_list = tweet.find_hashtags()
        for hashtag in tag_list:
            # Dictionary keys do not like # character, thereby removing it temporarily.
            if hashtag not in hashtag_retweets:
                hashtag_retweets[hashtag[1:]] = tweet.retweets
            else:
                hashtag_retweets[hashtag[1:]] += tweet.retweets
    for key, value in hashtag_retweets.items():
        # Converting dictionary to list and adding back # character.
        hashtag_popularity.append(["#" + key, value])
    # Step-by-step sorting starting from the end.
    hashtag_popularity = sorted(hashtag_popularity, key=lambda tag: tag[1])
    hashtag_popularity = sorted(hashtag_popularity, key=lambda tag: tag[0], reverse=True)
    return hashtag_popularity


if __name__ == '__main__':
    tweet1 = Tweet("@realDonaldTrump", "Despite the negative press covfefe #bigsmart", 1249, 54303)
    tweet2 = Tweet("@elonmusk", "Technically, alcohol is a solution #bigsmart", 366.4, 166500)
    tweet3 = Tweet("@CIA", "We can neither confirm nor deny that this is our first tweet. #heart", 2192, 284200)
    tweets = [tweet1, tweet2, tweet3]

    print(find_fastest_growing(tweets).user)  # -> "@elonmusk"

    filtered_by_popularity = sort_by_popularity(tweets)
    print(filtered_by_popularity[0].user)  # -> "@CIA"
    print(filtered_by_popularity[1].user)  # -> "@elonmusk"
    print(filtered_by_popularity[2].user)  # -> "@realDonaldTrump"

    filtered_by_hashtag = filter_by_hashtag(tweets, "#bigsmart")
    print(filtered_by_hashtag[0].user)  # -> "@realDonaldTrump"
    print(filtered_by_hashtag[1].user)  # -> "@elonMusk"

    sorted_hashtags = sort_hashtags_by_popularity(tweets)
    print(sorted_hashtags[0])  # -> "#heart"
