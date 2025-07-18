from tomlkit import value
from infrastructure.EmoThougtRepo import EmoThoughtRepo
from datetime import datetime


class EmoThought:

  def __init__(self):
    self.id = None
    
    # name of the emotion
    self.name = "" 

    # intensity of the emotion in 1 to 100 scale
    self._intensity = 0

    self.originalIntensity = 0  # original intensity before fading

    # direction of the emotion, pleasant:+, unpleasant:-
    self.direction = ""

    # time when the emotion happened, in ISO format
    self.time = ""

    # thought is the summary thought that triggered the emotion
    # it is not used to create the emotion, but to understand it
    self.thought = ""

    # context of the thought, it is used to create the emotion
    self.context = ""

    # source of the thought and context
    self.source = ""

    self.hoursPassed = 0  # hours passed since the emotion was created

  @property
  def intensity(self):
    return self._intensity

  @intensity.setter
  def intensity(self, value):
    self._intensity = value
    self.originalIntensity = value
  
  def show(self):
    
    print("EmoThought:")

    attrs = self.__dict__.copy()
    if "_intensity" in attrs:
      attrs["intensity"] = attrs.pop("_intensity")

    toPrint = [f"{key}: {value}" for key, value in attrs.items()]
    print("\n\t".join(toPrint))
    print("\t----------\n")

  
  def getFormated(self):
    prompt = ""
    for value in ["name", "intensity", "direction", "time", "thought"]:
      prompt += f"{value}: {getattr(self, value)}\n"
    return prompt

  
  def save(self):
    repo = EmoThoughtRepo()
    repo.saveEmoThoguth(self)
    print("EmoThought saved")

  
  def getHoursPassed(self):
    try:
        now = datetime.now().astimezone()
        if isinstance(self.time, str):
            cleaned_time = self.time.strip("'\"").replace(" ", "T")
            parsed = datetime.fromisoformat(cleaned_time)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=now.tzinfo)
            self.time = parsed
        elif self.time.tzinfo is None:
            self.time = self.time.replace(tzinfo=now.tzinfo)

        self.hoursPassed = (now - self.time).total_seconds() / 3600    
        return self.hoursPassed
    except Exception as e:
        print(f"[WARN] Failed to parse time for EmoThought ID {self.id}: {e}")
        return 0
