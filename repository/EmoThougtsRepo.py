from DbSrv import DbSrv
from sqlalchemy import text

class EmoThoughtsRepo:

    def __init__(self):
        self.db = DbSrv()

    def saveEmoThoguth(self, emoThought):
        

        sql = text(
            "insert into emo_thoughts (name, thought, score, direction, context, timeline) "
            "values (:name, :thought, :score, :direction, :context, :timeline)"
            )

        params = {
            "name": emoThought.name,
            "thought": emoThought.thought,
            "score": emoThought.score,
            "direction": emoThought.direction,
            "context": emoThought.context,
            "timeline": emoThought.timeline,
        }

        self.db.conn().execute(sql, params)
        self.db.conn().commit()  # jeśli używasz transakcji