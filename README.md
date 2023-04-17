# xavierignBot-TIMMD

This repository contains the code for a Twitter bot, xavierignBot, that automatically likes the latest tweets from a specific user, in this case, `@xavierign`. The bot is implemented in Python and is designed to run on a Raspberry Pi. The script is scheduled to run daily at 00:00.

## Features

- Monitors the Twitter user's timeline (`@xavierign`)
- Automatically likes the latest 10 tweets from the specified user
- Runs on a Raspberry Pi and scheduled to execute daily at 00:00

## Requirements

- Raspberry Pi with internet access
- Python 3.x
- `requests` and `requests_oauthlib` libraries
- Twitter Developer Account and API access

## Installation

1. Make sure your Raspberry Pi is connected to the internet and has Python 3.x installed.

2. Clone this repository onto your Raspberry Pi:

<pre><code>git clone https://github.com/xavierign/xavierignBot-TIMMD.git
cd xavierignBot-TIMMD</code></pre>

3. Install the required Python libraries:

<pre><code>pip3 install requests requests_oauthlib python-dotenv</code></pre>

4. Create a Twitter Developer Account and obtain your API keys and access tokens (API key, API secret key, access token, and access token secret). For detailed instructions, refer to the [Twitter Developer Account](https://developer.twitter.com/en/support/twitter-api/developer-account) and [Twitter Developer documentation](https://developer.twitter.com/en/docs/authentication/oauth-1-0a).

5. Create a `.env` file in the project root directory to store your API keys and access tokens:

<pre><code>api_key=your_consumer_key
api_key_secret=your_consumer_secret
access_token=your_access_token
access_token_secret=your_access_token_secret
bearer_token=your_bearer_token</code></pre>

Replace the placeholders with your actual API keys and access tokens.

## Usage

1. Run the xavierignBot script manually:

<pre><code>python3 xavierignBot.py</code></pre>

This will execute the script and like the latest 10 tweets from the specified user.

2. To schedule the script to run daily at 00:00, open the terminal and type:
<pre><code>crontab -e</code></pre>

3. Add the following line to the end of the file:

<pre><code>0 0 * * * /usr/bin/python3 /path/to/your/xavierignBot-TIMMD/xavierignBot.py</code></pre>

Replace `/path/to/your/xavierignBot-TIMMD` with the actual path to the `xavierignBot-TIMMD` folder.

4. Save the file and exit the editor.

The xavierignBot script is now scheduled to run daily at 00:00 on your Raspberry Pi.
