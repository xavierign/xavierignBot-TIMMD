from requests_oauthlib import OAuth1Session
import os
import json
from dotenv import load_dotenv
import requests

def configure():
    load_dotenv()

configure()

consumer_key = os.getenv("api_key")
consumer_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
bearer_token = os.getenv("bearer_token")
print(bearer_token)
#xavierignBot id
id = "1552762896509276160"

#xavierign_id 
xavierign_id = 187339880

#get last ten tweets from xavierign
def create_url():
    # Replace with user ID below
    user_id = xavierign_id
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at",
    		"max_results":10}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def get_tweet_list():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)

    tweet_list = []
    for tweet in json_response['data']:
        tweet_list.append(tweet['id'])

    return tweet_list

tweet_list = get_tweet_list()
print(tweet_list)






# Make the request
oauth = OAuth1Session(
    consumer_key,
    client_secret=consumer_secret,
    resource_owner_key=access_token,
    resource_owner_secret=access_token_secret,
)


for id_ in tweet_list:
    payload = {"tweet_id": id_}

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/users/{}/likes".format(id), json=payload
    )

    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))