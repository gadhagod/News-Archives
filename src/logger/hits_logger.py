from os import getenv
from rockset import Client, Q, F

rs = Client(api_key=getenv('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')

def after_req(response):
    cnt = rs.sql(
            Q('NewsArchivesHits').where(F['_id']=='News').select('count')
        )[0]['count']
    rs.Collection.retrieve('NewsArchivesHits').add_docs(
        [
            {
                '_id': 'News',
                'count': cnt + 1
            }
        ]
    )
    return(response)