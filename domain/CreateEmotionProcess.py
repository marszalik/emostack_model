from infrastructure.AiSrv import AiSrv
from domain.EmoThought import EmoThought
from datetime import datetime, timezone
import json


class CreateEmotionProcess:

  def __init__(self):
    pass

  @staticmethod
  def runProcess(context, source):
    process = CreateEmotionProcess()
    prompt = process.createPrompt(context)
    print("prompt", prompt)
    rawEmoThought = process.sendToAi(prompt)
    print("rawEmoThought", rawEmoThought)
    emoThought = process.createEmoThought(rawEmoThought, context, source)
    emoThought.save()
    return process

  def createEmoThought(self, rawEmoThought, context, source):
    emoThought = EmoThought()
    emoThought.thought = rawEmoThought[0]
    emoThought.name = rawEmoThought[1]
    emoThought.score = rawEmoThought[2]
    emoThought.direction = rawEmoThought[3]
    emoThought.context = context
    emoThought.source = source
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

    table = json.loads(answer)
    return table
