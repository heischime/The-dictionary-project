import tkinter as tk
from tkinter import ttk
# Define a dictionary with words in 5 different languages
words_dict = {
    "hello": {
        "English": "Hello",
        "Spanish": "Hola",
        "French": "Bonjour",
        "German": "Hallo",
        "Italian": "Ciao"
    },
    "goodbye": {
        "English": "Goodbye",
        "Spanish": "Adios",
        "French": "Au revoir",
        "German": "Tschuss",
        "Italian": "Addio"
    },
    "cat": {
        "English": "cat",
        "Spanish": "Gato",
        "French": "Chat",
        "German": "Katze",
        "Italian": "Gatto"
    },
    "apple": {
        "English": "Apple",
        "Spanish": "Manzana",
        "French": "Eau",
        "German": "Danke",
        "Italian": "Acqua"
    },
    "thank you": {
        "English": "Thank you",
        "Spanish": "Gracias",
        "French": "Merci",
        "German": "Danke",
        "Italian": "Grazie"
    },
    "please": {
        "English": "Please",
        "Spanish": "Por favor",
        "French": "S'il vous plait",
        "German": "Bitte",
        "Italian": "Per favore"
    },
    "yes": {
        "English": "Yes",
        "Spanish": "Si",
        "French": "Non",
        "German": "Gut",
        "Italian": "Buono"
    },
    "bad": {
        "English": "Bad",
        "Spanish": "Malo",
        "French": "Mauvais",
        "German": "Schlecht",
        "Italian": "Cattivo"
    },
    "friend": {
        "English": "Friend",
        "Spanish": "Amigo",
        "French": "Ami",
        "German": "Freud",
        "Italian": "Amico"
    },
    "family": {
        "English": "Family",
        "Spanish": "Familia",
        "French": "Maison",
        "German": "Hausa",
        "Italian": "Casa"
    },
    "car": {
        "English": "car",
        "Spanish": "Coche",
        "French": "Voiture",
        "German": "Auto",
        "Italian": "Auto"
    },
     "sun": {
         "English": "sun",
         "Spanish": "sol",
         "French" : "Soleil",
         "German" : "Sonne",
         "Italian": "Sole"
     },
     "moon": {
         "English": "Moon",
         "Spanish": "Luna",
         "French": "Lune",
         "German": "Mond",
         "Italian": "Luna"
     },
     "star": {
         "English": "Star",
         "Spanish": "Estrella",
         "French": "Etoile",
         "German": "Stern",
         "Italian": "Stella"
     },
     "dog": {
         "English": "Dog",
         "Spanish": "Gato",
         "French": "Chat",
         "German": "Katze",
         "Italian": "Gatto"
     },
     "water": {
         "English": "Water",
         "Spanish": "Agua",
         "French": "Eau",
         "German": "Wasser",
         "Italian": "Acqua"
     },
     "Good": {
         "English": "Good",
         "Spanish": "Bueno",
         "French": "Bon",
         "German": "Gut",
         "Italian": "Buono"
     },
     "No": {
         "English": "No",
         "Spanish": "No",
         "French": "Non",
         "German": "Nein",
         "Italian": "No"
     },
     "Tree": {
         "English": "Star",
         "Spanish": "Estrella",
         "French": "Etolie",
         "German": "Stern",
         "Italian": "Stella"
     },
     "Book": {
         "English": "Book",
         "Spanish": "Libro",
         "French": "Livre",
         "German": "Buch",
         "Italian": "Libro"
     }
}

# Create the main window
root = tk.Tk()
root.title("Language Translator")

# Function to update the displayed words based on selected language
def update_words(language):
    text_output.delete(1.0, tk.END) # Clear current text
    words = words_dict.get(language, {})
    for english_word, translated_word in words.items():
        text_output.insert(tk.END, f"{english_word}: translated_word\n")

# Create and place widgets on the window

# Label for the title
label_title = tk.Label(root, text="Choose a language", font=("Arial", 16))
label_title.pack(pady=10)

# Dropdown menu to select a language
language_combobox = ttk.Combobox(root, values= list(words_dict.keys()), width=20)
language_combobox.set("Select Language") #Set default text
language_combobox.pack(pady=10)

#Button to trigger language selection
button_select = tk.Button(root, text="Show words", command=lambda: update_words(language_combobox.get()))
button_select.pack(pady=10)

# Text box to display the words and their translations
text_output = tk.Text(root, height=15, width=50)
text_output.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()