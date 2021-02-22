# records

## Heroku App Routes
- root: https://hack-records-2.herokuapp.com/
- docs: https://hack-records-2.herokuapp.com/docs
- iris: https://hack-records-2.herokuapp.com/iris
- iris query “species=Iris-setosa”: https://hack-records-2.herokuapp.com/iris?species=Iris-setosa

## Challenge Discrepancy
Something odd about the database is that the example genus given bombs has two possible genusKeys, 1340278 and 2874864. Consequently, I did not convert the genus name query to a genus name to keep all possible results. However, it seems that the difference between both queries only 2, so hopefully this discrepancy is negligible.