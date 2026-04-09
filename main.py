import tkinter as tk

# =========================
# DONNÉES DU QUIZ
# =========================

quiz_data = {
    "Maths": [
        {
            "question": "Combien font 2 + 2 ?",
            "choices": ["3", "4", "5"],
            "answer": "4"
        },
        {
            "question": "Combien font 5 x 3 ?",
            "choices": ["15", "10", "8"],
            "answer": "15"
        },
        {
            "question": "Combien font 12 - 7 ?",
            "choices": ["6", "5", "4"],
            "answer": "5"
        }
    ],
    "Français": [
        {
            "question": "Quel est le verbe dans la phrase : 'Je mange une pomme' ?",
            "choices": ["Je", "mange", "pomme"],
            "answer": "mange"
        },
        {
            "question": "Quel mot est un adjectif ?",
            "choices": ["courir", "bleu", "chien"],
            "answer": "bleu"
        },
        {
            "question": "Combien y a-t-il de syllabes dans 'ordinateur' ?",
            "choices": ["3", "4", "5"],
            "answer": "4"
        }
    ],
    "Histoire": [
        {
            "question": "En quelle année commence la Révolution française ?",
            "choices": ["1789", "1815", "1492"],
            "answer": "1789"
        },
        {
            "question": "Qui était le roi de France en 1789 ?",
            "choices": ["Louis XIV", "Louis XVI", "Napoléon"],
            "answer": "Louis XVI"
        },
        {
            "question": "Quel monument se trouve à Paris ?",
            "choices": ["Le Colisée", "La tour Eiffel", "Big Ben"],
            "answer": "La tour Eiffel"
        }
    ]
}

# =========================
# VARIABLES GLOBALES
# =========================

selected_subject = None
current_question_index = 0
score = 0

# =========================
# FENÊTRE
# =========================

root = tk.Tk()
root.title("FocusFlow Seconde")
root.geometry("760x540")
root.configure(bg="#0f172a")
root.resizable(False, False)

# =========================
# STYLES
# =========================

BG_MAIN = "#0f172a"
BG_CARD = "#1e293b"
FG_MAIN = "#f8fafc"
FG_SUB = "#cbd5e1"
ACCENT = "#38bdf8"
GOOD = "#22c55e"
BAD = "#ef4444"
BTN = "#334155"
BTN_HOVER = "#475569"

title_font = ("Arial", 24, "bold")
subtitle_font = ("Arial", 13)
text_font = ("Arial", 15)
button_font = ("Arial", 13, "bold")
small_font = ("Arial", 11)

# =========================
# FONCTIONS UTILITAIRES
# =========================

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()

def create_title(text):
    label = tk.Label(
        main_frame,
        text=text,
        font=title_font,
        fg=FG_MAIN,
        bg=BG_CARD
    )
    label.pack(pady=(25, 10))
    return label

def create_subtitle(text):
    label = tk.Label(
        main_frame,
        text=text,
        font=subtitle_font,
        fg=FG_SUB,
        bg=BG_CARD,
        wraplength=620,
        justify="center"
    )
    label.pack(pady=(0, 20))
    return label

def create_button(text, command, bg=BTN, fg=FG_MAIN, width=22):
    button = tk.Button(
        main_frame,
        text=text,
        command=command,
        font=button_font,
        bg=bg,
        fg=fg,
        activebackground=ACCENT,
        activeforeground=BG_MAIN,
        relief="flat",
        bd=0,
        width=width,
        padx=10,
        pady=10,
        cursor="hand2"
    )
    button.pack(pady=8)
    return button

# =========================
# ÉCRANS
# =========================

def show_home():
    clear_frame()

    create_title("FocusFlow Seconde")
    create_subtitle(
        "Une appli simple pour réviser avec un mini quiz, "
        "gagner des points et rester motivée."
    )

    emoji = tk.Label(
        main_frame,
        text="📚⏱️✨",
        font=("Arial", 28),
        fg=ACCENT,
        bg=BG_CARD
    )
    emoji.pack(pady=(0, 20))

    create_button("Commencer", show_subjects, bg=ACCENT, fg=BG_MAIN, width=18)

    info = tk.Label(
        main_frame,
        text="Projet Python avec interface graphique",
        font=small_font,
        fg=FG_SUB,
        bg=BG_CARD
    )
    info.pack(pady=(25, 0))

def show_subjects():
    clear_frame()

    create_title("Choisis une matière")
    create_subtitle("Sélectionne une matière pour lancer ton quiz.")

    create_button("Maths", lambda: start_quiz("Maths"))
    create_button("Français", lambda: start_quiz("Français"))
    create_button("Histoire", lambda: start_quiz("Histoire"))

    create_button("Retour accueil", show_home, bg="#64748b", width=18)

