import urllib2
import simplejson
import base64
from urlparse import urlparse

class ZeoApiError(Exception):
    '''A base class for API errors occuring'''

class Api(object):
    
    ###########################################################################################################
    # Initialize the Api class, authenticate with Api(username='my_username',password='a_secret' and the other 
    # parameters. You get them when you sign up for a API key)
    #
    # Documentation for the Zeo API can be found at: http://mysleep.myzeo.com/api/api.shtml
    ########################################################################################################### 
     
    def __init__(self, 
        apikey = None,
        username = None,
        password = None, 
        referrer = None,
        host = "http://api.myzeo.com:8080/zeows/api/v1/json/sleeperService/",
        ):
        
        self.apikey = apikey
        self.username = username
        self.password = password
        self.referrer = referrer
        self.host = host
        
    ################################################################################
    # Basic authentication and parsing URL that are returning JSON from the Zeo API 
    ################################################################################
    
    def Authenticate(self, method):
        request = urllib2.Request(method, None, {'Referer': self.referrer})
        base64string = base64.encodestring('%s:%s' % (self.username, self.password))[:-1]
        authheader =  "Basic %s" % base64string
        request.add_header("Authorization", authheader)
        return request    

    def OpenUrl(self, method):
        url = self.Authenticate(method)        
        response = urllib2.urlopen(url)
        results = simplejson.load(response)
        if results['response']['@status'] == '0':
            return results
        else:
            raise ZeoApiError('Something went wrong, error code: ' + str(results['response']['@status']))
    
    #####################################################
    # Basic functions for getting scores and date ranges.
    #####################################################
    
    def getOverallAverageZQScore(self):
        method = self.host + "getOverallAverageZQScore?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['value']
      
    def getOverallAverageSleepStealerScore(self):
        method = self.host + "getOverallAverageSleepStealerScore?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['value']
   
    def getAllDatesWithSleepData(self):
        method = self.host + "getAllDatesWithSleepData?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['dateList']['date']
    
    def getDatesWithSleepDataInRange(self, dateFrom=None, dateTo=None):
        method = self.host + "getDatesWithSleepDataInRange?key=" + self.apikey
        
        if dateFrom:
            method += '&dateFrom=' + dateFrom
        if dateTo:
            method += '&dateTo=' + dateTo
            
        result = self.OpenUrl(method)
        return result['response']['dateList']['date']
        
    ##############################################    
    # Functions for a retrieval of a specific date
    ##############################################

    def getSleepStatsForDate(self, date=None):
        if date is not None:
            method = self.host + "getSleepStatsForDate?key=" + self.apikey + '&date=' + date
            result = self.OpenUrl(method)
            return result['response']['sleepStats']
        else:
            raise ZeoApiError('A date is required to use this API. Format: "YYYY-MM-DD" ')
   
    def getSleepRecordForDate(self, date=None):
        if date is not None:
            method = self.host + "getSleepRecordForDate?key=" + self.apikey + '&date=' + date
            result = self.OpenUrl(method)
            return result['response']['sleepRecord']
        else:
            raise ZeoApiError('A date is required to use this API. Format: "YYYY-MM-DD" ')
         
    ###############################################         
    # Paging functions when getting multiple nights 
    ###############################################         
         
    def getPreviousSleepStats(self, date=None):
        if date is not None:
            method = self.host + "getPreviousSleepStats?key=" + self.apikey + '&date=' + date
            result = self.OpenUrl(method)
            return result['response']['sleepStats']
        else:
            raise ZeoApiError('A date is required to use this API. Format: "YYYY-MM-DD" ')
        
    def getPreviousSleepRecord(self, date=None):
        if date is not None:
            method = self.host + "getPreviousSleepRecord?key=" + self.apikey + '&date=' + date
            result = self.OpenUrl(method)
            return result['response']['sleepRecord']
        else:
            raise ZeoApiError('A date is required to use this API. Format: "YYYY-MM-DD" ')
        
    def getNextSleepStats(self, date=None):
        if date is not None:
            method = self.host + "getNextSleepStats?key=" + self.apikey + '&date=' + date
            result = self.OpenUrl(method)
            return result['response']['sleepStats']
        else:
            raise ZeoApiError('A date is required to use this API. Format: "YYYY-MM-DD" ')
        
    def getNextSleepRecord(self, date=None):
        if date is not None:
            method = self.host + "getNextSleepRecord?key=" + self.apikey + '&date=' + date
            result = self.OpenUrl(method)
            return result['response']['sleepRecord']
        else:
            raise ZeoApiError('A date is required to use this API. Format: "YYYY-MM-DD" ')            
    

    #########################################################
    # First or last sleep results, no date needs to specified
    #########################################################

    def getEarliestSleepStats(self):
        method = self.host + "getEarliestSleepStats?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['sleepStats']
    

    def getEarliestSleepRecord(self):
        method = self.host + "getEarliestSleepRecord?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['sleepRecord']
    

    def getLatestSleepStats(self):
        method = self.host + "getLatestSleepStats?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['sleepStats']
    
        
    def getLatestSleepRecord(self):
        method = self.host + "getLatestSleepRecord?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['sleepRecord']    
    
    #######################################
    # Logout function, ends the API session
    #######################################
    
    def logout(self):
        method = self.host + "logout?key=" + self.apikey
        result = self.OpenUrl(method)
        return result['response']['sleepRecord']
    
    
    
    