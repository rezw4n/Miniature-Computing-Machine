import streamlit as st


st.set_page_config(page_title="Miniature Computing Machine",
                   page_icon="earth_asia",
                   layout='centered',
                   initial_sidebar_state='auto')

st.title('Miniature Computing Machine for the Humans of GEN, DU')

st.sidebar.subheader(
    'Department of Geography and Environment, University of Dhaka')

faculty = st.sidebar.radio(label="Faculty:", options=('Science', 'Arts'))
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


column_1, column_2 = st.beta_columns(2)

year = st.sidebar.selectbox(label="Academic Year:", options=(
        '1st Year', '2nd Year', '3rd Year', '4th Year'))

mark_dict = {'A+ | 4.00': 4,
             'A  | 3.75': 3.75,
             'A- | 3.50': 3.50,
             'B+ | 3.25': 3.25,
             'B  | 3.00': 3,
             'B- | 2.75': 2.75,
             'C+ | 2.50': 2.50,
             'C  | 2.25': 2.25,
             'D  | 2.00': 2,
             'F  | 0.00': 0}
marks = [key for key in mark_dict]


if year == '1st Year' and faculty == 'Science':
    courses = {'Introduction to Geography and Environment': 2, 'Region and World Regional Pattern': 2, 'Introduction to Physical Geography and Environment': 2, 'Introduction to Human Geography and Environment': 2, 'Fundamentals of Chemistry in Geography and Environment': 2,
               'Fundamentals of English Language': 2, 'Fundamentals of Cartography and Map Projection': 2, 'Introduction to Computer in Geography and Environment': 2, 'Topographic Surveying': 2, 'Introduction to Research and Field Studies': 2, 'Viva': 2, 'Geology': 4, 'Introduction to Soil': 4}

if year == '1st Year' and faculty == 'Arts':
    courses = {'Introduction to Geography and Environment': 2, 'Region and World Regional Pattern': 2, 'Introduction to Physical Geography and Environment': 2, 'Introduction to Human Geography and Environment': 2, 'Fundamentals of Chemistry in Geography and Environment': 2,
               'Fundamentals of English Language': 2, 'Fundamentals of Cartography and Map Projection': 2, 'Introduction to Computer in Geography and Environment': 2, 'Topographic Surveying': 2, 'Introduction to Research and Field Studies': 2, 'Viva': 2, 'Sociology Part I': 4, 'Introduction to Psychology': 4}

if year == '2nd Year' and faculty == 'Science':
    courses = {'Geography of Soils': 2, 'Biogeography': 2, 'Oceanography and Marine Environment': 2, 'Population Geography': 3, 'Economic Geography-I': 2, 'Cultural Geography': 3, 'Quantitative Techniques in Geography and Environment': 2,
               'Introduction to GIS and Computer Cartography': 2, 'Geomatic Surveying': 2, 'Remote Sensing-I: Fundamentals': 2, 'Research Methods and Field Study in Human Geography and Environment – I': 2, 'Viva Voce': 2, 'Geology II': 4, 'Soil, Water & Environment': 4, 'Ecology, Environment and Plants': 4}

if year == '2nd Year' and faculty == 'Arts':
    courses = {'Geography of Soils': 2, 'Biogeography': 2, 'Oceanography and Marine Environment': 2, 'Population Geography': 3, 'Economic Geography-I': 2, 'Cultural Geography': 3, 'Quantitative Techniques in Geography and Environment': 2,
               'Introduction to GIS and Computer Cartography': 2, 'Geomatic Surveying': 2, 'Remote Sensing-I: Fundamentals': 2, 'Research Methods and Field Study in Human Geography and Environment – I': 2, 'Viva Voce': 2, 'Sociology of Bangladesh': 4, 'Social Psychology': 4, 'International Relations / Economics': 4}

