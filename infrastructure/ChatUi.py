import gradio as gr


class ChatUi:

    def __init__(self, respond, onEndChat):
        self.respond = respond
        self.onEndChat = onEndChat

    def start(self):
        with gr.Blocks() as demo:
            # EKRAN 1: Imię + Start
            with gr.Row() as start_row:
                user_name = gr.Textbox(label="Podaj swoje imię", value="")
                start_btn = gr.Button("Rozpocznij chat")

            # EKRAN 2: Chat + zakończ (ukryte na start)
            with gr.Row(visible=False) as chat_row:
                chat = gr.ChatInterface(fn=self.respond,
                                        additional_inputs=[user_name],
                                        title="EmoStack",
                                        description="Start chat")
                end_btn = gr.Button("Zakończ chat")
                end_message = gr.Textbox(label="Wiadomość po zakończeniu",
                                         visible=False)

            # Kliknięcie start pokazuje chat, chowa ekran startowy
            def show_chat(name):
                if name and name.strip():
                    return [gr.update(visible=False), gr.update(visible=True)]
                else:
                    return [gr.update(visible=True), gr.update(visible=False)]

            start_btn.click(show_chat,
                            inputs=[user_name],
                            outputs=[start_row, chat_row])

            def end_chat():
                return [self.onEndChat(), gr.update(visible=True)]

            end_btn.click(end_chat, outputs=[end_message])

        demo.launch(server_name="0.0.0.0", share=True)
