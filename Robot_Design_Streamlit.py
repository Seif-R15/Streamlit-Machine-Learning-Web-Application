# streamlit run  "Robot_Design_Streamlit.py"
import streamlit as st
import pandas as pd
import pickle as pkl

# Define a function to make a prediction with the pre-trained model
def predict(city,city_development_index, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, company_type, last_new_job, training_hours):
    # Load the pre-trained model
    model = pkl.load(open("Rmodel.pkl", "rb"))

    # Prepare the input data
    input_data = pd.DataFrame({
        'city':[city],
        'city_development_index': [city_development_index],
        'gender': [gender],
        'relevent_experience': [relevent_experience],
        'enrolled_university': [enrolled_university],
        'education_level': [education_level],
        'major_discipline': [major_discipline],
        'experience': [experience],
        'company_size':[company_size],
        'company_type':[company_type],
        'last_new_job':[last_new_job],
        'training_hours':[training_hours]
    })
    
    input_data['last_new_job'] = input_data['last_new_job'].replace('>4','5').replace('never','0')
    input_data['last_new_job'] = pd.to_numeric(input_data['last_new_job'])
    input_data['company_size'] = input_data['company_size'].replace('50-99',(50+99)/2).replace('100-500',(100+500)/2).replace('10/49',(10+49)/2).replace('500-  999',(999+500)/2).replace('1000-4999',(1000+4999)/2).replace('100-500',(100+500)/2).replace('5000-9999',(5000+9999)/2).replace('+10000',(10000)).replace('<10',9)

    input_data['city_numeric'] = pd.to_numeric(input_data['city'].str.split('_').str[1])


    input_data = pd.get_dummies(data=input_data, columns=['gender','relevent_experience','company_type','major_discipline','enrolled_university'])
                      



    education_dict = {'Primary School' : 0,
                      'High School' : 1,
                      'Graduate' : 2,
                      'Masters' : 3,
                      'Phd' : 4}
    
    # For Reversing the keys and vlues of the dictionary to retrive the encoded values using copmrehension for loop
    rev_education_dict = {value: key for key, value in education_dict.items()}

    input_data['education_level'] = input_data['education_level'].map(education_dict)

    input_data.drop(['city'],axis=1,inplace=True)
    
    col = ['city_development_index', 'education_level', 'experience',
           'company_size', 'last_new_job', 'training_hours', 'gender_Female',
           'gender_Male', 'gender_Other',
           'relevent_experience_Has relevent experience',
           'relevent_experience_No relevent experience', 'company_type_1.0',
           'company_type_Early Stage Startup', 'company_type_Funded Startup',
           'company_type_NGO', 'company_type_Other', 'company_type_Public Sector',
           'company_type_Pvt Ltd', 'major_discipline_Arts',
           'major_discipline_Business Degree', 'major_discipline_Humanities',
           'major_discipline_No Major', 'major_discipline_Other',
           'major_discipline_STEM', 'enrolled_university_Full time course',
           'enrolled_university_Part time course',
           'enrolled_university_no_enrollment']

    input_data = pd.get_dummies(data=input_data).reindex(columns=col,fill_value=0)
    
    # Make a prediction using the loaded model
    prediction = int(model.predict(input_data)[0])
    probability = model.predict_proba(input_data)[0][prediction]

    return prediction, probability

