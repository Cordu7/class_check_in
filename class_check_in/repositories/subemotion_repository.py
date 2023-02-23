from db.run_sql import run_sql
from models.subemotion import Subemotion

def save(subemotion):
    sql = "INSERT INTO subemotions (subemotion_name, emotion_id ) VALUES (%s, %s) RETURNING *"
    values = [subemotion.subemotion_name, subemotion.emotion.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    subemotion.id = id
    
def select_all():
    subemotions = []
    sql = "SELECT * FROM subemotions "
    results = run_sql(sql)
    for result in results:
        subemotion = Subemotion(result['subemotion_name'], result['emotion_id'], result['id'])
        subemotions.append(subemotion)
    return subemotions 

def select_by_emotion(emotion):
    subemotions = []
    sql = "SELECT * FROM subemotions  WHERE emotion_id = %s"
    values = [emotion.id]
    results = run_sql(sql, values)
    for result in results:
        subemotion = Subemotion(result['subemotion_name'], result['emotion_id'], result['id'])
        subemotions.append(subemotion)
    return subemotions


def select(id):
    subemotion = None
    sql = "SELECT * FROM subemotions  WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        subemotion = Subemotion(result['subemotion_name'], result['emotion_id'], result['id'])
    return subemotion

