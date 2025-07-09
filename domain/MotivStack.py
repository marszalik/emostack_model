from services.Singleton import Singleton
from domain.StartingMotives import StartingMotives


@Singleton
class MotivStack:

  def __init__(self):
    self.stack = []

    StartingMotives.createStartingMotives(self)

  def addMotivation(self, motivation):
    self.stack.append(motivation)

  def show(self):
    print("MotivStack:")
    print(f"Stack size: {len(self.stack)}")
    print("Motivations in the stack:")
    for motivation in self.stack:
      motivation.show()
      print("\t----------\n")

  def getFormated(self):
    prompt = ""
    for motivation in self.stack:
      prompt += motivation.getFormated()
      prompt += "\n\n---\n\n"
      return prompt

  def loadMotivations(self):
    pass
