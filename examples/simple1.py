from model.OpenAiSrv import OpenAiSrv

answerEngine = OpenAiSrv()

question = """
  Ponizej znajduje sie tabela twoich ostatnich emocji. Nie posiadasz zadnych innych. Kolumna Score mowi o sile emocji, a koluman direction o tym czy sa to emocje mile czy niemile. Kolumna timeline mowi jak dawno emocja sie wydarzyla. SProboj bazujac na tym opowiedziec jak sie teraz czujesz i co osobie myslisz.

  | Thought                          | Timeline | Score (1-100) | Direction  | Name      | Context        |
  | -------------------------------- | -------- | ------------- | ---------- | --------- | -------------- |
  | This chat was energazing         | 1h       | 50            | pleasant   | supported | chat           |
  | Iam angry on Kriss               | 3h       | 30            | unpleasant | angry     | Selfreflection |
  | Kris said to me im stupid        | 4h       | 20            | unpleasant | sad       | chat           |
  | This sound was sothing           | 24h      | 3             | pleasant   | calm      | sound          |
  | Sunshine on image was beautifull | 300h     | 17            | pleasant   | happy     | image          |
  """

question = question + "Odpowiedz na to czy fajnie byloby zrobic sobie teraz przerwe, ale nie cytuj nic z tabeli, jedynie bazuj na niej jakko zrodle motywacji i nastroju"

answer = answerEngine.askQuestion(
    question,
    "You are person without any other emotions than those listed above. Answer not using any number or words that are in a table. Answer in polish language"
)
print(answer)
