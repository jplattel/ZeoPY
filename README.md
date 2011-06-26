This is the readme file for the Zeo Python API I'm trying to develop

All functions described in the Zeo API documentation are supported: http://mysleep.myzeo.com/api/api.shtml

===Basic functions===

	getOverallAverageZQScore
	getOverallAverageSleepStealerScore
	getAllDatesWithSleepData
	getDatesWithSleepDataInRange
	
===Date specific functions===
	
	getSleepStatsForDate
	getSleepRecordForDate
	
===Paging functions===
	
	getPreviousSleepStats
	getPreviousSleepRecord
	getNextSleepStats
	getNextSleepRecord
	
===Functions for first or last sleep===

	getEarliestSleepStats
	getEarliestSleepRecord
	getLatestSleepStats
	getLatestSleepRecord
	
All response for the functions are received in JSON and return as useful python dictionaries.
