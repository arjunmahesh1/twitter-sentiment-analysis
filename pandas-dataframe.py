from tqdm import tqdm
tqdm.pandas()

tweet_dataframe['sentiment'] = tweet_dataframe['text'].progress_apply(get_sentiment)
tweet_dataframe.head()

import seaborn as sns
sns.set_style("darkgrid")
sns.set(rc={'figure.figsize':(10,7)})
sns.set_context("poster")

print(tweet_dataframe['sentiment'].value_counts())
sns.countplot(x='sentiment', data = tweet_dataframe)

# Plot some tweets with positive/negative sentiments

positive_tweets = tweet_dataframe[tweet_dataframe['sentiment'] == 'Positive']['text'].tolist()
for i, pos in enumerate(positive_tweets[10:15]):
  print(i, " - ", pos)

negative_tweets = tweet_dataframe[tweet_dataframe['sentiment'] == 'Negative']['text'].tolist()
for i, pos in enumerate(negative_tweets[10:15]):
  print(i, " - ", pos)

