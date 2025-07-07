from domain.ChatProcess import ChatProcess
from domain.EmoStack import EmoStack

print("Working... ")

EmoStack().loadEmoThoughts()

ChatProcess.startChatFactory()