if year == '3rd Year':
    courses = {'Geographic Thoughts and Concept': 3, 'Geomorphology-1': 3, 'Climatology-I': 3, 'Rural Geography': 3, 'Geography of Natural Resources': 3,
               'Bangladesh: Physical Geography and Environment': 3, 'Bangladesh : Human Geography and Environment': 3, 'Quantitative Techniques in Geography and Environment-II': 3, 'Economic Geography-II': 2, 'GIS-II: Advanced Data Concepts in GIS': 2, 'Remote Sensing-II: Image Processing and Analysis': 2, 'Map Reading and Interpretation': 2, 'Research Methods and Field Survey in Physical Geography and Environment-II': 3, 'Viva': 2}

if year == '4th Year':
    courses = {'Geomorphology-II': 3, 'Climatology-II': 3, 'Political Geography': 3, 'Urban Geography': 3, 'Agricultural Geography': 3, 'Environmental Management': 3, 'Regional Geography and Environment of South Asia': 3, 'Transport Geography': 3,
               'Landuse Planning and Development': 3, 'GIS –III: Spatial Analysis and Modeling': 2, 'Remote Sensing –III: Thermal and Microwave Remote Sensing': 2, 'Techniques in Physical Geography': 2, 'Environmental Analysis': 2, 'Landuse Survey': 3, 'Viva': 2}

st.sidebar.text('\n')

st.sidebar.latex(
    r'''CGPA = \frac{\sum(Grades \times Credits)}{\sum Credits}''')

st.sidebar.text('\n')

if st.sidebar.checkbox(label="Show Course Name and Credits"):
    st.sidebar.write(courses)

course_marks = []
for index, course in enumerate(courses):
    if len(courses) % 2 == 1:
        if index < len(courses) // 2 + 1:
            mark = column_1.selectbox(label=course, options=(marks))
            course_marks.append(mark_dict.get(mark))
        else:
            mark = column_2.selectbox(label=course, options=(marks))
            course_marks.append(mark_dict.get(mark))
    else:
        if index < len(courses) // 2:
            mark = column_1.selectbox(label=course, options=(marks))
            course_marks.append(mark_dict.get(mark))
        else:
            mark = column_2.selectbox(label=course, options=(marks))
            course_marks.append(mark_dict.get(mark))

credit_hours = [value for value in courses.values()]


def calculate(credit_hours, course_marks):
    total_point = sum([credit_hours * course_marks for credit_hours,
                       course_marks in zip(credit_hours, course_marks)])
    return round(total_point / sum(credit_hours), 2)


st.markdown('---')

result = calculate(credit_hours, course_marks)
st.title(f"You CGPA for {year} is {result}")

st.markdown('---')

average_gpa = []
with st.beta_expander(label="Calculate Cumulative Grade Point Average", expanded=False):
    st.text('Enter Your GPA for Each Year')
    column_1, column_2, column_3, column_4 = st.beta_columns(4)
    with column_1:
        gpa = st.number_input(label='1st Year', min_value=0.00, max_value=4.00)
        average_gpa.append(gpa)
    with column_2:
        gpa = st.number_input(label='2nd Year', min_value=0.00, max_value=4.00)
        average_gpa.append(gpa)
    with column_3:
        gpa = st.number_input(label='3rd Year', min_value=0.00, max_value=4.00)
        average_gpa.append(gpa)
    with column_4:
        gpa = st.number_input(label='4th Year', min_value=0.00, max_value=4.00)
        average_gpa.append(gpa)
    average_gpa = [gpa for gpa in average_gpa if gpa != 0.00]
    if st.button('Calculate Average'):
        try:
            st.title(
                f"Your CGPA is {round(sum(average_gpa) / len(average_gpa), 2)}")
        except:
            st.warning('Please enter your CGPA first')

with st.beta_expander(label="About this website..."):
    st.markdown(
        """This website is created and maintained by [**Rezwan Ahmed**](mailto:rezwan490@gmail.com) for the undergraduate students of Department of Geography and Environment, University of Dhaka.  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. All the course titles and their information were collected from the [official website](http://geoenv.du.ac.bd/undergraduate-overview/).  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. If you want to contribute, feel free to open a [pull request!](https://github.com/rezw4n/miniature-computing-machine/pulls)  
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. If you find any bug on the website, or a mistake or want a new feature to be implemented please create an issue on [Github](https://github.com/rezw4n/miniature-computing-machine).""")
