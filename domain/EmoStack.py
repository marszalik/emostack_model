from domain.EmoRules import EmoRules
from domain.EmoThought import EmoThought
from infrastructure.EmoThougthsRepo import EmoThoughtsRepo
from services.Singleton import Singleton
from datetime import datetime, timezone

from datetime import datetime


@Singleton
class EmoStack:

   def __init__(self):

      self.stack = []

   def recountStack(self):
      """
      use each time the stack is changed to recount the stack
      """

      # sort the stack by score in descending order
      self.stack.sort(key=lambda x: x.score, reverse=True)

      # fade emotions based on their age
      EmoRules.fadeEmotionsWithTime(self)

   def addEmoThought(self, emoThought: EmoThought):
      """
      add an emoThought to the stack and save it to the database
      """

      emoThought.save()

      self.stack.append(emoThought)

      self.recountStack()

   def loadEmoThoughts(self):
      """
      load emoThoughts from the database and add them to the stack
      """

      # zero the stack
      self.stack = []

      # internal function to load each emoThought from the database
      def loadEmoThought(emoThought: EmoThought):
         # add emoThought to the stack
         self.stack.append(emoThought)

      # load the stack from the database
      EmoThoughtsRepo().getEmoThoughts(loadEmoThought, EmoThought)

      self.recountStack()

   def show(self):
      """
      Prints the current state of the EmoStack to the console.
      """
      print("EmoStack:")
      print(f"Stack size: {len(self.stack)}")
      print("EmoThoughts in the stack:")
      for emoThought in self.stack:
         emoThought.show()

   def getFormated(self):
      """
      Returns a formatted string representation of the EmoStack.
      """
      prompt = ""
      for emoThought in self.stack:
         prompt += emoThought.getFormated()
         prompt += "\n\n---\n\n"
      return prompt
