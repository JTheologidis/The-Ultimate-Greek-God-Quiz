from tkinter import *
from functools import partial   # To prevent unwanted windows
import random
from turtle import bgcolor


class Main:
    def __init__(self, parent):

        # Formatting variables
        background_color = "light blue"

        # Initialise list to hold quiz results
        self.difficulty = IntVar()
        self.difficulty.set(0)

        # normal_list = normal_q_a_list_true, normal_q_a_list_false
        # hard_list = hard_q_a_list_true, hard_q_a_list_false

        # randomly choose from the list...
        

        # Main Menu Frame
        self.main_frame = Frame(width=200, bg=background_color,
                                     pady=10)
        self.main_frame.grid()

        # Main Menu Heading (row 0)
        self.main_heading_label = Label(self.main_frame,
                                        text="The Ultimate Greek God Quiz",
                                          font="Arial 18 bold",
                                          bg=background_color,
                                          padx=10, pady=10)
        self.main_heading_label.grid(row=0)
        
        # User Instructions (row 1)
        self.main_instructions_label = Label(self.main_frame,
                                             text="Welcome to The Ultimate Greek God Quiz!\n"  
                                                  "Choose a difficulty and test your knowledge.\n\n" \
                                                  "Click the 'Help' button to view instructions\n"
                                                  "or click the 'Quit' button to exit to desktop.",
                                          font="Arial 10", wrap=260,
                                          justify=LEFT, bg=background_color,
                                          padx=10, pady=10)
        self.main_instructions_label.grid(row=1)

        # Button frame (row 2)
        self.quiz_difficulty_frame = Frame(self.main_frame, bg=background_color)
        self.quiz_difficulty_frame.grid(row=2)
        
        # Buttons go here...
        button_font = "Arial 12 bold"
        
        # Easy quiz button...
        self.easy_quiz_button = Button(self.quiz_difficulty_frame, text="Easy",
                                       command=lambda: self.to_quiz(0),
                                       font=button_font, bg="#3EC70B",
                                       fg="white")
        self.easy_quiz_button.grid(row=2, column=0, pady=10)

        # Normal quiz button...
        self.normal_quiz_button = Button(self.quiz_difficulty_frame, text="Normal",
                                       command=lambda: self.to_quiz(1),
                                       font=button_font, bg="#FF9933",
                                       fg="white")
        self.normal_quiz_button.grid(row=2, column=1, padx=10, pady=10)

        # Hard quiz button...
        self.hard_quiz_button = Button(self.quiz_difficulty_frame, text="Hard",
                                       command=lambda: self.to_quiz(2),
                                       font=button_font, bg="#FF1818",
                                       fg="white")
        self.hard_quiz_button.grid(row=2, column=2, pady=10)

        # Help and Quit Frame
        self.help_quit_frame = Frame(self.quiz_difficulty_frame)
        self.help_quit_frame.grid(row=3, column=1, pady=5)

        self.help_button = Button(self.help_quit_frame, font=button_font,
                                       text="Help", bg="#7C99AC",
                                       fg="white", command=self.help,
                                       justify=CENTER)
        self.help_button.grid(row=0, column=1)

        self.quit_frame = Frame(self.quiz_difficulty_frame)
        self.quit_frame.grid(row=3, column=2, pady=5)

        self.quit_button = Button(self.help_quit_frame, font=button_font,
                                       text="Quit", bg="#890F0D",
                                       fg="white", command=self.to_quit,
                                       justify=CENTER)
        self.quit_button.grid(row=0, column=2)

    def to_quiz(self, difficulty_list):

        # retrieve starting difficulty
        # difficulty_list = self.difficulty.get()
        Quiz(self, difficulty_list)

        if self.to_quiz:
            self.easy_quiz_button.config(state=DISABLED)
            self.normal_quiz_button.config(state=DISABLED)
            self.hard_quiz_button.config(state=DISABLED)
            self.help_button.config(state=DISABLED)

        

        

    def help(self):
        Help(self)

    def to_quit(self):
        root.destroy()





