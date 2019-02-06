# Parse json file and input into neo4j database through put request
import fileinput
import csv
import json
import requests
import sys


# api-endpoint
ACTOR_API_ENDPOINT = "http://localhost:8080/api/v1/addActor"
MOVIE_API_ENDPOINT = "http://localhost:8080/api/v1/addMovie"
RELATIONSHIPS_API_ENDPOINT = "http://localhost:8080/api/v1/addRelationship"

 
def makeRequest(jsonRequest, API_ENDPOINT):
    # sending post request and saving response as response object
    r = requests.post(url = API_ENDPOINT, data = jsonRequest)
    # status code 
    # print(r.status_code, r.reason)
    return


def createActorJson(row):
    jsonRequest = {"name": row[1] ,"actorId" : row[0]}
    jsonRequest = json.dumps(jsonRequest)
    makeRequest(jsonRequest, ACTOR_API_ENDPOINT)
    return

def createMovieJson(row):
    jsonRequest = {"name": row[2] ,"movieId" : row[0]}
    jsonRequest = json.dumps(jsonRequest)
    # print(jsonRequest)
    makeRequest(jsonRequest, MOVIE_API_ENDPOINT)
    return

def createRelationshipJson(row):
    jsonRequest = {"actorId": row[2] ,"movieId" : row[0]}
    jsonRequest = json.dumps(jsonRequest)
    # print(jsonRequest)
    makeRequest(jsonRequest, RELATIONSHIPS_API_ENDPOINT)
    return

if __name__ == '__main__':
    INPUT = sys.argv[1]
    with open(INPUT, 'r') as file:
        # Read each line from the file
        if INPUT == "movies.tsv":
            rd = csv.reader(file, delimiter="\t", quotechar='"')
            for row in rd:
                createMovieJson(row)
        elif INPUT == "actors.tsv":
            rd = csv.reader(file, delimiter="\t", quotechar='"')
            for row in rd:
                createActorJson(row)
        elif INPUT == "relationships.tsv":
            rd = csv.reader(file, delimiter="\t", quotechar='"')
            for row in rd:
                createRelationshipJson(row)


