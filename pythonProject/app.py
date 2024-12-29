import streamlit as st
from model import Model


def prepare_model(model):
    model.load_dataset()
    model.train()


options = {
    'Male': True,
    'Female': False,
    'Rural': True,
    'Urban': False,
    'Yes': True,
    'No': False,
}

ml_model = Model()
prepare_model(ml_model)

numerical_options = [1, 2, 3, 4, 5]
answers = []
st.title("Third year grade prediction")

gender = options[st.radio('Pick your gender', ['Male', 'Female'])]
answers.append(gender)
age = st.slider('How old are you?', 0, 99)
answers.append(age)
address = options[st.radio('Do you leave in urban or rural area?', ['Rural', 'Urban'])]
answers.append(address)
parents_status = options[st.radio('Does your parents live together?', ['Yes', 'No'])]
answers.append(parents_status)
absences = st.number_input('How many absences on average did you have on first and second year?', 0)
answers.append(absences)
travel_dict = {'faster than 15 min': 1, '15 - 30 min': 2, '30 min - 1 hour': 3,
               'longer than 1 hour': 4}
travel = st.select_slider('How long do you travel to school?',
                          ['faster than 15 min', '15 - 30 min', '30 min - 1 hour', 'longer than 1 hour'])

answers.append(travel_dict[travel])
study_dict = {'less than 2 hours': 1, '2 - 5 hours': 2, '5 - 10 hours': 3,
              'more than 10 hours': 4}
study = st.select_slider('How long do you study on your own each week?',
                         ['less than 2 hours', '2 - 5 hours', '5 - 10 hours', 'more than 10 hours'])
answers.append(study_dict[study])
school_help = options[st.radio('Do you have extra helping lessons at school?', ['Yes', 'No'])]
answers.append(school_help)
parents_help = options[st.radio('Do your parents help you with studying?', ['Yes', 'No'])]
answers.append(parents_help)
activities = options[st.radio('Do you have any activities outside of school?', ['Yes', 'No'])]
answers.append(activities)
tutoring = options[st.radio('Do you have outside of school lessons?', ['Yes', 'No'])]
answers.append(tutoring)
collage = options[st.radio('Are you planning to study at the University after finishing third year?', ['Yes', 'No'])]
answers.append(collage)
internet = options[st.radio('Do you have an Internet connection at home?', ['Yes', 'No'])]
answers.append(internet)
relationship = options[st.radio('Are you in a romantic relationship?', ['Yes', 'No'])]
answers.append(relationship)
family_rel_dict = {'Very bad': 1, 'Bad': 2, 'Not good nor bad': 3,
                   'Good': 4, 'Very Good': 5}
family_rel = st.select_slider('How would you describe your relation with your family?',
                              ['Very bad', 'Bad', 'Not good nor bad',
                               'Good', 'Very Good'])
answers.append(family_rel_dict[family_rel])
free_time_dict = {'Very little': 1, 'A little': 2, 'Average amount': 3,
                  'High amount': 4, 'A lot': 5}
free_time = st.select_slider('How much free time do you have after school?',
                             ['Very little', 'A little', 'Average amount',
                              'High amount', 'A lot'])
answers.append(free_time_dict[free_time])
friends_dict = {'Very little': 1, 'A little': 2, 'Average amount': 3,
                'High amount': 4, 'A lot': 5}
friends = st.select_slider('How often dou you go out with your friends?',
                           ['Very little', 'A little', 'Average amount',
                            'High amount', 'A lot'])
answers.append(friends_dict[friends])
alcohol_dict = {'None': 1, 'Minimal': 2, 'Moderately': 3,
                'Frequently': 4, 'Excessively': 5}
week_alcohol = st.select_slider('How often do you drink alcohol during the working days?',
                                ['None', 'Minimal', 'Moderately', 'Frequently', 'Excessively'])
answers.append(alcohol_dict[week_alcohol])
weekend_alcohol = st.select_slider('How often do you drink alcohol during the weekend?',
                                   ['None', 'Minimal', 'Moderately', 'Frequently', 'Excessively'])
answers.append(alcohol_dict[weekend_alcohol])
health_dict = {'Poor': 1, 'Fair': 2, 'Good': 3, 'Very Good': 4, 'Excellent': 5}
health = st.select_slider('How would you describe your health?',
                          ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent'])
answers.append(health_dict[health])
grade1 = st.slider('What was your grade in first year', 0, 20)
answers.append(grade1)
grade2 = st.slider('What was your grade in second year', 0, 20)
answers.append(grade2)

if st.button("Make prediction"):
    if not ml_model.trained:
        prepare_model(ml_model)
    input_values = [answers]
    prediction = round(float(ml_model.predict(input_values)))
    st.write(f"Predicted score: {prediction}")
