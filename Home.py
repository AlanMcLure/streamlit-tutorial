import streamlit as st

st.title("🎨 Hub de Proyectos")
st.write("Explora los proyectos disponibles y selecciona uno para más detalles:")

# División en columnas para organizar las tarjetas
col1, col2 = st.columns(2)

# Proyecto 1
with col1:
    st.image("assets/images/proyecto_1.png", use_container_width=True)
    st.subheader("📊 Mapa de Tiros")
    st.write("Visualización interactiva de disparos en un campo de fútbol.")
    # if st.button("Explorar Proyecto 1"):
    #     st.query_params(page="Mapa_de_Tiros")
    #     st.rerun()  # Redirige inmediatamente a la nueva página

# # Proyecto 2
# with col2:
#     # st.image("assets/images/proyecto_2.png", use_container_width=True)
#     st.subheader("📁 Proyecto 2")
#     st.write("Descripción breve del segundo proyecto.")
#     if st.button("Explorar Proyecto 2"):
#         st.query_params(page="Proyecto_2")
#         st.rerun()

# # Proyecto 3
# with col3:
#     # st.image("assets/images/proyecto_3.png", use_container_width=True)
#     st.subheader("🖼 Proyecto 3")
#     st.write("Descripción breve del tercer proyecto.")
#     if st.button("Explorar Proyecto 3"):
#         st.query_params(page="Proyecto_3")
#         st.rerun()
