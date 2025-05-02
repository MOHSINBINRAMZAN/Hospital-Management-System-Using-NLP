

# 🏥 Hospital Management System using Regex and NLP

This project is a smart **Hospital Management System (HMS)** that leverages **Natural Language Processing (NLP)** and **Regular Expressions (Regex)** to improve administrative workflows, patient interaction, and data extraction. The system is designed to efficiently manage patient records, appointments, staff details, and more, while offering intelligent text-based processing features.

## 🚀 Features

* ✅ **Patient Record Management**: Add, search, update, and delete patient information.
* 📅 **Appointment Scheduling**: Book, view, and cancel doctor appointments.
* 🧠 **NLP Integration**: Extract relevant information from unstructured text like doctor notes or patient feedback using libraries such as spaCy or NLTK.
* 🔍 **Regex Matching**: Clean and validate input data such as emails, phone numbers, and ID formats.
* 📄 **Text-Based Search**: Find patient or staff details using flexible keyword searches.
* 🔐 **Authentication System**: Admin/staff login for secure data access.
* 📊 **Reports Generation**: Summarize patient visits and staff schedules.

## 🛠️ Tech Stack

* **Backend**: Python
* **NLP Libraries**: spaCy / NLTK
* **Regex**: Python `re` module
* **Database**: SQLite / MySQL
* **Frontend (Optional)**: Flask / Django (if web-based), or CLI-based interface

## 📂 Folder Structure

```
hospital-management-system/
├── data/                   # Database or sample text files
├── models/                 # NLP models or custom logic
├── regex_utils.py          # Regex validation and cleaning functions
├── nlp_utils.py            # NLP processing functions
├── main.py                 # Entry point for the system
├── requirements.txt
└── README.md
```

## 💡 Sample Use Cases

* **Extract Diagnosis from Text**: Automatically tag and summarize symptoms from doctor notes.
* **Validate Patient Details**: Use regex to ensure correct formats for emails and phone numbers.
* **Free-text Search**: Search for patient history using natural language queries like "show patients with diabetes from last 6 months".

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/hospital-management-system.git
cd hospital-management-system
pip install -r requirements.txt
python main.py
```

## 🧪 Example Regex Patterns

```python
# Email validation
re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Phone number validation (e.g., US format)
re.match(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", phone)

# Extract age from sentence
re.findall(r'\b\d{1,3}\s?(?:years?|yrs?)\b', text)
```

## 📌 Future Enhancements

* Integrate voice-to-text for doctor dictation
* Use advanced transformers (e.g., BERT) for better NLP accuracy
* Add a web interface with user dashboards
* Implement role-based access control

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


