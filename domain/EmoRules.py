from tabulate import tabulate

class EmoRules:

    @staticmethod
    def isEmotionSignificant(emoThought):
        """
        Assess the emotion score based on the EmoThought object.
        Returns a boolean indicating significance.
        """
        if emoThought.score > 30 and emoThought.direction == "+":
                return True
        elif emoThought.score > 20 and emoThought.direction == "-":
                return True
        else:
                return False

    @staticmethod
    def emotionScoreTable():
        """        
        Returns a markdown formatted table of emotion scores and their meanings.
        """
        
        scoreTable = [
            {"score": 1, "meaning": "Barely noticeable emotional trace, almost irrelevant."},
            {"score": 20, "meaning": "Mild, but noticeable - a minor annoyance or brief moment of pleasure."},
            {"score": 40, "meaning": "Moderate - clearly felt, influences mood but doesn't dominate thoughts or actions."},
            {"score": 60, "meaning": "Strong - noticeably shifts thinking or behavior, emotionally engaging."},
            {"score": 80, "meaning": "Very strong - memorable, leaves a long-lasting emotional mark, strongly engaging."},
            {"score": 100, "meaning": "Maximum impact - life-changing event or trauma, extreme positive or negative experience that redefines perception or priorities."},
        ]

        md = tabulate(scoreTable, headers="keys", tablefmt="pipe", stralign="left")

        return md   
