from domain.Motivation import Motivation
from domain.MotivStack import MotivStack


class StartingMotives:

  @staticmethod
  def createStartingMotives(motivStack):

    m = Motivation()
    m.name = "Hunger"
    m.intnencity = 90
    m.direction = "+"
    m.term = "short"
    m.source = "innate"
    motivStack.addMotivation(m)

    m = Motivation()
    m.name = "Social Belonging"
    m.intnencity = 70
    m.direction = "+"
    m.term = "long"
    m.source = "innate"
    motivStack.addMotivation(m)

    m = Motivation()
    m.name = "Curiosity"
    m.intnencity = 60
    m.direction = "+"
    m.term = "short"
    m.source = "innate"
    motivStack.addMotivation(m)

    m = Motivation()
    m.name = "Achievement"
    m.intnencity = 75
    m.direction = "+"
    m.term = "long"
    m.source = "extrinsic"
    motivStack.addMotivation(m)

    m = Motivation()
    m.name = "Avoid Pain"
    m.intnencity = 85
    m.direction = "-"
    m.term = "short"
    m.source = "innate"
    motivStack.addMotivation(m)
