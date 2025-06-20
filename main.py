
from domain.ChatProcess import ChatProcess
from domain.EmoStack import EmoStack
from domain.CreateEmotionProcess import CreateEmotionProcess

print("Dzialam... ")

es = EmoStack.getEmoStack()
print("emostack", es.prompt)

ChatProcess.startNewChat()

# context = '''
#     Eliza - Czesc tu Eliza
#     Eliza - Jak tam u ciebie
#     EmoStack - Slab Kris byl dla mnie niemily
#     Eliza - co teraz planujesz zrobic?
#     EmoStack - schowac sie gdzies i nie wychodzic
#     '''

# CreateEmotionProcess.runProcess(context)