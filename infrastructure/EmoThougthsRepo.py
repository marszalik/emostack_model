from infrastructure.DbSrv import DbSrv
from sqlalchemy import text
from services.Singleton import Singleton


@Singleton
class EmoThoughtsRepo:

    def __init__(self):
        self.db = DbSrv()

    def getEmoThoughts(self, addEmoThought, createEmoThought):
        query = self.db.query("select * from emo_thoughts")
        results = self.db.conn().execute(query)
        data = results.mappings().all()

        for row in data:
            emoThough = self.loadEmoThought(row, createEmoThought)
            addEmoThought(emoThough)

    def loadEmoThought(self, rawEmoThought, createEmoThought):
        emoThought = createEmoThought()
        emoThought.id = rawEmoThought["id"]
        emoThought.name = rawEmoThought["name"]
        emoThought.score = rawEmoThought["score"]
        emoThought.direction = rawEmoThought["direction"]
        emoThought.timeline = rawEmoThought["timeline"]
        emoThought.thought = rawEmoThought["thought"]
        emoThought.context = rawEmoThought["context"]
        emoThought.source = rawEmoThought["source"]
        return emoThought
