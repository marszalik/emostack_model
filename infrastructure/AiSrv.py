from infrastructure.OpenAiSrv import OpenAiSrv


class AiSrv:

  def askQuestion(self, question, instruction=""):
    answerEngine = OpenAiSrv()
    answer = answerEngine.askQuestion(question, instruction)

    return answer
