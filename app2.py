# streamlit run  "app.py"

import streamlit as st
import pandas as pd
import pickle as pkl




st.title('Data Scientist Job Change Prediction')

st.image("https://i.ibb.co/wynpxvD/career-change.jpg")

df = pd.DataFrame({'What is Churn':['Churn is'],'What can we do':'you can do'})
st.write(df)


x = st.metric('Sales',2500,-12)

city = st.selectbox('What is Your city',('city_103', 'city_40', 'city_21', 'city_115', 'city_162',
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

city_development_index = st.slider('Enter Your city_development_index',0.1,0.1,0.9)
st.write('You Choose',city_development_index)

gender = st.radio('Gender',('Male','Female','Other'))

relevent_experience = st.radio('Are There relevent_experience',('Has relevent experience', 'No relevent experience'))

enrolled_university = st.radio('Are There enrolled_university',('no_enrollment', 'Full time course','Part time course'))

education_level = st.radio('Is There education_level',('Graduate', 'Masters', 'High School', 'Phd', 'Primary School'))

major_discipline = st.selectbox('What is Your major_discipline Status',('STEM', 'Business Degree', 'Arts', 'Humanities', 'No Major',
       'Other'))

experience = st.slider('Enter Your experience',1,20)
st.write('You Choose',experience)

company_size = st.selectbox('company_size Type',('50-99', '<10', '10000+', '5000-9999', '1000-4999', '10/49',
       '100-500', '500-999'))

if company_size == '50-99':
    st.write('You Choose',74.5)

company_type = st.selectbox('company Type',('Pvt Ltd', 'Funded Startup', 'Early Stage Startup', 'Other',
       'Public Sector', 'NGO'))

last_new_job = st.selectbox(' last_new_job Type',('1', '>4', 'never', '4', '3', '2',))


training_hours = st.slider('Enter Your training_hours',1,300)
st.write('You Choose',training_hours)

target = st.radio('Is There target',(0,1))

data = pd.DataFrame({'city': [city],'city_development_index': [city_development_index],'gender': [gender],'relevent_experience': [relevent_experience],'enrolled_university':[enrolled_university],'education_level':[education_level],'major_discipline':[major_discipline],'experience':[experience],'company_size':[company_size],'company_type':[company_type],'last_new_job':[last_new_job],'training_hours':[training_hours]})

        
data['last_new_job'] = data['last_new_job'].replace('>4','5').replace('never','0')
data['last_new_job'] = pd.to_numeric(data['last_new_job'])
data['company_size'] = data['company_size'].replace('50-99',(50+99)/2).replace('100-500',(100+500)/2).replace('10/49',(10+49)/2).replace('500-999',(999+500)/2).replace('1000-4999',(1000+4999)/2).replace('100-500',(100+500)/2).replace('5000-9999',(5000+9999)/2).replace('+10000',(10000)).replace('<10',9)
data['city_numeric'] = pd.to_numeric(data['city'].str.split('_').str[1])

data = pd.get_dummies(data=data, columns=['gender', 'relevent_experience','company_type','major_discipline','enrolled_university'])
                      



education_dict = {'Primary School' : 0,
                  'High School' : 1,
                  'Graduate' : 2,
                  'Masters' : 3,
                  'Phd' : 4}
# For Reversing the keys and vlues of the dictionary to retrive the encoded values using copmrehension for loop
rev_education_dict = {value: key for key, value in education_dict.items()}
data['education_level'] = data['education_level'].map(education_dict)
data.drop(['city'],axis=1,inplace=True)


col = ['city_development_index', 'education_level', 'experience',
       'company_size', 'last_new_job', 'training_hours', 'gender_Female',
       'gender_Male', 'gender_Other',
       'relevent_experience_Has relevent experience',
       'relevent_experience_No relevent experience', 'company_type_1',
       'company_type_Early Stage Startup', 'company_type_Funded Startup',
       'company_type_NGO', 'company_type_Other', 'company_type_Public Sector',
       'company_type_Pvt Ltd', 'major_discipline_Arts',
       'major_discipline_Business Degree', 'major_discipline_Humanities',
       'major_discipline_No Major', 'major_discipline_Other',
       'major_discipline_STEM', 'enrolled_university_Full time course',
       'enrolled_university_Part time course',
       'enrolled_university_no_enrollment']
data = pd.get_dummies(data=data).reindex(columns=col,fill_value=0)


st.write(data)

model = pkl.load(open('Rmodel.pkl', 'rb'))

churn_prop = model.predict_proba(data)[0][1] * 100
st.markdown(f'## Probability of a Candidate to Take the Data Science Job is : {round(churn_prop, 2)} %')

st.write(data['last_new_job'])
st.write(data['company_size'])

st.write(data)

st.markdown(f'# Thanks For Using Our Application')