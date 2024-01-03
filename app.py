import streamlit as st
# st.title('')
st.markdown("<h1 style='text-align: center; color: grey;'>CGPA CALCULATOR</h1>", unsafe_allow_html=True)
with st.columns(3)[1]:
     st.image("CGPA.png")
semester = ['I','II','III','IV','V','VI','VII','VIII']
credit = {
    1:20.5,
    2:20.5,
    3:24.5,
    4:23.5,
    5:23,
    6:23.5,
    7:15,
    8:15.5
}

semester_choosen = st.selectbox('Select Semester',semester)
number_of_subjects = st.number_input('Enter Number of Subjects (including theory, practical and sodeca)')
total_grade_credit = 0
final_answer = 0
number_of_subjects = int(number_of_subjects)
for i in range(number_of_subjects):
    with st.form(f"form_{i}"):
        st.write(f"Subject {i + 1}:")
        grade = ['A++','A+','A','B+','B','C+','C','D+','D','E+','E']
        grade = st.selectbox('Select the Grade',grade)
        credits = [0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0]
        subject_credit = st.selectbox('Enter the Subject Credit',credits)
        grade_score = {
            'A++':10,
            'A+':9,
            'A':8.5,
            'B+':8.0,
            'B':7.5,
            'C+':7.0,
            'C':6.5,
            'D+':6.0,
            'D':5.5,
            'E+':5.0,
            'E':4.0
        }
        g_score = grade_score[grade]
        total_grade_credit += (g_score*subject_credit)
        st.form_submit_button("Submit")



col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button('Calculate CGPA')
if center_button:
    if total_grade_credit > 0:
        try:
            idx = semester.index(semester_choosen)
            final_answer = (total_grade_credit) / credit[idx+1]
            st.success(f'CGPA is: {final_answer}')
            if final_answer >= 9.0:
                with st.columns(3)[1]:
                    st.image("pat.jpeg") 
            elif final_answer >= 8.0 and final_answer < 9.0:
                with st.columns(3)[1]:
                    st.image("8.0.jpg")
            elif final_answer >=7.0 and final_answer < 8.0:
                with st.columns(3)[1]:
                    st.image("OIP.jpeg") 
        except ValueError:
                st.error('!!! Shi Shi Daal Credit and Grade !!! ')
    else:
        st.warning('!!!!!!! Kuch Bhul Gya H re Tu !!!!!!!!')

       