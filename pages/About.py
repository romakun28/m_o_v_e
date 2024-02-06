import streamlit as st

st.header("About")

col1, col2 = st.columns(2)

with col1:
    st.image("images/ron.jpeg")
    st.write("Lorem ipsum dolor sit amet. Id cupiditate odio est animi illo ut galisum vitae est voluptatem suscipit "
             "non deleniti dolorem sed excepturi nihil eos facilis adipisci. Eos obcaecati laborum et ratione alias et "
             "deleniti molestias. Sit dolores libero eos quasi consequatur et molestiae internos aut tempora magni aut "
             "nemo totam? Ut voluptate illum et explicabo itaque ut repellat voluptatem ea fuga tempore ut perspiciatis "
             "voluptatem et rerum corrupti.")

with col2:
    st.image("images/luciano.jpeg")
    st.write("Lorem ipsum dolor sit amet. Id cupiditate odio est animi illo ut galisum vitae est voluptatem suscipit "
             "non deleniti dolorem sed excepturi nihil eos facilis adipisci. Eos obcaecati laborum et ratione alias et "
             "deleniti molestias. Sit dolores libero eos quasi consequatur et molestiae internos aut tempora magni aut "
             "nemo totam? Ut voluptate illum et explicabo itaque ut repellat voluptatem ea fuga tempore ut perspiciatis "
             "voluptatem et rerum corrupti.")