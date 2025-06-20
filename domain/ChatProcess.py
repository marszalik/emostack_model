from OpenAiSrv import OpenAiSrv
from domain.EmoStack import EmoStack
import gradio as gr
from domain.CreateEmotionProcess import CreateEmotionProcess

class ChatProcess:

    def __init__(self):
        # self.prompt = ""
        # self.answer = ""
        self.userName = "Anonim"
        self.history = []
        self.message = ""
        self.emoThoughtsPrompt = ""
        pass

    @staticmethod
    def startNewChat():
        chatProcess = ChatProcess()
        chatProcess.setEmoThougthsPrompt()
        chatProcess.startUi()
        return chatProcess

    def startUi(self):
        with gr.Blocks() as demo:
            # EKRAN 1: Imię + Start
            with gr.Row() as start_row:
                user_name = gr.Textbox(label="Podaj swoje imię", value="")
                start_btn = gr.Button("Rozpocznij chat")

            # EKRAN 2: Chat + zakończ (ukryte na start)
            with gr.Row(visible=False) as chat_row:
                chat = gr.ChatInterface(
                    fn=self.respond,
                    additional_inputs=[user_name],
                    title="EmoStack",
                    description="Start chat"
                )
                end_btn = gr.Button("Zakończ chat")
                end_message = gr.Textbox(label="Wiadomość po zakończeniu", visible=False)

            # Kliknięcie start pokazuje chat, chowa ekran startowy
            def show_chat(name):
                if name and name.strip():
                    return [gr.update(visible=False), gr.update(visible=True)]
                else:
                    return [gr.update(visible=True), gr.update(visible=False)]

            start_btn.click(
                show_chat,
                inputs=[user_name],
                outputs=[start_row, chat_row]
            )

            def end_chat():
                return [self.onEndChat(), gr.update(visible=True)]

            end_btn.click(
                end_chat,
                
                outputs=[end_message]
            )

        demo.launch(server_name="0.0.0.0", share=True)

    def onEndChat(self):
        
        print("CZAT ZAKOŃCZONY:", self.userName)
        print("HISTORIA:", self.history)
        
        formattedHistory = self.formatHistory()
        CreateEmotionProcess.runProcess(formattedHistory, f"Chat with {self.userName}")
        EmoStack.getEmoStack.loadEmoThoughts()

        
        return f"Dzięki za rozmowę, {self.userName}! Czat zakończony."
    

    def respond(self, message, history, user_name):  
        self.userName = user_name
        # self.history = history
        self.message = message
        self.history.append(f"{self.userName}: {message}")

        formattedHistory = self.formatHistory()
        prompt = self.addQuestion(formattedHistory)
        answer = self.sendToAi(prompt)
        self.history.append(message)
        self.history.append(f"Ja: {answer}")
        return answer

    def setEmoThougthsPrompt(self):
        emoStack = EmoStack.getEmoStack()
        self.emoThoughtsPrompt = emoStack.prompt

    def addQuestion(self, question):
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

        prompt = explanation + self.emoThoughtsPrompt + instruction + question
        print("\n\nPrompt: \n\n",prompt)
        return prompt

    def sendToAi(self, prompt):
        answerEngine = OpenAiSrv()
        answer = answerEngine.askQuestion(prompt)
        # print(self.answer)
        return answer

    def formatHistory(self):
        return "\n".join(self.history)
    
    