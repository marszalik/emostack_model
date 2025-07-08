from domain.EmoThought import EmoThought
from infrastructure.EmoThougthsRepo import EmoThoughtsRepo
from services.Singleton import Singleton
from datetime import datetime, timezone

import math
from datetime import datetime

@Singleton
class EmoStack:

   
   def __init__(self):

      self.stack = []
      self.fadeValue = 0.5  # default fade value for emotions


   
   def recountStack(self):
      """
      use each time the stack is changed to recount the stack
      """
      
      # sort the stack by score in descending order
      self.stack.sort(key=lambda x: x.score, reverse=True)

      # fade emotions based on their age
      self.fadeEmotionsWithTime()


   
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


   # show the stack in the console
   def show(self):
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


   def fadeEmotionsWithTime(self):
      """      
      Fades emotions in the stack based on their age.
      The score is reduced exponentially based on the fadeValue and the time passed since the emotion was created.
      Emotions older than 1 hour are faded, while fresher emotions (less than 1 hour old) retain their original score.
      Emotions with a score below 1 are removed from the stack.
      """
      
      for emoThought in self.stack:
         emoThought.originalScore = emoThought.score  # save original score before fading

         hours_passed = emoThought.getHoursPassed()
         if hours_passed < 1:
            decay_factor = 1.0  # świeże emocje — bez fadingu
         else:
            decay_factor = math.exp(-self.fadeValue * hours_passed)

         emoThought.score *= decay_factor

         print(f"ID {emoThought.id}: {emoThought.originalScore:.2f} → {emoThought.score:.2f} (age: {hours_passed:.1f}h)")

      self.stack = [e for e in self.stack if e.score >= 1]