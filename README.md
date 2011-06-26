A python library for the Zeo Sleep Monitor. I've build this in my spare time as a reward for the awesome guys from Zeo. They gifted me a Zeo for free and this is one of my ways of thanking them for a great product!

All functions described in the Zeo API documentation are supported: http://mysleep.myzeo.com/api/api.shtml

# Usage

	import zeoapi
	z = zeoapi.Api()

Authenticate with:

	z.username = 'your-username'
	z.password = 'your-password'
	z.apikey = 'your-apikey'
	z.referrer = 'your-referrer'

And if the host has changed you may need to change that as well:

	z.host = 'host-provided-by-zeo'
	
(default on http://api.myzeo.com:8080/zeows/api/v1/json/sleeperService/)


## Basic functions

*	getOverallAverageZQScore
*	getOverallAverageSleepStealerScore
*	getAllDatesWithSleepData
*	getDatesWithSleepDataInRange
	
## Date specific functions
	
*	getSleepStatsForDate
*	getSleepRecordForDate
	
## Paging functions
	
*	getPreviousSleepStats
*	getPreviousSleepRecord
*	getNextSleepStats
*	getNextSleepRecord
	
## Functions for first or last sleep

*	getEarliestSleepStats
*	getEarliestSleepRecord
*	getLatestSleepStats
*	getLatestSleepRecord
	
All response for the functions are received in JSON and return as useful python dictionaries.
