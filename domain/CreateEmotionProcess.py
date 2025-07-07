from domain.EmoStack import EmoStack
from infrastructure.AiSrv import AiSrv
from domain.EmoThought import EmoThought
from datetime import datetime, timezone
import json


class CreateEmotionProcess:

  @staticmethod
  def runProcessFactory(context):

    emotionProcess = CreateEmotionProcess()

    prompt = emotionProcess.createPrompt(context)

    rawEmoThought = emotionProcess.sendToAi(prompt)

    emoThought = emotionProcess.createEmoThought(rawEmoThought, context)

    emoThought.save()

    # add emoThought to emoStack
    EmoStack().addEmoThought(emoThought)

  def createEmoThought(self, rawEmoThought, context):
    emoThought = EmoThought()
    emoThought.thought = rawEmoThought[0]
    emoThought.name = rawEmoThought[1]
    emoThought.score = rawEmoThought[2]
    emoThought.direction = rawEmoThought[3]
    emoThought.context = context
    emoThought.timeline = datetime.now(timezone.utc).isoformat()

    return emoThought

  def setInput(self, input):
    self.input = input

  def createPrompt(self, context):
    prompt = """Answer in the first person perspective. What is the emotion based on folowing context and what is the intensity
      of the emotion in 1 to 100 scale and what is the direction (pleasnt:+, unpleasant:-). Create very short (1-2 sentence) summary of context you taking into consideration. 
      Answer using only json [context_summary, emotion_name, emotion_intensity, emotion_direction] 
      """ + context
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

  def isValidAnswer(self, answer):
    try:
      data = json.loads(answer)
      return isinstance(data, list) and len(data) == 4
    except Exception:
      return False
