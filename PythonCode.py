department_map = {

    # Cardiology Department - Handles heart-related symptoms
    'chest pain': 'Cardiology',
    'shortness of breath': 'Cardiology',
    'palpitations': 'Cardiology',
    'swelling in legs': 'Cardiology',
    'dizziness': 'Cardiology',
    'fatigue with exertion': 'Cardiology',

    # Dermatology Department - Skin, hair, and nail related symptoms
    'rashes': 'Dermatology',
    'itching': 'Dermatology',
    'skin lesions': 'Dermatology',
    'acne': 'Dermatology',
    'hair loss': 'Dermatology',
    'nail changes': 'Dermatology',
    'rash with infection': 'Dermatology',

    # Gastroenterology - Digestive system-related problems
    'abdominal pain': 'Gastroenterology',
    'nausea': 'Gastroenterology',
    'vomiting': 'Gastroenterology',
    'diarrhea': 'Gastroenterology',
    'constipation': 'Gastroenterology',
    'heartburn': 'Gastroenterology',
    'bloating': 'Gastroenterology',
    'jaundice': 'Gastroenterology',
    'rectal bleeding': 'Gastroenterology',

    # Neurology - Brain, nerves, and nervous system symptoms
    'headaches': 'Neurology',
    'migraines': 'Neurology',
    'vertigo': 'Neurology',
    'numbness': 'Neurology',
    'tingling': 'Neurology',
    'weakness': 'Neurology',
    'seizures': 'Neurology',
    'tremors': 'Neurology',
    'memory loss': 'Neurology',
    'speech difficulties': 'Neurology',
    'balance problems': 'Neurology',

    # Orthopedics - Bones, joints, and muscular issues
    'joint pain': 'Orthopedics',
    'muscle pain': 'Orthopedics',
    'swelling of joints': 'Orthopedics',
    'limited range of motion': 'Orthopedics',
    'fractures': 'Orthopedics',
    'ligament tears': 'Orthopedics',
    'back pain': 'Orthopedics',
    'neck pain': 'Orthopedics',

    # Pulmonology - Lung and respiratory conditions
    'cough': 'Pulmonology',
    'wheezing': 'Pulmonology',
    'chest tightness': 'Pulmonology',
    'chronic bronchitis': 'Pulmonology',
    'asthma attacks': 'Pulmonology',
    'cough with infection': 'Pulmonology',

    # Endocrinology - Hormone-related symptoms like thyroid or diabetes
    'unexplained weight changes': 'Endocrinology',
    'increased thirst': 'Endocrinology',
    'frequent urination': 'Endocrinology',
    'mood changes': 'Endocrinology',
    'hair changes': 'Endocrinology',
    'heat intolerance': 'Endocrinology',
    'cold intolerance': 'Endocrinology',
    'tremors': 'Endocrinology',

    # Nephrology - Kidney and urinary related complaints
    'swelling of face': 'Nephrology',
    'swelling of hands': 'Nephrology',
    'swelling of feet': 'Nephrology',
    'changes in urination': 'Nephrology',
    'loss of appetite': 'Nephrology',
    'muscle cramps': 'Nephrology',
    'general itching': 'Nephrology',

    # General Medicine - General body symptoms not specific to any one department
    'fatigue': 'General Medicine',
    'weakness': 'General Medicine',
    'body pain': 'General Medicine',
    'general discomfort': 'General Medicine',
    'fever': 'General Medicine',
    'chills': 'General Medicine',
    'swollen lymph nodes': 'General Medicine'
}


# Function that runs the chatbot interaction
def chatbot():
    print("\n")
    print("      WELCOME TO THE MEDICAL SYMPTOM ANALYSIS CHATBOT!".center(70))
    print("\nDescribe your symptoms, and I'll suggest the best department to consult.")
    print("Type 'exit' to end the conversation.\n")

    while True:
        user_input = input("You: ").lower() 

        if user_input == "exit":
            print("Chatbot: Thank you! Stay healthy.\n")
            break  

        department_count = {}

        # Check for known symptoms in the user's input and track which department they belong to
        for symptom, department in department_map.items():
            if symptom in user_input:
                department_count[department] = department_count.get(department, 0) + 1

        
        if department_count:
            # Find the department with the highest symptom count
            best_department = max(department_count, key=department_count.get)
            print(f"Chatbot: Based on your symptoms, please consult the {best_department} department.\n")
        else:
            # If no matching symptom found, suggest seeing a General Physician
            print("Chatbot: I'm unable to determine the department. Please provide more details or consult a General Physician.\n")


# Program execution starts here
if __name__ == "__main__":
    chatbot()
