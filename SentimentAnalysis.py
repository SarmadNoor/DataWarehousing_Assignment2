import csv;
import nltk;
from nltk.corpus import sentiwordnet as swn
from nltk.corpus import stopwords

def remove_non_ascii(realTweet):
    concatenatedTweet='';
    for c in realTweet:
        if (64 < ord(c)<91 or 96 < ord(c)<123 or 47 < ord(c)< 58 or ord(c)==32):
            concatenatedTweet = concatenatedTweet+c;
    return(''.join(concatenatedTweet))

def getMappingPOS(POSFromNLTK):
    POSForSentiWordNet=None
    if(POSFromNLTK.startswith('JJ')):
        POSForSentiWordNet = "a"
    else:
        if(POSFromNLTK.startswith('VB')):
            POSForSentiWordNet = "v"
        else:
            if(POSFromNLTK.startswith('RB')):
                POSForSentiWordNet = "r"
            else:
                 if(POSFromNLTK.startswith('NN')):
                     POSForSentiWordNet = "n"
    
    return POSForSentiWordNet;
   
with open ('ProcessedTweet.csv', 'w', encoding='utf-8') as Processed_csv_file:
    writer= csv.writer(Processed_csv_file)
    writer.writerow(['Tweets','Sentiment','Sentiment Score'])
    with open('tweets.csv',encoding='utf-8') as Tweet_csv_file:
        csvReader=csv.DictReader(Tweet_csv_file)
        for row in csvReader:
            inputTweet = remove_non_ascii(row['Tweet'])
            tokenizedTweet = nltk.word_tokenize(inputTweet);
            tweetPostStopWordRemoval=[usefulTweet for usefulTweet in tokenizedTweet if usefulTweet not in stopwords.words('english') ]
            posTaggedTweet=nltk.pos_tag(tweetPostStopWordRemoval);
            
            totalPosScore=0;
            totalNegScore=0;
            for wordWithPOS in posTaggedTweet:
                synsetsResult = swn.senti_synsets(wordWithPOS[0],getMappingPOS(wordWithPOS[1]));
                synsetsResultArr = [x for x in synsetsResult]
                if(len(synsetsResultArr) > 0):
                    synsetsResultScore = synsetsResultArr[0];
                    totalPosScore += synsetsResultScore.pos_score();
                    totalNegScore += synsetsResultScore.neg_score();
            sentencePosScore = totalPosScore / len(posTaggedTweet);
            sentenceNegScore = totalNegScore / len(posTaggedTweet);
            if(sentencePosScore > sentenceNegScore):
                sentiment="Positive"
                sentimentScore=1
            else:
                if (sentencePosScore < sentenceNegScore):
                    sentiment="Negative"
                    sentimentScore=-1
                else:
                    sentiment="Neutral"
                    sentimentScore=0
            writer.writerow([row['Tweet'], sentiment,sentimentScore]);
    
    
