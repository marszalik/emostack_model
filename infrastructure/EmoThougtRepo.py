from infrastructure.DbSrv import DbSrv
from sqlalchemy import text


class EmoThoughtRepo:

    def __init__(self):
        self.db = DbSrv()

    def saveEmoThoguth(self, emoThought):

        sql = text(
            "insert into emo_thoughts (name, thought, intensity, direction, context, time, source) "
            "values (:name, :thought, :intensity, :direction, :context, :time, :source)"
        )

        params = {
            "name": emoThought.name,
            "thought": emoThought.thought,
            "intensity": emoThought.intensity,
            "direction": emoThought.direction,
            "context": emoThought.context,
            "time": emoThought.time,
            "source": emoThought.source
        }

        self.db.conn().execute(sql, params)
        self.db.conn().commit()  # jeśli używasz transakcji
