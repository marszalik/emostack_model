from domain.EmoThought import EmoThought
from infrastructure.EmoThougthsRepo import EmoThoughtsRepo
from Singleton import Singleton


@Singleton
class EmoStack:
   _instance = None

   def __init__(self):

      self.stack = []
      self.prompt = ""

   def reload(self):
      self.loadEmoThoughts()
      self.prompt = self.promptFormat()
      return self

   def addEmoThought(self, emoThought):
      self.stack.append(emoThought)

   def createEmoThought(self):
      return EmoThought()

   # load the stack from the database
   def loadEmoThoughts(self):
      # zero the stack
      self.stack = []
      # load the stack from the database
      EmoThoughtsRepo().getEmoThoughts(self.addEmoThought,
                                       self.createEmoThought)

   def show(self):
      for emoThought in self.stack:
         print(emoThought)

   def promptFormat(self):
      prompt = ""
      for emoThought in self.stack:
         prompt += emoThought.promptFormat()
         prompt += "\n\n---\n\n"
      return prompt
