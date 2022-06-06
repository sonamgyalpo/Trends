pip install git+https://github.com/GeneralMills/pytrends.git
import pandas as pd
from pytrends.request import TrendReq


header = st.container()
input1 = st.container()
relatedtopics = st.container()
relatedqueries = st.container()
trial = st.container()

with header:
	st.title("Here's our first attempt at using pytrends")
	text_input = st.text_input("Enter Keyword","loans")
	if text_input:
		# pytrend = TrendReq(hl='en-US', tz=360)
		# pytrend.build_payload(kw_list=text_input[0], cat=0, timeframe="today 12-m", geo="US")
		# def make_clickable(val):
		# 	return f'<a target="_blank" href="{val}">{val}</a>'
		# relatedtopics_analysis.style.format({'link': make_clickable})
		text_input = [text_input]
		pytrend = TrendReq(hl='en-US', tz=360)

		#provide your search terms
		pytrend.build_payload(kw_list=text_input, cat=0, timeframe="today 12-m", geo="US")

		#interest over time
		interest_over_time = pytrend.interest_over_time()
		interest_over_time = interest_over_time.iloc[:,0:1]

		#related topics
		relatedtopics_analysis = pytrend.related_topics()
		relatedtopics_analysis = relatedtopics_analysis.get(text_input[0]).get("top")
		relatedtopics_analysis = pd.DataFrame(relatedtopics_analysis)
		relatedtopics_analysis['link'] = "https://trends.google.com"+ relatedtopics_analysis['link']

		#get related queries
		related_queries = pytrend.related_queries()
		related_queries.values()

		#build lists dataframes

		top = list(related_queries.values())[0]['top']
		rising = list(related_queries.values())[0]['rising']

		#convert lists to dataframes

		dftop = pd.DataFrame(top)
		dfrising = pd.DataFrame(rising)

		#join two data frames
		joindfs = [dftop, dfrising]
		allqueries = pd.concat(joindfs, axis=1)

		#function to change duplicates

		cols=pd.Series(allqueries.columns)
		for dup in allqueries.columns[allqueries.columns.duplicated(keep=False)]: 
		    cols[allqueries.columns.get_loc(dup)] = ([dup + '.' + str(d_idx) 
		                                     if d_idx != 0 
		                                     else dup 
		                                     for d_idx in range(allqueries.columns.get_loc(dup).sum())]
		                                    )
		allqueries.columns=cols

		#rename to proper names

		allqueries.rename({'query': 'top query', 'value': 'top query value', 'query.1': 'rising query', 'value.1': 'rising query value'}, axis=1, inplace=True) 

		#check your dataset
		st.line_chart(interest_over_time)
		st.write(allqueries.head(50))
		st.write(relatedtopics_analysis[['topic_title','topic_type','value','link']])






# with relatedqueries:
# 	#We indicate that we want the topics with an increasing volume
# 	#during the established period of time
# 	trend_analysis = pytrends.related_queries()

# 	trend_analysis_top = trend_analysis.get(kw_list[0]).get('top')
# 	df1 = pd.DataFrame(trend_analysis_top)
# 	df1.columns = ["Top Queries","Value1"]

# 	trend_analysis_rising = trend_analysis.get(kw_list[0]).get('rising')
# 	df2 = pd.DataFrame(trend_analysis_rising)
# 	df2.columns = ["Rising Queries","Value2"]

# 	relatedqueries_df = pd.concat([df1,df2],axis=1)
# 	st.write(relatedqueries_df)



# with trial:
	# pytrend = TrendReq(hl='en-US', tz=360)

	# #provide your search terms
	# kw_list=['Car Loans']
	# pytrend.build_payload(kw_list=kw_list, cat=0, timeframe="today 12-m", geo="US")


	# #get related queries
	# related_queries = pytrend.related_queries()
	# related_queries.values()

	# #build lists dataframes

	# top = list(related_queries.values())[0]['top']
	# rising = list(related_queries.values())[0]['rising']

	# #convert lists to dataframes

	# dftop = pd.DataFrame(top)
	# dfrising = pd.DataFrame(rising)

	# #join two data frames
	# joindfs = [dftop, dfrising]
	# allqueries = pd.concat(joindfs, axis=1)

	# #function to change duplicates

	# cols=pd.Series(allqueries.columns)
	# for dup in allqueries.columns[allqueries.columns.duplicated(keep=False)]: 
	#     cols[allqueries.columns.get_loc(dup)] = ([dup + '.' + str(d_idx) 
	#                                      if d_idx != 0 
	#                                      else dup 
	#                                      for d_idx in range(allqueries.columns.get_loc(dup).sum())]
	#                                     )
	# allqueries.columns=cols

	# #rename to proper names

	# allqueries.rename({'query': 'top query', 'value': 'top query value', 'query.1': 'rising query', 'value.1': 'rising query value'}, axis=1, inplace=True) 

	# #check your dataset
	# st.write(allqueries.head(50))
