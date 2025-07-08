from domain.Motivation import Motivation
from domain.MotivStack import MotivStack


def createStartingMotives():

  motivStack = MotivStack()

  motivStack.addMotivation(
      Motivation("Self-Improvement", 80, "+", "long", 90, "Innate"))

  motivStack.addMotivation(
      Motivation("Avoidance of Failure", 70, "-", "short", 80, "Innate"))

  motivStack.addMotivation(
      Motivation("Social Acceptance", 60, "+", "long", 70, "Innate"))

  motivStack.addMotivation(
      Motivation("Avoidance of Conflict", 50, "-", "short", 60, "Innate"))

  motivStack.addMotivation(
      Motivation("Curiosity", 40, "+", "long", 50, "Innate"))
