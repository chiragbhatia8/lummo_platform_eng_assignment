# Lummo platform Engineer Assignment

This assignment focuses on using a in memory store, I have used redis as database to store the key value.

To start up with project you need docker-compose in your system.
  `docker-compose up`
 
 The main app resides app folder with 3 main endpoints:
   - /set - Which is used to set the data inside the in memory store 
            payload is `{
                          "data": {
                              "ABC": "DEF"
                          }
                      }`
   - /get/<key> : is used to retrieve the key and check and return the value, bear in mind key is a variable
   - /search: is used to search in the list with KEYS expression and will try to search with a pattern.
  
 
 The project consists of docker, docker-compose, kubernetes and monitoring stack.
 The spec files related to kuberenetes can be found under deployment folder where we are using ingress.
  P.S since i didn't have a domain name kept it as a dummy value

The monitoring stack can be started with docker-compose.monitoring.yml inside monitoring folder.
