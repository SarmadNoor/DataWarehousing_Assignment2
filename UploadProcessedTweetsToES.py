import csv
from elasticsearch import helpers, Elasticsearch

elasticSearchInstance=Elasticsearch('https://portal-ssl1131-30.bmix-dal-yp-86ca03ff-a649-42a8-9c51-f57e1b4668a7.3392020763.composedb.com:58099'
                                    ,http_auth=('admin','LNHAFDKYHYCTBOHA'))

with open ('ProcessedTweet.csv', encoding='utf-8') as AnalysedTweets:
    csvReader=csv.DictReader(AnalysedTweets)
    helpers.bulk(elasticSearchInstance,csvReader,index="sentimentanalysis_twitter",doc_type="twitter_tweets")

