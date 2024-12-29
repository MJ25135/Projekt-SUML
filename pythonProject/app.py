import streamlit as st

options = {
    'Male': True,
    'Female': False,
    'Rural': True,
    'Urban': False,
    'Yes': True,
    'No': False,
}

answers =[]
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
travel = st.select_slider('How long do you travel to school?',
                          {'faster than 15 min': 1, '15 - 30 min': 2, '30 min - 1 hour': 3,
                           'longer than 1 hour': 4})
answers.append(travel)
study = st.select_slider('How long do you study on your own each week?',
                         {'less than 2 hours': 1, '2 - 5 hours': 2, '5 - 10 hours': 3,
                          'more than 10 hours': 4})
answers.append(study)
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
family_rel = st.select_slider('How would you describe your relation with your family?',
                              {'Very bad': 1, 'Bad': 2, 'Not good nor bad': 3,
                               'Good': 4, 'Very Good': 5})
answers.append(family_rel)
free_time = st.select_slider('How much free time do you have after school?',
                             {'Very little': 1, 'A little': 2, 'Average amount': 3,
                              'High amount': 4, 'A lot': 5})
answers.append(free_time)
friends = st.select_slider('How often dou you go out with your friends?',
                           {'Very little': 1, 'A little': 2, 'Average amount': 3,
                            'High amount': 4, 'A lot': 5})
answers.append(friends)
week_alcohol = st.select_slider('How often do you drink alcohol during the working days?',
                                {'None': 1, 'Minimal': 2, 'Moderately': 3,
                                 'Frequently': 4, 'Excessively': 5})
answers.append(week_alcohol)
weekend_alcohol = st.select_slider('How often do you drink alcohol during the weekend?',
                                   {'None': 1, 'Minimal': 2, 'Moderately': 3,
                                    'Frequently': 4, 'Excessively': 5})
answers.append(weekend_alcohol)
health = st.select_slider('How would you describe your health?',
                          {'Poor': 1, 'Fair': 2, 'Good': 3, 'Very Good': 4, 'Excellent': 5})
answers.append(health)
grade1 = st.slider('What was your grade in first year', 0, 20)
answers.append(grade1)
grade2 = st.slider('What was your grade in second year', 0, 20)
answers.append(grade2)

if st.button("Complete"):
    st.write(answers)



