import streamlit as st
from src.ui.base_layout import style_background_dashboard, style_base_layout
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from PIL import Image
import numpy as np
from src.pipelines.face_pipeline import predict_attendance, get_face_embeddings, train_classifier
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student, get_student_subjects, get_student_attendance, unenroll_student_to_subject
import time
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def student_dashboard():
    student_data = st.session_state.student_data
    student_id = student_data['student_id']

    # --- Top bar ---
    c1, c2 = st.columns([1, 1], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        col_a, col_b = st.columns([2, 1])
        with col_a:
            st.markdown(f"""
                <p style="
                    text-align: right;
                    font-size: 0.85rem;
                    font-weight: 600;
                    color: #E2E8F0 !important;
                    margin: 0;
                ">Welcome, {student_data['name']}</p>
            """, unsafe_allow_html=True)
        with col_b:
            if st.button("Logout", type='secondary', key='loginbackbtn',
                         use_container_width=True):
                st.session_state['is_logged_in'] = False
                del st.session_state.student_data
                st.session_state.show_registration = False
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Section header ---
    c1, c2 = st.columns([2, 1], vertical_alignment='center')
    with c1:
        st.markdown("""
            <h3 style="
                font-size: 1.1rem;
                font-weight: 700;
                color: #E2E8F0 !important;
                margin: 0;
            ">Enrolled Subjects</h3>
        """, unsafe_allow_html=True)
    with c2:
        if st.button('+ Enroll in Subject', type='primary',
                     use_container_width=True):
            enroll_dialog()

    st.divider()

    # --- Load data ---
    with st.spinner('Loading subjects...'):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendance(student_id)

    # --- Stats map ---
    stats_map = {}
    for log in logs:
        sid = log['subject_id']
        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}
        stats_map[sid]['total'] += 1
        if log.get('is_present'):
            stats_map[sid]['attended'] += 1

    # --- Subject cards ---
    if not subjects:
        st.markdown("""
            <div style="
                text-align: center;
                padding: 3rem;
                background: #2A2A3E;
                border: 1px solid #3D3D5C;
                border-radius: 0.75rem;
                margin-top: 1rem;
            ">
                <p style="color: #94A3B8 !important; margin: 0; font-size: 0.9rem;">
                    No subjects enrolled yet. Click <b>Enroll in Subject</b> to get started.
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        cols = st.columns(2)
        for i, sub_node in enumerate(subjects):
            sub = sub_node['subjects']
            sid = sub['subject_id']
            stats = stats_map.get(sid, {"total": 0, "attended": 0})

            def unenroll_button(s=sub, subject_id=sid):
                if st.button(
                    "Unenroll from this course",
                    key=f"unenroll_{subject_id}",
                    type='tertiary',
                    use_container_width=True,
                ):
                    unenroll_student_to_subject(student_id, subject_id)
                    st.toast(f"Unenrolled from {s['name']}.")
                    st.rerun()

            with cols[i % 2]:
                subject_card(
                    name=sub['name'],
                    code=sub['subject_code'],
                    section=sub['section'],
                    stats=[
                        ('·', 'Total Classes', stats['total']),
                        ('·', 'Attended', stats['attended']),
                    ],
                    footer_callback=unenroll_button
                )

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "student_data" in st.session_state:
        student_dashboard()
        return

    # ✅ Fix 1: Initialize session state for registration
    if 'show_registration' not in st.session_state:
        st.session_state.show_registration = False

    # ✅ Fix 2: Store photo in session state so it persists
    if 'captured_photo' not in st.session_state:
        st.session_state.captured_photo = None

    # --- Top bar ---
    c1, c2 = st.columns([1, 1], vertical_alignment='center')
    with c1:
        header_dashboard()
    with c2:
        st.markdown("<div style='display:flex; justify-content:flex-end;'>", unsafe_allow_html=True)
        if st.button("Back to Home", type='secondary', key='loginbackbtn'):
            st.session_state['login_type'] = None
            st.session_state.show_registration = False
            st.session_state.captured_photo = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- Login title ---
    st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="
                font-size: 1.6rem;
                font-weight: 700;
                color: #E2E8F0 !important;
                margin: 0 0 6px 0;
            ">Student Login</h2>
            <p style="color: #94A3B8 !important; font-size: 0.85rem; margin: 0;">
                Position your face in the camera to sign in
            </p>
        </div>
    """, unsafe_allow_html=True)

    photo_source = st.camera_input("", label_visibility="collapsed")

    if photo_source:
        # ✅ Fix 3: Save photo to session state
        st.session_state.captured_photo = photo_source
        img = np.array(Image.open(photo_source))

        with st.spinner('Scanning your face...'):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces == 0:
                st.warning('No face detected. Please try again.')
                st.session_state.show_registration = False

            elif num_faces > 1:
                st.warning('Multiple faces detected. Please ensure only one face is visible.')
                st.session_state.show_registration = False

            else:
                if detected:
                    student_id = list(detected.keys())[0]
                    all_students = get_all_students()
                    student = next(
                        (s for s in all_students if s['student_id'] == student_id), None
                    )
                    if student:
                        st.session_state.is_logged_in = True
                        st.session_state.user_role = 'student'
                        st.session_state.student_data = student
                        st.session_state.show_registration = False
                        st.session_state.captured_photo = None
                        st.toast(f"Welcome back, {student['name']}!")
                        time.sleep(1)
                        st.rerun()
                else:
                    # ✅ Fix 4: Set session state not local variable
                    st.info('Face not recognized. You may be a new student.')
                    st.session_state.show_registration = True

    # ✅ Fix 5: Use session state to show registration form
    if st.session_state.show_registration and st.session_state.captured_photo:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("""
            <h3 style="
                font-size: 1.1rem;
                font-weight: 700;
                color: #E2E8F0 !important;
                margin: 0 0 1rem 0;
            ">Create New Profile</h3>
        """, unsafe_allow_html=True)

        with st.container(border=True):
            new_name = st.text_input("Full Name", placeholder='e.g. Adarsh Kumar')

            st.markdown("""
                <p style="
                    font-size: 0.8rem;
                    font-weight: 600;
                    color: #CBD5E1 !important;
                    margin: 0.5rem 0 4px 0;
                ">Voice Enrollment
                <span style='color:#94A3B8; font-weight:400;'>(Optional)</span></p>
                <p style="color: #94A3B8 !important; font-size: 0.78rem; margin: 0 0 8px 0;">
                    Record a short phrase for voice-based attendance
                </p>
            """, unsafe_allow_html=True)

            audio_data = None
            try:
                audio_data = st.audio_input('Say: "I am present" or your full name')
            except Exception:
                st.error('Microphone not available.')

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button('Create Account', type='primary', use_container_width=True):
                if new_name:
                    with st.spinner('Creating your profile...'):
                        # ✅ Fix 6: Use session state photo not local variable
                        img = np.array(Image.open(st.session_state.captured_photo))
                        encodings = get_face_embeddings(img)
                        if encodings:
                            face_emb = encodings[0].tolist()
                            voice_emb = None
                            if audio_data:
                                voice_emb = get_voice_embedding(audio_data.read())
                            response_data = create_student(
                                new_name,
                                face_embedding=face_emb,
                                voice_embedding=voice_emb
                            )
                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in = True
                                st.session_state.user_role = 'student'
                                st.session_state.student_data = response_data[0]
                                st.session_state.show_registration = False
                                st.session_state.captured_photo = None
                                st.toast(f'Welcome, {new_name}! Profile created.')
                                time.sleep(1)
                                st.rerun()
                        else:
                            st.error('Could not capture facial features. Please retake the photo.')
                else:
                    st.warning('Please enter your full name.')

    footer_dashboard()