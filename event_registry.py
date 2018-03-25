from eventregistry import *

er = EventRegistry(apiKey = "9b322093-d7ff-46d0-aa50-82ea9840a8c2")
q = QueryArticlesIter(conceptUri = er.getConceptUri("AMD"), categoryUri = er.getCategoryUri("Technology"))
# obtain at most 500 newest articles
for art in q.execQuery(er, sortBy = "rel", maxItems = 5):
    print (art['url'])

#Searching for events https://github.com/EventRegistry/event-registry-python/wiki/Searching-for-events
# q = QueryEventsIter(conceptUri = er.getConceptUri("AMD"),
#                     keywords = None)
# for event in q.execQuery(er,
#                 sortBy = "rel",
#                 sortByAsc = False,
#                 returnInfo = ReturnInfo(),
#                 eventBatchSize = 50,
#                 maxItems = -1):
#     print (event['uri'])                
                