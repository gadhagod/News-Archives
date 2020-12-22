while :; do
    if [ "$(date +%H)" -eq "14" ]; then 
        curl --request POST \
            --url https://api.rs2.usw2.rockset.com/v1/orgs/self/ws/commons/collections/NewsArchivesHits/docs \
            -H 'Authorization: ApiKey '"$ROCKSET_SECRET"'' \
            -H 'Content-Type: application/json' \
            -d '{
                "_id": "'""$(date +20%y-%m-%d)""'",
                "articles": '""$(python3 news.py)""'
            }'
    fi
done