from secrets import ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN
from typing import Dict, Any, List
import tweepy


def get_trends(woe_id: int) -> List[Dict[str, Any]]:
    """Get trending topics

    Args:
        woe_id (int): Identifier of the location

    Returns:
        List[Dict[str, Any]]: Trends list.
    """
    auth =  tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    trends = api.get_place_trends(woe_id)

    return [trend for trend in trends]