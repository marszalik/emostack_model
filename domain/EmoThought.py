from infrastructure.EmoThougtRepo import EmoThoughtRepo


class EmoThought:

  def __init__(self):
    self.id = None
    self.name = ""
    self.score = 0
    self.direction = ""
    self.timeline = ""
    self.thought = ""
    self.context = ""
    self.source = ""

  def show(self):
    print(
        f"EmoThought: {self.id}, {self.name}, {self.score}, {self.direction}, {self.timeline}, {self.thought}, {self.context}"
    )

  def promptFormat(self):
    prompt = ""
    for value in ["name", "score", "direction", "timeline", "thought"]:
      prompt += f"{value}: {getattr(self, value)}\n"
    return prompt

  def save(self):
    repo = EmoThoughtRepo()
    repo.saveEmoThoguth(self)
    print("EmoThought saved")
