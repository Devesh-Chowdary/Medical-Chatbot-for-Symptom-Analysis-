# Medical Chatbot for Symptom Analysis

This project is a Python-based Medical Chatbot designed to interact with users, understand their symptoms, and recommend the appropriate medical department (e.g., Cardiology, Dermatology, Neurology) to consult.

## Features

* Symptom-to-department mapping using prompt-based logic.
* Interactive chatbot interface via the console.
* Can run on Google Colab, VSCode, or Jupyter Notebook.
* Guides users to the right specialist based on symptom descriptions.

## Tools & Technologies

* Python 3.x
* Prompt-based logic for reasoning

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Devesh-Chowdary/medical-chatbot-symptom-analysis.git
cd medical-chatbot-symptom-analysis
```

2. Run the chatbot script:

```bash
python chatbot.py
```

3. Interact with the chatbot via the console. Type 'exit' to end the session.

## Sample Input/Output

```
Welcome to the Medical Symptom Analysis Chatbot!
Describe your symptoms, and I'll suggest which department to consult.
Type 'exit' to end the conversation.

You: I have chest pain since morning
Chatbot: Based on your symptoms, please consult the Cardiology department.

You: I am getting some skin rash on my hands
Chatbot: Based on your symptoms, please consult the Dermatology department.

You: I have slight fever and cough
Chatbot: Based on your symptoms, please consult the General Medicine department.

You: exit
Chatbot: Thank you! Stay healthy.
```

## Future Enhancements

* Expand the symptom database.
* Integrate NLP for better understanding.
* Deploy using IBM Watson Assistant or cloud platforms.
* Add multilingual support.

## License

This project is for educational and academic demonstration purposes.