def main():
    st.set_page_config(page_title="ML App", page_icon=":robot_face:")
    st.title("ML App User Interface")
    
    city = st.sidebar.selectbox('What is Your city',('city_103', 'city_40', 'city_21', 'city_115', 'city_162',
       'city_176', 'city_160', 'city_46', 'city_61', 'city_114',
       'city_13', 'city_159', 'city_102', 'city_67', 'city_100',
       'city_16', 'city_71', 'city_104', 'city_64', 'city_101', 'city_83',
       'city_105', 'city_73', 'city_75', 'city_41', 'city_11', 'city_93',
       'city_90', 'city_36', 'city_20', 'city_57', 'city_152', 'city_19',
       'city_65', 'city_74', 'city_173', 'city_136', 'city_98', 'city_97',
       'city_50', 'city_138', 'city_82', 'city_157', 'city_89',
       'city_150', 'city_70', 'city_175', 'city_94', 'city_28', 'city_59',
       'city_165', 'city_145', 'city_142', 'city_26', 'city_12',
       'city_37', 'city_43', 'city_116', 'city_23', 'city_99', 'city_149',
       'city_10', 'city_45', 'city_80', 'city_128', 'city_158',
       'city_123', 'city_7', 'city_72', 'city_106', 'city_143', 'city_78',
       'city_109', 'city_24', 'city_134', 'city_48', 'city_144',
       'city_91', 'city_146', 'city_133', 'city_126', 'city_118',
       'city_9', 'city_167', 'city_27', 'city_84', 'city_54', 'city_39',
       'city_79', 'city_76', 'city_77', 'city_81', 'city_131', 'city_44',
       'city_117', 'city_155', 'city_33', 'city_141', 'city_127',
       'city_62', 'city_53', 'city_25', 'city_2', 'city_69', 'city_120',
       'city_111', 'city_30', 'city_1', 'city_140', 'city_179', 'city_55',
       'city_14', 'city_42', 'city_107', 'city_18', 'city_139',
       'city_180', 'city_166', 'city_121', 'city_129', 'city_8',
       'city_31', 'city_171'))
    
    
    st.sidebar.header("city_development_index")
    city_development_index = st.sidebar.slider('Enter Your city_development_index',0.1,0.1,2.2)
    def validate_city_development_index(city_development_index):
        try:
            city_development_index = float(city_development_index)
            if city_development_index < 0 or city_development_index > 1:
                raise ValueError("City development index must be between 0 and 1.")
        except ValueError:
            return "Invalid input. City development index must be a float between 0 and 1."

        return "Input validated successfully."
    if validate_city_development_index(city_development_index) == "Invalid input. City development index must be a float between 0 and 1.":
        st.sidebar.warning(validate_city_development_index(city_development_index))
    else:
        st.sidebar.success(validate_city_development_index(city_development_index))

    gender = st.sidebar.radio('Gender',('Male','Female','Other'))
    
    def validate_Gender(gender):
        try:
            if gender == 'Other'  :
                raise ValueError("No such Gender")
        except ValueError:
            return " No Such a Gender"

        return "Input validated successfully."
    if validate_Gender(gender) == " No Such a Gender":
        st.sidebar.warning(validate_Gender(gender))
    else:
        st.sidebar.success(validate_Gender(gender))

    relevent_experience = st.sidebar.radio('Are There relevent_experience',('Has relevent experience', 'No relevent experience'))

    enrolled_university = st.sidebar.radio('Are There enrolled_university',('no_enrollment', 'Full time course','Part time course'))

    education_level = st.sidebar.radio('Is There education_level',('Graduate', 'Masters', 'High School', 'Phd', 'Primary School'))

    major_discipline = st.sidebar.selectbox('What is Your major_discipline Status',('STEM', 'Business Degree', 'Arts', 'Humanities', 'No Major',
           'Other'))

    experience = st.sidebar.slider('Enter Your experience',1,20,key="experience_slider")
    st.sidebar.write('You Choose',experience)
    
    company_size = st.sidebar.selectbox('company_size Type',('50-99', '<10', '10000+', '5000-9999', '1000-4999', '10/49',
       '100-500', '500-999'))

    if company_size == '50-99':
        st.sidebar.write('You Choose',74.5)

    company_type = st.sidebar.selectbox('company Type',('Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other','Public Sector', 'NGO'))

    last_new_job = st.sidebar.selectbox(' last_new_job Type',('1', '>4', 'never', '4', '3', '2',))


    training_hours = st.sidebar.slider('Enter Your training_hours',1,300)
    st.sidebar.write('You Choose',training_hours)
    
    video_file = open('First_ML.mp4', 'rb')
    
    st.video(video_file)
    


    # Add slider widget
    age = st.slider('Select your age', 0, 100)

    # Add checkbox widget
    agree = st.checkbox('I agree to the terms and conditions')

    if st.button('Submit'):
        # Perform action based on widget inputs
        if agree:
            prediction, probability = predict(city,city_development_index, gender, relevent_experience, enrolled_university, education_level, major_discipline, experience, company_size, company_type, last_new_job, training_hours)
            st.write(f'Prediction: {prediction}')
            st.write(f'Probability: {probability}')
            st.write(f'Your age is: {age}')
            st.success('Thank you for submitting!')
        else:
            st.warning('Please agree to the terms and conditions')

if __name__ == "__main__":
    main()