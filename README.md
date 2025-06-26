---

# Flashcard App 🧠

A simple and effective language learning app built using Python and Tkinter. It helps users memorize French words through interactive flashcards with an auto-flip timer and progress tracking.

---

## Features 📚

* **Flashcard Learning**: Displays a French word and flips after 3 seconds to show the English translation.
* **Smart Progress Tracking**: Correctly answered words are removed from future sessions.
* **CSV Storage**: Tracks progress by updating a `words_to_learn.csv` file.
* **Minimal UI**: Clean interface with buttons for correct and incorrect answers.
* **Random Word Selection**: Words are picked randomly from a custom dictionary.

---

## Requirements 🛠️

* Python 3.6+
* Pandas library (`pip install pandas`)
* Tkinter (usually pre-installed with Python)

---

## Files Included 📂

1. **`main.py`** – Main application file with all logic and GUI setup
2. **`french_words.csv`** – Default vocabulary dataset (French to English)
3. **`words_to_learn.csv`** – Auto-generated file storing user progress
4. **`card_front.png`** – Flashcard front image (French word side)
5. **`card_back.png`** – Flashcard back image (English word side)
6. **`right.png`** – Checkmark button image for correct answers
7. **`wrong.png`** – Cross button image for incorrect answers

---

## How to Run? 🖥️

1. Clone this repository or download the ZIP:

   ```bash
   git clone https://github.com/AbdulRehmanMarfani/flashcard-app.git
   cd flashcard-app
   ```

2. Install required libraries:

   ```bash
   pip install pandas
   ```

3. Run the app:

   ```bash
   python main.py
   ```

---

## How It Works 🧩

* The app starts by showing a French word.
* After 3 seconds, the card flips to show the English meaning.
* Click ✅ if you got it right – the word is removed from future sessions.
* Click ❌ if you got it wrong – the word stays in rotation.
* Your progress is saved in `words_to_learn.csv`, so you can continue next time where you left off.

---

## Future Improvements 🚀

* Add score counter / progress bar
* Support for multiple languages
* Dark mode toggle
* Reverse mode (English → French)

---

## Credits ✨

* **Programming**: Abdul Rehman Marfani
* **Data Handling**: Pandas
* **GUI Framework**: Tkinter
* **Images & Word List**: From the 100 Days of Code Python course

---

Enjoy learning! 🇫🇷📖
Feel free to fork or contribute to make it even better!

---

