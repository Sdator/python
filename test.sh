
INSERT_USER_OAUTH_ACCESS_TOKEN="595cdbcf231b407b8854af244b844ee8"
uid="f7455cc4aab1411ea69cafc94e153426"

echo "asdf${uid}111${INSERT_USER_OAUTH_ACCESS_TOKEN}111"

curl 'https://api.sketchfab.com/v3/models/${uid}/download' -H 'authorization: Bearer ${INSERT_USER_OAUTH_ACCESS_TOKEN}'

# curl 'https://api.sketchfab.com/v3/models/f7455cc4aab1411ea69cafc94e153426/download' -H 'authorization: Bearer 595cdbcf231b407b8854af244b844ee8'