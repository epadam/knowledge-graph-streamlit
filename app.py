import streamlit as st

st.title('Knowledge Graph Overview')


st.header('1. Structure of Knowledge Graph')

st.subheader('Triple Store')
st.image('kg.png', use_column_width=True)
st.subheader('Open Knowledge Graph')
st.selectbox('', ('DBpedia', 'Freebase', 'Wikidata'))

st.header('2. Knowlege Graph Database')

st.write('Neo4j')


st.header('3. Building Knowledge Graph')

st.subheader('Automatic Knowledge Graph Construction')

st.write('Knowledge graph can be used to train language models like Bert, then use the trained model to buld the build the knowledge graph from structured or unstructured data')



st.header('4. Knowledge Graph Applications')

st.subheader('Knowledge Representation Learning')

st.write('Knowledge Graph Embedding')



st.subheader('Knowledge Graph and Machine Learning')

st.subheader('Knowledge Graph with Language Models')

st.image('jaket.png',caption='JAKET: Joint Pre-training of Knowledge Graph and Language Understanding')

st.subheader('Graph Convolutional Network with Knowledge Graph')

st.subheader('Knowledge Graph Compensation')







st.header('4. Real World Examples')

st.subheader('Q&A Chatbot')

st.subheader('Web and Social Media Monitoring')

st.subheader('Recommendation')

st.subheader('Knowledge Graph for Banking')

st.subheader('Knowledge Graph for Biology and Medicine')



st.header('5. Knowledge Graph Resources')