class Help:
    def __init__(self, partner):

        # disable help button
        partner.help_button.config(state=DISABLED)
        
        # Sets up child window (ie: help box)
        self.help_box = Toplevel()

        # If users press cross at the top, closes help and 'releases' help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # Set up GUI Frame
        self.help_frame = Frame(self.help_box, width=300)
        self.help_frame.grid()

        # Set up Help heading (row 0)
        self.how_heading = Label(self.help_frame, text="Help / Instructions",
                                 font="arial 10 bold")
        self.how_heading.grid(row=0)

        help_text="This quiz is to test your knowledge on Greek Gods.  " \
                  "You can choose between three difficulties (Easy, Normal, " \
                  "and Hard).\n\n" \
                  "Easy mode will include 5 questions that most people can answer. " \
                  "Normal mode will include 5 questions that only some people are able to answer, " \
                  "and Hard mode will include 5 questions that only experts know the answers to " \
                  "\n\n" \
                  "After completing the quiz, you will have the option of viewing and exporting  " \
                  "your results via .txt file. To do this, you can click 'View Results' which will " \
                  "show your results from the most recently completed quiz. From there, you can " \
                  "click the 'Export' button if you want to export your results.\n\n" \
                  "Nobody can stop you from looking up the answers online,\n" \
                  "though I would appreciate it if you didn't.\n\n" \
                  "Cheating is not cool :("


        # Help text (label, row 1)
        self.help_text = Label(self.help_frame, text=help_text,
                               justify=LEFT, wrap=400, padx=10, pady=10)
        self.help_text.grid(row=1)

        # Dismiss button (row 2)
        self.dismiss_btn = Button(self.help_frame, text="Dismiss",
                                  width=10, bg="#660000", fg="white", 
                                  font="arial 15 bold",
                             command=partial(self.close_help, partner))
        self.dismiss_btn.grid(row=2, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()



class Quiz:
    def __init__(self, partner, level):

        background_color = "#d4f0d3"    # light green

        button_color = "#7a7a7a"    #light grey

        # Initialise list to hold quiz results
        

        # List for holding statistics
        self.quiz_stats_list = []
        
        # initialise variables
        self.q_amount = IntVar()
        self.q_number = IntVar()
        self.score = IntVar()
        # Set # of questions at the start of quiz
        self.q_amount.set(6)

        self.level = IntVar()
        self.level.set(level)

        # Set question number
        self.q_number.set(0)

        # Set score
        self.score.set(0)
        
        # Correct/Incorrect answers
        self.answer_true = StringVar()
        self.answer_false = StringVar()

        # Answer Feebdack
        # self.feedback = StringVar
        # self.feedback = ""
       
        # GUI Setup
        self.quiz_box = Toplevel()

        # If users press cross at top, quiz quits
        self.quiz_box.protocol('WM_DELETE_WINDOW', self.to_quit)

        self.quiz_frame = Frame(self.quiz_box, bg=background_color)
        self.quiz_frame.grid()

        # Heading Row (Question No.)
        self.question_number_label = Label(self.quiz_frame, text=" ", font="Arial 24 bold", wrap=400, bg=background_color, padx=10, pady=10)
        self.question_number_label.grid(row=0)

        # Question Label
        self.question_label = Label(self.quiz_frame, text="Push 'Next Question' to start quiz",
                                   font="Arial 20 bold", wrap=400, bg=background_color,
                                   padx=10, pady=10)
        self.question_label.grid(row=1)



        # Answer buttons go here... (row 2 and 3)
        self.answer_frame = Frame(self.quiz_frame, bg=background_color)
        self.answer_frame.grid(row=2)

        self.answer_button_1 = Button(self.answer_frame, text="?",
                                      font="Arial 11 bold", bg=button_color,
                                      fg="white", width=25, command=lambda: self.reveal_answer(1))
        self.answer_button_1.config(state=DISABLED)
        self.answer_button_1.grid(row=0, column=0, padx=10, pady=10)

        self.answer_button_2 = Button(self.answer_frame, text="?",
                                      font="Arial 11 bold", wrap=400, bg=button_color,
                                      fg="white", width=25, command=lambda: self.reveal_answer(2))
        self.answer_button_2.config(state=DISABLED)
        self.answer_button_2.grid(row=0, column=1, padx=10, pady=10)

        self.answer_button_3 = Button(self.answer_frame, text="?",
                                      font="Arial 11 bold", wrap=400, bg=button_color,
                                      fg="white", width=25, command=lambda: self.reveal_answer(3))
        self.answer_button_3.config(state=DISABLED)
        self.answer_button_3.grid(row=1, column=0, padx=10, pady=10)

        self.answer_button_4 = Button(self.answer_frame, text="?",
                                      font="Arial 11 bold", wrap=400, bg=button_color,
                                      fg="white", width=25, command=lambda: self.reveal_answer(4))
        self.answer_button_4.config(state=DISABLED)
        self.answer_button_4.grid(row=1, column=1, padx=10, pady=10)

        # Correct/Incorrect feedback message display...
        self.correct_incorrect_text = Label(self.quiz_frame, text="", bg=background_color)
        self.correct_incorrect_text.grid(row=6, padx=5, pady=5)

        # Correct Answer/Score Counter
        self.score_text = Label(self.quiz_frame, text="", bg=background_color)
        self.score_text.grid(row=7, padx=5, pady=5)

        # Buttons for Next Question and Quit (row 6)
        self.results_next_quit_frame = Frame(self.quiz_frame, bg=background_color)
        self.results_next_quit_frame.grid(row=8, pady=10)

        self.next_button = Button(self.results_next_quit_frame, text="Next Question",
                                  font="Arial 15 bold", bg="#34c3eb", fg="white", command=self.next_question)
        self.next_button.grid(row=6, column=0, padx=10, pady=10)        

        self.quit_button = Button(self.results_next_quit_frame, text="Quit",
                                  fg="white", bg="#660000", font="Arial 15 bold",
                             command=self.to_quit)
        self.quit_button.grid(row=6, column=1, padx=5, pady=5)




    def next_question(self):

        difficulty_list = self.level.get()

        # default button color
        button_color = "#7a7a7a"

        print("you pushed the next button")
        
        # Easy List
        easy_q_a_list_true = [["Zeus", "The Sky, Thunder and Lightning"],
                              ["Poseidon", "The Sea"],
                              ["Hades", "The Underworld"],
                              ["Ares", "War"],
                              ["Athena", "Wisedom"]]
        

        normal_q_a_list_true = [["Apollo", "Music, Arts, And Knowledge"],
                                ["Hera", "Marriage, Women and Childbirth"],
                                ["Hermes", "Trade and Communication"],
                                ["Artemis", "The hunt, Wild animals"],
                                ["Aphrodite", "Beauty, Love and Pleasure"],
                                ["Hephaestus", "Fire, Metalworking"],
                                ["Dionysus", "Wine"]]

        hard_q_a_list_true = [["Achlys", "Poisons"],
                              ["Hypnos", "Sleep"],
                              ["Chronos", "Time"],
                              ["Aion", "Eternity"],
                              ["Eros", "Love"],
                              ["Nyx", "Night"],
                              ["Aether", "Light"],
                              ["Erebus", "Darkness"],
                              ["Thanatos", "Death"],
                              ["Chaos", "Nothingness"]]

        q_a_list_false = ["Dirt", "Sand", "Wind", "Steam",
                          "Smoke", "The Stars", "Mischief",
                          "Justice", "Modesty", "Luck",
                          "Snow", "Energy", "Misfortune", "Hatred",
                          "Evolution","Dark Matter", "Cookery",
                          "Nature", "Harvest", "Triumph", "Greed",
                          "Stone", "Wonder", "Intelligence", "Agility",
                          "Betrayal", "Plasma", "Space", "The Universe",
                          "Rot", "Liberty", "Laughter", "Peace", "Color",
                          "Visions", "Witchcraft", "Illusions", "Poverty",
                          "Mutation", "Jealousy", "Exile", "Gold", "Silver",
                          "Bronze", "Platinum", "Healing", "Discovery"]
        
        
        
        normal_q_a_list_true.append(1)
        hard_q_a_list_true.append(2)

        # randomizes list order...
        random.shuffle(easy_q_a_list_true)
        random.shuffle(normal_q_a_list_true)
        random.shuffle(hard_q_a_list_true)
        random.shuffle(q_a_list_false)
        
        # Chooses Corresponding Lists, Randomizes Q&A...

        if difficulty_list == 0:
            q_a_row = random.choice(easy_q_a_list_true)
        elif difficulty_list == 1:
            q_a_row = random.choice(normal_q_a_list_true)
        else:
            q_a_row = random.choice(hard_q_a_list_true)
            

        question = q_a_row[0]
        answer_true = q_a_row[1]
        optn_2 = random.choice(q_a_list_false)
        optn_3 = random.choice(q_a_list_false)
        optn_4 = random.choice(q_a_list_false)

        all_choices = [answer_true, optn_2, optn_3, optn_4]

        random.shuffle(all_choices)

        question_text = ("{} is the God of what?".format(question))
        self.question_label.config(text=question_text)
        print(question_text)


        answer_text_1 = ("{}".format(all_choices[0]))
        self.answer_button_1.config(text=answer_text_1)

        answer_text_2 = ("{}".format(all_choices[1]))
        self.answer_button_2.config(text=answer_text_2)

        answer_text_3 = ("{}".format(all_choices[2]))
        self.answer_button_3.config(text=answer_text_3)

        answer_text_4 = ("{}".format(all_choices[3]))
        self.answer_button_4.config(text=answer_text_4)

        # answer and quit buttons back to normal
        self.answer_button_1.config(state=NORMAL)
        self.answer_button_2.config(state=NORMAL)
        self.answer_button_3.config(state=NORMAL)
        self.answer_button_4.config(state=NORMAL)

        # retrieve correct/incorrect answers
        correct_answers = answer_true
        self.answer_true.set(correct_answers)
        
        
        incorrect_answers = [optn_2, optn_3, optn_4]
        self.answer_false.set(incorrect_answers)


        # retrieves the question from the initial function...
        number_of_questions_to_go = self.q_amount.get()
        correct_answers = 0

        # retrieves question number
        question_number = self.q_number.get()
        question_number += 1
        self.q_number.set(question_number)

        question_number_text = ("Question {}".format(question_number))
        self.question_number_label.config(text = question_number_text)

        # retrieves score
        score = self.score.get()
        self.score_text.config(text="Score: {}/5".format(score))

        # Deduct question from quiz
        number_of_questions_to_go -= 1 

        # Add correct answers
        number_of_questions_to_go += correct_answers

        # Set question to new question
        self.q_amount.set(number_of_questions_to_go)

        # Resets answer feedback to ""
        self.correct_incorrect_text.config(text="")

        # Resets button colour back to normal
        self.answer_button_1.config(bg=button_color)
        self.answer_button_2.config(bg=button_color)
        self.answer_button_3.config(bg=button_color)
        self.answer_button_4.config(bg=button_color)

        # Disable next question button (force user to choose answer)
        self.next_button.config(state=DISABLED)

        # Edit label and disable buttons so user knows quiz is completed
        if number_of_questions_to_go < 2:
            self.next_button.config(text="Finish Quiz")

        if number_of_questions_to_go < 1:
            self.next_button.config(state=DISABLED)
            self.answer_button_1.config(state=DISABLED)
            self.answer_button_2.config(state=DISABLED)
            self.answer_button_3.config(state=DISABLED)
            self.answer_button_4.config(state=DISABLED)
            self.quiz_box.focus()
            self.next_button.config(text="Quiz Completed")
            print("Quiz Finished!")

        if number_of_questions_to_go < 1:
            quiz_completed_statement = "You have completed the Quiz! \n" \
                                       "Push the 'Quit' button to exit.".format(number_of_questions_to_go)

            self.question_label.configure(text=quiz_completed_statement)
            self.question_label.config(fg="#660000", font="Arial 10 bold",
                                       text=quiz_completed_statement)

        if question_number > 5:
            congratulation_statement = "Congratulations".format(question_number)

            self.question_number_label.configure(text=congratulation_statement)
            self.question_number_label.config(fg="#660000", font="Arial 24 bold",
                                       text=congratulation_statement)


            



    def reveal_answer(self, buttonID):

        # get question
        # self.question_text.get()

        # Button ID Config...
        if buttonID == 1:
            user_ans = self.answer_button_1['text']
            button_selected = self.answer_button_1
        elif buttonID == 2:
            user_ans = self.answer_button_2['text']
            button_selected = self.answer_button_2
        elif buttonID == 3:
            user_ans = self.answer_button_3['text']
            button_selected = self.answer_button_3
        else:
            user_ans = self.answer_button_4['text']
            button_selected = self.answer_button_4


        # get correct answer
        correct = self.answer_true.get()

        #get score
        score = self.score.get()

        if user_ans == correct:
            user_correct_ans_text = "You chose {}, That was correct!".format(correct)
            self.correct_incorrect_text.config(text=user_correct_ans_text)

            button_selected.config(bg="#43cc81")

            self.answer_button_1.config(state=DISABLED)
            self.answer_button_2.config(state=DISABLED)
            self.answer_button_3.config(state=DISABLED)
            self.answer_button_4.config(state=DISABLED)

            self.next_button.config(state=NORMAL)

            score += 1
            self.score.set(score)

            print("You chose", correct, ",", "That was correct!".format(user_correct_ans_text))
        else:
            user_incorrect_ans_text = "You chose {}, the correct answer was {}".format(user_ans, correct)
            self.correct_incorrect_text.config(text=user_incorrect_ans_text)
        
            button_selected.config(bg="#ff6666")

            self.answer_button_1.config(state=DISABLED)
            self.answer_button_2.config(state=DISABLED)
            self.answer_button_3.config(state=DISABLED)
            self.answer_button_4.config(state=DISABLED)

            self.next_button.config(state=NORMAL)

            
            print("You chose", user_ans, ",", "the correct answer was", correct.format(user_incorrect_ans_text))

        # Add quiz results to statistics list
    #     quiz_summary = "Question {}: {} | {}".format()
        
      
    # def to_quiz_results(self, quiz_results):
    #     Results(self, quiz_results)

    def to_quit(self):
        root.destroy()

        



# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("The Ultimate Greek God Quiz")
    something = Main(root)
    root.mainloop()



