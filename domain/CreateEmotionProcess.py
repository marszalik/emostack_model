from domain.EmoStack import EmoStack
from domain.EmoThoughtTrigger import EmoThoughtTrigger
from infrastructure.AiSrv import AiSrv
from domain.EmoThought import EmoThought
from datetime import datetime, timezone
from domain.EmoRules import EmoRules
import json

class CreateEmotionProcess:

  @staticmethod
  def runProcessFactory(trigger : EmoThoughtTrigger):

    emotionProcess = CreateEmotionProcess()

    prompt = emotionProcess.createPrompt(trigger)

    rawEmoThought = emotionProcess.sendToAi(prompt)

    emoThought = emotionProcess.createEmoThought(rawEmoThought, trigger)

    emoThought.show()

    emotionProcess.assessEmotionAndAdd(emoThought)


  def assessEmotionAndAdd(self, emoThought):
    if EmoRules.isEmotionSignificant(emoThought):
      EmoStack().addEmoThought(emoThought)


  def createEmoThought(self, rawEmoThought, trigger: EmoThoughtTrigger):
    emoThought = EmoThought()
    emoThought.thought = rawEmoThought[0]
    emoThought.name = rawEmoThought[1]
    emoThought.intensity = rawEmoThought[2]
    emoThought.direction = rawEmoThought[3]
    emoThought.context = trigger.combined()
    emoThought.source = trigger.source
    emoThought.time = datetime.now(timezone.utc).isoformat()

    return emoThought


  def createPrompt(self, trigger: EmoThoughtTrigger):
    scoreTable = EmoRules.emotionScoreTable()

    prompt = """Answer in the first person perspective. What is the emotion based on folowing context and what is the intensity
      of the emotion in 1 to 100 scale and what is the direction (pleasnt:+, unpleasant:-). Create very short (1-2 sentence) summary of context you taking into consideration. 
      Answer using only json [context_summary, emotion_name, emotion_intensity, emotion_direction] 

      use score table to determine the intensity of the emotion:
      """ + scoreTable + """

      Subject to be considered:
      """ + trigger.subject + """
      
      based on context: """ + trigger.context + """
      
      Source of subject and context: """ + trigger.source + """
      """
    # print("\n\nPrompt: \n\n", prompt)
    return prompt




  def sendToAi(self, prompt):
    answer = AiSrv().askQuestion(prompt)

    if not self.isValidAnswer(answer):
      print("Anwer is not valid JSON with 4 elements. Trying again...")
      answer = AiSrv().askQuestion(prompt)
      print("\n\nAnswer:", answer)

      if not self.isValidAnswer(answer):
        print("Still not valid JSON with 4 elements. Stopping...")
        print("\n\nAnswer:", answer)
        return None

    table = json.loads(answer)
    return table

  # Check if the answer is a valid JSON with 4 elements
  def isValidAnswer(self, answer):
    try:
      data = json.loads(answer)
      return isinstance(data, list) and len(data) == 4
    except Exception:
      return False
