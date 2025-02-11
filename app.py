import joblib
import streamlit as st
import pandas as pd

# 0 = Dropout, 1 = Graduate, 2 = Enrolled

model_load = joblib.load('RF_model.pkl')

kolom_data = [
    'Marital_status',
    'Nacionality',
    'Displaced',
    'Educational_special_needs',
    'Debtor',
    'Tuition_fees_up_to_date',
    'Gender',
    'Scholarship_holder',
    'Age_at_enrollment',
    'International',
    'Curricular_units_1st_sem_credited',
    'Curricular_units_1st_sem_enrolled',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_credited',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Unemployment_rate',
    'Inflation_rate',
    'GDP'
]

def yesno_convert(option):
    """Converts 'Yes'/'No' to 1/0."""
    return 1 if option == 'Yes' else 0

def gender_convert(option):
    """Converts 'Man'/'Woman' to 1/0."""
    return 1 if option == 'Man' else 0

def marital_convert(option):
    """Converts marital status to corresponding integer values."""
    mapping = {
        'Single': 1,
        'Married': 2,
        'Widower': 3,
        'Divorced': 4,
        'Facto Union': 5,
        'Legally Separated': 6
    }
    return mapping.get(option, 0)  # Default to 0 if not found

def nationality_convert(option):
    """Converts nationality to corresponding categorical integer values."""
    mapping = {
        'Portugal': 1,
        'Jerman': 2,
        'Spanyol': 6,
        'Italia': 11,
        'Belanda': 13,
        'Inggris': 14,
        'Lituania': 17,
        'Angola': 21,
        'Kap Verde': 22,
        'Guinea': 24,
        'Mozambik': 25,
        'Sao Tomean': 26,
        'Turki': 32,
        'Brasil': 41,
        'Rumania': 62,
        'Moldova (Republik)': 100,
        'Meksiko': 101,
        'Ukraina': 103,
        'Rusia': 105,
        'Kuba': 108,
        'Kolombia': 109
    }
    return mapping.get(option, 0)  # Default to 0 if not found



