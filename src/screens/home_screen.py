import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home

def home_screen():
    style_background_home()
    style_base_layout()
    header_home()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
            <div style="margin-bottom: 1.5rem;">
                <p style="
                    font-size: 0.68rem;
                    font-weight: 600;
                    letter-spacing: 2.5px;
                    color: #6366F1 !important;
                    text-transform: uppercase;
                    margin: 0 0 10px 0;
                ">For Students</p>
                <h3 style="
                    font-size: 1.25rem;
                    font-weight: 700;
                    color: #E2E8F0 !important;
                    margin: 0 0 8px 0;
                ">Student Portal</h3>
                <p style="
                    color: #64748B !important;
                    font-size: 0.82rem;
                    margin: 0;
                    line-height: 1.6;
                ">Mark your attendance using face recognition. View records and enrolled subjects.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(
            'Continue as Student',
            type='primary',
            use_container_width=True,
            key='student_btn'
        ):
            st.session_state['login_type'] = 'student'
            st.rerun()

    with col2:
        st.markdown("""
            <div style="margin-bottom: 1.5rem;">
                <p style="
                    font-size: 0.68rem;
                    font-weight: 600;
                    letter-spacing: 2.5px;
                    color: #6366F1 !important;
                    text-transform: uppercase;
                    margin: 0 0 10px 0;
                ">For Teachers</p>
                <h3 style="
                    font-size: 1.25rem;
                    font-weight: 700;
                    color: #E2E8F0 !important;
                    margin: 0 0 8px 0;
                ">Teacher Portal</h3>
                <p style="
                    color: #64748B !important;
                    font-size: 0.82rem;
                    margin: 0;
                    line-height: 1.6;
                ">Manage classes, record attendance, and monitor student attendance.</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(
            'Continue as Teacher',
            type='primary',
            use_container_width=True,
            key='teacher_btn'
        ):
            st.session_state['login_type'] = 'teacher'
            st.rerun()

    footer_home()