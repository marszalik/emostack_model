from domain.EmoThought import EmoThought
from infrastructure.EmoThougthsRepo import EmoThoughtsRepo
from services.Singleton import Singleton


@Singleton
class EmoStack:

   def __init__(self):

      self.stack = []

   def addEmoThought(self, emoThought: EmoThought):
      self.stack.append(emoThought)

   # load the stack from the database
   def loadEmoThoughts(self):

      # zero the stack
      self.stack = []

      # load the stack from the database
      EmoThoughtsRepo().getEmoThoughts(self.addEmoThought, EmoThought)

   def show(self):
      for emoThought in self.stack:
         print(emoThought)

   def getFormated(self):
      prompt = ""
      for emoThought in self.stack:
         prompt += emoThought.getFormated()
         prompt += "\n\n---\n\n"
      return prompt
