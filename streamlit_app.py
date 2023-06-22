import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multislect("Pick some fruits:", list(my_freuit_list.index))
streamlit.dataframe(my_fruit_list)
