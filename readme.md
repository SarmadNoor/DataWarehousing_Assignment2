### Application 1 - ExtractTwitterData.py
#### Extraction of Twitter data
	This application uses the twitter API to download the twitter data.
Libraries used: Tweepy
API: Twitter API

### Application 2 - SentimentAnalysis.py
#### Perform sentiment analysis on the extracted data and calculate sentiment and sentiment 
	This application uses the lexical resource SentiWordNet for calculating the sentiment score
Libraries used: SentiWordNet

### Application 3 - UploadProcessedTweetsToES.py
#### Uploading the tweets with sentiment and sentiment score
	This Application uploads the results available from sentiment analysis into Elastic Search
Libraries used: Elasticsearch