if __name__=="__main__":

    # Judul web
    st.title('Jaya Jaya Institut')
    
    st.subheader('Pengenalan Jaya Jaya Institut',  divider='grey')
    st.markdown('''Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan internasional yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik dalam bidang pendidikan. Selain itu merupakan pendidikan perguruan internasional yang sudah menarik perhatian berbagai kalangan siswa, bahkan dari mancanegara.''')
    
    st.subheader('Apa fungsi Predict Machine di bawah ini?',  divider='grey')
    st.markdown('''Predict Machine adalah sebuah mesin model yang dibuat untuk
                prediksi. Mesin ini dibuat dan di _train_ berdasarkan data yang ada pada
                Jaya Jaya Institute.''')
    
    st.subheader('Bagaimana cara menggunakannya?',  divider='grey')
    st.markdown(' Dari data yang dimiliki, anda tinggal memasukkannya sesuai dengan format data yang ada, dan berikut ini merupakan beberapa inputan yang harus diisi, yaitu:')

    st.write('**Marital Status**: Status pernikahan (Single = Belum menikah, Married = Menikah, Widower = Janda/Duda, Divorced = Cerai, Facto Union = Pernikahan tidak resmi, Legally Separated = Perceraian resmi)')
    st.write('**Nacionality**: Negara asal (Portugal, Jerman, Spanyol, Italia, Belanda, Inggris, Lituania, Angola, Kap Verde, Guinea, Mozambik, Sao Tomean, Turki, Brasil, Rumania, Moldova-Republik, Meksiko, Ukraina, Rusia, Kuba, Kolombia)') 
    st.write('**Admission Grade**: Nilai masuk (0-200)')
    st.write('**Displaced**: Apakah siswa berasal dari keluarga kurang mampu?')
    st.write('**Educational Special Needs**: Apakah siswa memiliki kebutuhan khusus pendidikan?')
    st.write('**Debtor**: Apakah siswa memiliki tanggungan hutang?')
    st.write('**Tuition Fees**: Apakah siswa sudah melunasi pembayaran terkini?')
    st.write('**Scholarship Holder**: Apakah siswa mendapatkan beasiswa?')
    st.write('**Gender**: Jenis kelamin (Man = Laki-laki, Woman = Perempuan)')
    st.write('**Age At Enrollment**: Usia siswa saat melakukan enrollment')
    st.write('**International**: Apakah siswa berasal dari luar negeri?')
    st.write('**Unemployment Rate**: Tingkat pengangguran di daerah mahasiswa')
    st.write('**Inflation Rate**: Tingkat inflasi di daerah mahasiswa')
    st.write('**GDP (Gross Domestic Product**): Tingkat GDP di daerah mahasiswa')
    st.write('**Curriculum Unit**: Jumlah Curriculum yang dikreditkan, dienrollment, disetujui, dan nilainya. Baik pada semester 1 maupun semester 2')


    st.header('Predict Machine', divider='rainbow')

    # Marital Status
    st.subheader('Marital Status')
    Marital_status = marital_convert(st.selectbox('Pilih status pernikahan',
                                                    ['Single', 'Married', 'Widower', 'Divorced',
                                                    'Facto Union', 'Legally Separated'],
                                                    label_visibility='collapsed'))

    # Nacionality
    st.subheader('Nacionality')
    Nacionality = nationality_convert(st.selectbox('Pilih kewarganegaraan',
                            ['Portugal', 'Jerman', 'Spanyol', 'Italia', 'Belanda', 'Inggris', 
                                'Lituania', 'Angola', 'Kap Verde', 'Guinea', 'Mozambik', 'Sao Tomean', 
                                'Turki', 'Brasil', 'Rumania', 'Moldova (Republik)', 'Meksiko', 
                                'Ukraina', 'Rusia', 'Kuba', 'Kolombia'],
                            label_visibility='collapsed'))

    # Admission Grade
    st.subheader('Admission Grade')
    Admission_grade = st.number_input('Nilai Saat Pendaftaran', min_value=0.00, max_value=200.00, format="%.2f", value=0.00)

    # Displaced
    st.subheader('Displaced')
    Displaced = yesno_convert(st.radio('Displaced', ['Yes', 'No'], horizontal=True,
                                        label_visibility='collapsed'))

    # Educational Special Needs
    st.subheader('Educational Special Needs')
    Educational_special_needs = yesno_convert(st.radio('Kebutuhan khusus pendidikan', ['Yes', 'No'],
                                                        horizontal=True,
                                                        label_visibility='collapsed'))

    # Debtor
    st.subheader('Debtor')
    Debtor = yesno_convert(st.radio('Debtor', ['Yes', 'No'], horizontal=True,
                                    label_visibility='collapsed'))

    # Tuition Fees
    st.subheader('Tuition Fees')
    Tuition_fees_up_to_date = yesno_convert(st.radio('Tuition Fees Up To Date',
                                                        ['Yes', 'No'], horizontal=True,
                                                        label_visibility='collapsed'))

    # Scholarship Holder
    st.subheader('Scholarship Holder')
    Scholarship_holder = yesno_convert(st.radio('Scholarship Holder', ['Yes', 'No'],
                                                horizontal=True, label_visibility='collapsed'))

    # Gender
    st.subheader('Gender')
    Gender = gender_convert(st.selectbox('Pilih jenis kelamin',
                                        ['Man', 'Woman'],
                                        label_visibility='collapsed'))

    # Age At Enrollment
    st.subheader('Age At Enrollment')
    Age_at_enrollment = st.number_input('Umur saat enrollment', min_value=10, max_value=100)

    # International
    st.subheader('International')
    International = yesno_convert(st.radio('Internasional', ['Yes', 'No'], horizontal=True,
                                            label_visibility='collapsed'))

    # Unemployment Rate
    st.subheader('Unemployment Rate')
    Unemployment_rate = st.number_input('Tingkat pengangguran', min_value=-100.0, max_value=100.0, format="%.2f", value=0.00)

    # Inflation Rate
    st.subheader('Inflation Rate')
    Inflation_rate = st.number_input('Tingkat inflasi', min_value=-100.0, max_value=100.0, format="%.2f", value=0.00)

    # GDP
    st.subheader('GDP')
    GDP = st.number_input('PDB', min_value=-100.0, format="%.2f", value=0.00)

    # Curriculum Unit Credited
    st.subheader('Curriculum Unit')
    st.subheader('Curriculum Unit Credited')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_credited = st.number_input('1st Semester Credited')
    with col2:
        Curricular_units_2nd_sem_credited = st.number_input('2nd Semester Credited')

    st.subheader('Curriculum Unit Enrolled')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_enrolled = st.number_input('1st Semester Enrolled')
    with col2:
        Curricular_units_2nd_sem_enrolled = st.number_input('2nd Semester Enrolled')

    st.subheader('Curriculum Unit Approved')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_approved = st.number_input('1st Semester Approved')
    with col2:
        Curricular_units_2nd_sem_approved = st.number_input('2nd Semester Approved')

    st.subheader('Curriculum Unit Grade')
    col1, col2 = st.columns(2)
    with col1:
        Curricular_units_1st_sem_grade = st.number_input('1st Semester Grade')
    with col2:
        Curricular_units_2nd_sem_grade = st.number_input('2nd Semester Grade')

    # Create the feature list based on the input data
    new_data = [[Marital_status, Nacionality, Displaced, Educational_special_needs,
                    Debtor, Tuition_fees_up_to_date, Gender, Scholarship_holder, 
                    Age_at_enrollment, International,
                    Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled,
                    Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade,
                    Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled,
                    Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade,
                    Unemployment_rate, Inflation_rate, GDP]]

    if st.button('Predict'):
        # Convert the data into a DataFrame with proper columns
        new_data = pd.DataFrame(new_data, columns=kolom_data)
        
        # Make the prediction using the model
        result = model_load.predict(new_data)

        # Display result in a more visually appealing way
        if result[0] == 0:
            st.error('Siswa dropout', icon="🚨")  # Error with an icon
        else:
            st.balloons()  # Show balloons animation
            st.success('Siswa bukan dropout 🎉')  # Success message with emoji