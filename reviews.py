import pandas as pd

reviews=pd.read_csv('data/winemag-data-130k-v2.csv.zip',compression='zip')
#print(reviews)
summary=reviews.groupby('country').points.agg(['count',('points','mean')]).sort_values('count',ascending=False)
summary['points']=summary.points.round(1)
print(summary)
summary.to_csv('data/reviews-per-country.csv')
