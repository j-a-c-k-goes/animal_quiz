# --- GLOBAL SCORE --- 
score = 0

# --- GAME TITLE --- 
def game_title():
    title = "guess the animal!"
    return title.upper()
    
# --- QUESTION CLASS ---   
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def _question(self):
        return self.question   
    def _answer(self):
        return self.answer
    def check_guess(self, answer, guess):
        global score
        still_guessing = True
        attempt = 0
       # --- BEGIN MAKING GUESSES ---
        while still_guessing and attempt < 3:
            # --- CORRECT ANSWER---
            if guess.lower() == self.answer.lower():
                score += 3 - attempt
                still_guessing = False
                # --- SCORE IS 1 ---
                if 0 > score < 2:
                    print(f"that is correct! {score} point")
                else:
                    print(f"that is correct! {score} points")
            # --- INCORRECT ANSWER ---
            else:
                if attempt < 2:
                    print(f"{guess} is incorrect")
                    guess = str(input("enter a new guess: "))
                attempt += 1
        if attempt == 3:
            print(f"the correct answer is {answer}")
            
# --- BIND & INIT GAME QUESTIONS ---
q = Question("what type of fish stings yet is not a fish?", "jellyfish") 
r = Question("what animal comes down from eucalyptus once a week to defacate?", "sloth") 
s = Question("this animal is more efficient at camoflage than a chameleon..?", "octopus") 
t = Question("what is the heaviest flightless bird that is not an ostrich?", "cassowary") 
questions = [q,r,s,t]

# --- RUN QUIZ ---
def run_quiz(questions):
    for index, el in enumerate(questions):
        guess = str(input(f"{index+1}] {el.question.title()} "))
        el.check_guess(el.answer, guess)
    print(f"final score\t{score} points")
    
# --- ON RUN / IMPORT ---
if __name__ == "__main__":
    print("--- new game ---")
    print(game_title())
    run_quiz(questions)