def start_quiz(subject):
    global selected_subject, current_question_index, score
    selected_subject = subject
    current_question_index = 0
    score = 0
    show_question()

def show_question():
    clear_frame()

    questions = quiz_data[selected_subject]
    question_data = questions[current_question_index]

    progress = tk.Label(
        main_frame,
        text=f"Matière : {selected_subject}   |   Question {current_question_index + 1}/{len(questions)}   |   Score : {score}",
        font=small_font,
        fg=ACCENT,
        bg=BG_CARD
    )
    progress.pack(pady=(20, 10))

    question_label = tk.Label(
        main_frame,
        text=question_data["question"],
        font=("Arial", 18, "bold"),
        fg=FG_MAIN,
        bg=BG_CARD,
        wraplength=620,
        justify="center"
    )
    question_label.pack(pady=(20, 25))

    for choice in question_data["choices"]:
        choice_button = tk.Button(
            main_frame,
            text=choice,
            command=lambda c=choice: check_answer(c),
            font=button_font,
            bg=BTN,
            fg=FG_MAIN,
            activebackground=ACCENT,
            activeforeground=BG_MAIN,
            relief="flat",
            bd=0,
            width=24,
            padx=10,
            pady=10,
            cursor="hand2"
        )
        choice_button.pack(pady=8)

def check_answer(choice):
    global score

    correct_answer = quiz_data[selected_subject][current_question_index]["answer"]

    if choice == correct_answer:
        score += 1
        show_feedback(True, correct_answer)
    else:
        show_feedback(False, correct_answer)

def show_feedback(is_correct, correct_answer):
    clear_frame()

    if is_correct:
        color = GOOD
        message = "✅ Bonne réponse !"
        detail = "Bravo, tu gagnes 1 point."
    else:
        color = BAD
        message = "❌ Mauvaise réponse"
        detail = f"La bonne réponse était : {correct_answer}"

    feedback_label = tk.Label(
        main_frame,
        text=message,
        font=("Arial", 22, "bold"),
        fg=color,
        bg=BG_CARD
    )
    feedback_label.pack(pady=(50, 15))

    detail_label = tk.Label(
        main_frame,
        text=detail,
        font=text_font,
        fg=FG_MAIN,
        bg=BG_CARD,
        wraplength=620,
        justify="center"
    )
    detail_label.pack(pady=(0, 20))

    score_label = tk.Label(
        main_frame,
        text=f"Score actuel : {score}",
        font=subtitle_font,
        fg=FG_SUB,
        bg=BG_CARD
    )
    score_label.pack(pady=(0, 25))

    create_button("Question suivante", next_question, bg=ACCENT, fg=BG_MAIN, width=20)

def next_question():
    global current_question_index
    current_question_index += 1

    if current_question_index < len(quiz_data[selected_subject]):
        show_question()
    else:
        show_result()

def show_result():
    clear_frame()

    total_questions = len(quiz_data[selected_subject])

    if score == total_questions:
        final_message = "🏆 Incroyable ! Sans faute !"
        color = GOOD
    elif score >= 2:
        final_message = "🎉 Très bon travail !"
        color = ACCENT
    else:
        final_message = "💪 Continue, tu vas progresser !"
        color = "#f59e0b"

    create_title("Quiz terminé")

    result_label = tk.Label(
        main_frame,
        text=f"Tu as obtenu {score} / {total_questions}",
        font=("Arial", 20, "bold"),
        fg=FG_MAIN,
        bg=BG_CARD
    )
    result_label.pack(pady=(10, 15))

    message_label = tk.Label(
        main_frame,
        text=final_message,
        font=("Arial", 18, "bold"),
        fg=color,
        bg=BG_CARD
    )
    message_label.pack(pady=(0, 20))

    motivation = tk.Label(
        main_frame,
        text="La régularité vaut souvent plus que le talent.",
        font=subtitle_font,
        fg=FG_SUB,
        bg=BG_CARD
    )
    motivation.pack(pady=(0, 25))

    create_button("Recommencer", show_subjects, bg=ACCENT, fg=BG_MAIN, width=18)
    create_button("Retour accueil", show_home, bg="#64748b", width=18)

# =========================
# STRUCTURE PRINCIPALE
# =========================

outer_frame = tk.Frame(root, bg=BG_MAIN)
outer_frame.pack(fill="both", expand=True, padx=30, pady=30)

main_frame = tk.Frame(
    outer_frame,
    bg=BG_CARD,
    highlightbackground="#334155",
    highlightthickness=2
)
main_frame.pack(fill="both", expand=True)

# =========================
# LANCEMENT
# =========================

show_home()
root.mainloop()