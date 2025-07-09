from tabulate import tabulate

import math

class EmoRules:

    @staticmethod
    def isEmotionSignificant(emoThought):
        """
        Assess the emotion intensity based on the EmoThought object.
        Returns a boolean indicating significance.
        """
        if emoThought.intensity > 30 and emoThought.direction == "+":
                return True
        elif emoThought.intensity > 20 and emoThought.direction == "-":
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

    @staticmethod
    def fadeEmotionsWithTime(emoStack):
        """      
        Fades emotions in the stack based on their age.
        The score is reduced exponentially based on the fadeValue and the time passed since the emotion was created.
        Emotions older than 1 hour are faded, while fresher emotions (less than 1 hour old) retain their original score.
        Emotions with a score below 1 are removed from the stack.
        """

        fadeValue = 0.5  # default fade value for emotions

        for emoThought in emoStack.stack:
         emoThought.originalIntensity = emoThought.intensity  # save original intensity before fading
        
         hours_passed = emoThought.getHoursPassed()
         if hours_passed < 1:
            decay_factor = 1.0  # świeże emocje — bez fadingu
         else:
            decay_factor = math.exp(-fadeValue * hours_passed)

         emoThought.intensity *= decay_factor
        
         print(
             f"ID {emoThought.id}: {emoThought.originalIntensity:.2f} → {emoThought.intensity:.2f} (age: {hours_passed:.1f}h)"
         )
        
        # remove emotions with intensity below 1
        emoStack.stack = [e for e in emoStack.stack if e.intensity >= 1]        