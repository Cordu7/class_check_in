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

    # checking if the list returned by `run_sql(sql, values)` is egaampty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    for result in results:
        subemotion = Subemotion(result['subemotion_name'], result['emotion_id'], result['id'])
        subemotions.append(subemotion)
    return subemotions


def select(id):
    subemotion = None
    sql = "SELECT * FROM subemotions  WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    # checking if the list returned by `run_sql(sql, values)` is empty. Empty lists are 'fasly' 
    # Could alternativly have..
    # if len(results) > 0 
    if results:
        result = results[0]
        subemotion = Subemotion(result['subemotion_name'], result['emotion_id'], result['id'])
    return subemotion


# def delete_all():s
#     sql = "DELETE  FROM emotions "
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE  FROM emotions  WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(emotion):
#     sql = "UPDATE emotions  SET (emotion_category) = (%s) WHERE id = %s"
#     values = [emotion.emotion_category, emotion.id]
#     run_sql(sql, values)