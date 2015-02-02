# MongoDb
from pymongo import MongoClient # the mongo client
from bson import json_util # to read bson boject from MongoDB
from bson.objectid import ObjectId # get bson ojbect id into python readable

import json
from datetime import datetime

clientRemote = MongoClient('mongodb://104.131.97.242:27017/')
clientLocal = MongoClient('mongodb://localhost:27017/')

def main():
	try:
		db_remote = clientRemote['bot']
		db_local = clientLocal['cricketApp']
		collection_matches = db_remote['espn_teamWise_head2head']
		collection_matches_local = db_local['espn_teamWise_head2head_refined']
	except: return jsonify(error='Invalid access.')
	matches_pointer = collection_matches.find().sort("CountryId", 1)
	for i in matches_pointer: # going to each country
		team = {
			"countryName": i["CountryName"].lower(),
			"format": i["format"],
			"_url": i["_url"]
		}
		matches_data=[]
		print team
		data_items = i["_data"]
		months = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10","Nov": "11", "Dec": "12"}
		count=0
		for j in data_items: # for every match
			match= {}
			count+=1
			for key in j: # for all key-value pairs in the match
				val = j[key]
				if key=="start date":
					d_item = val.split()
					yy = int(d_item[2].strip())
					mm = int(months[d_item[1]].strip())
					dd = int(d_item[0].strip())
					date = datetime(yy, mm, dd)
					match.update({"startDate": str(yy)+"-"+str(mm)+"-"+str(dd), "strStartDate": val,"utcDate": date})
				elif key=="opposition":
					match.update({"opposition": val[1:].strip().lower()}) #v New Zealand
				elif key=="toss" or key=="result" or key=="team" or key=="ground": #lower()
					match.update({key: val.lower()})
				else:
					match.update({key: val})
			#print match
			matches_data.append(match)
			print count
		team.update({"_data": matches_data})
		collection_matches_local.insert(team)
if __name__=="__main__":
	main()