from db.run_sql import run_sql
from models.emotion import Emotion


def save(emotion):
    sql = "INSERT INTO emotions (emotion_name) VALUES (%s) RETURNING *"
    values = [emotion.emotion_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    emotion.id = id
    
def select_all():
    emotions = []
    sql = "SELECT * FROM emotions "
    results = run_sql(sql)
    for result in results:
        emotion = Emotion(result['emotion_name'], result['id'] )
        emotions .append(emotion)
    return emotions 

def select(id):
    emotion = None
    sql = "SELECT * FROM emotions  WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        emotion = Emotion(result['emotion_name'], result['id'] )
    return emotion


