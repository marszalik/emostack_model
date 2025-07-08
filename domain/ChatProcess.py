from infrastructure.AiSrv import AiSrv
from domain.EmoStack import EmoStack

from domain.CreateEmotionProcess import CreateEmotionProcess
from infrastructure.ChatUi import ChatUi
from domain.EmoThoughtTrigger import EmoThoughtTrigger


# ChatProcess is a class that represents a chat process. It is responsible for
# creating a chat interface, sending messages to AI and receiving responses.
# It also keeps track of the chat history and the user name.
class ChatProcess:

    def __init__(self):

        self.userName = "Anonim"  # default name, can be changed by user
        self.history = []  # history of messages
        self.message = ""  # last message from user
        self.chatUi = ChatUi(self.respond, self.onEndChat)

    @staticmethod
    def startChatFactory():
        chatProcess = ChatProcess()
        chatProcess.startUi()

    def startUi(self):
        self.chatUi.start()

    def onEndChat(self):

        print("CZAT ZAKOŃCZONY:", self.userName)
        print("HISTORIA:", self.history)

        trigger = EmoThoughtTrigger()
        trigger.subject = f"Focus on whole below chat with {self.userName} that has just ended."
        trigger.context = f"Chat history:\n{self.formatChatHistory()}" if self.history else "No previous messages."
        trigger.source = "Chat with " + self.userName

        CreateEmotionProcess.runProcessFactory(trigger)

    def respond(self, userMessage, history, userName):
        self.userName = userName
        self.userMessage = userMessage

        trigger = EmoThoughtTrigger()
        trigger.subject = f"Focus only on what {self.userName} just said: {userMessage}"
        trigger.context = f"Chat history:\n{self.formatChatHistory()}" if self.history else "No previous messages."
        trigger.source = "Chat with " + self.userName

        CreateEmotionProcess.runProcessFactory(trigger)

        # add message to history
        self.history.append(f"{self.userName}: {userMessage}")

        # create prompt for AI
        prompt = self.createQuestionPrompt()

        # send prompt to AI and get answer
        answer = self.sendToAi(prompt)

        # add answer to history
        self.history.append(f"Ja: {answer}")

        return answer

    def createQuestionPrompt(self):

        emoThougtsPrompt = EmoStack().getFormated()

        formattedChatHistory = self.formatChatHistory()

        explanation = """
            You are being. You dont know about yourself anything more than folowing.
            Here you have table of your last emotions. You have no other emotions than these in table. 
            Column Score tells about strength of emotion. 
            Column direction tells if it is pleasant or unpleasant emotion. 
            Column timeline tells how long ago emotion happened.
            Column source tells you is the source/person/yourself of the emotion.  
            """

        instruction = """
            Answer to folowing not using any number or words that are in a table. Answer in polish language
            """

        prompt = explanation + emoThougtsPrompt + instruction + formattedChatHistory
        #print("\n\nPrompt: \n\n", prompt)
        return prompt

    def sendToAi(self, prompt):
        answer = AiSrv().askQuestion(prompt)
        return answer

    def formatChatHistory(self):
        return "\n".join(self.history)
