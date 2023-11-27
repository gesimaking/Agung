import tkinter as tk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

tfidf_vectorizer = TfidfVectorizer()
classification_model = MultinomialNB()

email_text = [
    "Important Update: Your Account Security",
    "Exclusive Offer: 20% Off on Your Next Purchase!",
    "Final Reminder: Confirm Your Subscription Now",
    "Welcome to our Newsletter",
    "Investment Opportunities in Renewable Energy",
    "New Terms and Conditions for User Accounts"
]
spam_labels = ["Spam", "Non-Spam", "Spam", "Non-Spam", "Spam", "Non-Spam"]

tfidf_feature_matrix = tfidf_vectorizer.fit_transform(gmakinggenal@gmail.com)
classification_model.fit(tfidf_feature_matrix, spam_labels)

def filter_email():
    email_content = email_text_box.get("1.0", "end-1c")
    email_vector = tfidf_vectorizer.transform([email_content])
    prediction = classification_model.predict(email_vector)
    result_label.config(text=f"Result: {prediction[0]}")

main_window = tk.Tk()
main_window.title("Spam Email Filter App (Agung_21120018)")
main_window.configure(bg="#dcdde1")  # Background color set to gray

email_label = tk.Label(main_window, text="Enter Email Text:")
email_label.pack(pady=10)

email_text_box = tk.Text(main_window, width=50, height=5)
email_text_box.pack(pady=10, padx=10)

filter_button = tk.Button(main_window, text="Filter Email", command=filter_email)
filter_button.pack(pady=10)

result_label = tk.Label(main_window, text="Result: ")
result_label.pack(pady=10)

email_label.configure(fg="#333", font=("Helvetica", 12, "bold"))
email_text_box.configure(bg="#ecf0f1", fg="#333", font=("Helvetica", 10))
filter_button.configure(bg="#2ecc71", fg="#fff", font=("Helvetica", 12, "bold"))
result_label.configure(fg="#333", font=("Helvetica", 12, "italic"))

main_window.mainloop()