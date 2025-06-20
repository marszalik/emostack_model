from domain.EmoThought import EmoThought
from DbSrv import DbSrv


class EmoStack:
   _instance = None

   def __init__(self):

      self.stack = []
      self.prompt = ""

   @staticmethod
   def getEmoStack():
      if EmoStack._instance is None:
         EmoStack._instance = EmoStack()
         es = EmoStack._instance
         es.loadEmoThoughts()
         es.prompt = es.promptFormat()

      return EmoStack._instance

   def addEmoThought(self, emoThought):
      self.stack.append(emoThought)

   def loadEmoThoughts(self):
      db = DbSrv()

      results = db.conn().execute(db.query("select * from emo_thoughts"))
      data = results.mappings().all()

      self.stack = []
      for row in data:
         emoThough = self.loadEmoThought(row)
         self.stack.append(emoThough)

   def loadEmoThought(self, rawEmoThought):
      emoThought = EmoThought()
      emoThought.id = rawEmoThought["id"]
      emoThought.name = rawEmoThought["name"]
      emoThought.score = rawEmoThought["score"]
      emoThought.direction = rawEmoThought["direction"]
      emoThought.timeline = rawEmoThought["timeline"]
      emoThought.thought = rawEmoThought["thought"]
      emoThought.context = rawEmoThought["context"]
      emoThought.source = rawEmoThought["source"]
      return emoThought

   def show(self):
      for emoThought in self.stack:
         print(emoThought)

   def promptFormat(self):
      prompt = ""
      for emoThought in self.stack:
         prompt += emoThought.promptFormat()
         prompt += "\n\n---\n\n"
      return prompt
