import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #1E1E2E !important;
            }
            .stApp div[data-testid="stColumn"] {
                background: #2A2A3E !important;
                padding: 2.5rem !important;
                border-radius: 0.875rem !important;
                border: 1px solid #3D3D5C !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #1E1E2E !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

        /* Hide Streamlit chrome */
        #MainMenu, footer, header { visibility: hidden; }

        html, body, p, span, label, div {
            font-family: 'Inter', sans-serif !important;
        }

        .block-container {
            padding-top: 2.5rem !important;
            max-width: 900px !important;
        }

        /* Headings */
        h1, h2, h3, h4 {
            font-family: 'Inter', sans-serif !important;
            font-weight: 700 !important;
            color: #E2E8F0 !important;
            margin-bottom: 0 !important;
        }

        /* Body text */
        p {
            font-family: 'Inter', sans-serif !important;
            font-size: 0.875rem !important;
            line-height: 1.6 !important;
            color: #94A3B8 !important;
        }

        /* Labels */
        label, .stTextInput label, [data-testid="stWidgetLabel"] p {
            color: #CBD5E1 !important;
            font-size: 0.82rem !important;
            font-weight: 500 !important;
        }

        /* Primary Button — blue accent */
        button[kind="primary"] {
            font-family: 'Inter', sans-serif !important;
            font-weight: 600 !important;
            font-size: 0.875rem !important;
            background: #4F86F7 !important;
            color: #FFFFFF !important;
            border: none !important;
            border-radius: 0.5rem !important;
            padding: 0.6rem 1.4rem !important;
            transition: background 0.2s ease, transform 0.15s ease !important;
            letter-spacing: 0.01em !important;
        }

        button[kind="primary"]:hover {
            background: #3B74E8 !important;
            transform: translateY(-1px) !important;
        }

        /* Secondary Button — outlined */
        button[kind="secondary"] {
            font-family: 'Inter', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.875rem !important;
            background: transparent !important;
            color: #CBD5E1 !important;
            border: 1.5px solid #3D3D5C !important;
            border-radius: 0.5rem !important;
            padding: 0.6rem 1.4rem !important;
            transition: all 0.2s ease !important;
        }

        button[kind="secondary"]:hover {
            border-color: #6366F1 !important;
            color: #E2E8F0 !important;
            background: #2A2A3E !important;
        }

        /* Tertiary Button */
        button[kind="tertiary"] {
            font-family: 'Inter', sans-serif !important;
            font-weight: 500 !important;
            font-size: 0.875rem !important;
            background: #2A2A3E !important;
            color: #94A3B8 !important;
            border: 1px solid #3D3D5C !important;
            border-radius: 0.5rem !important;
            padding: 0.6rem 1.4rem !important;
            transition: all 0.2s ease !important;
        }

        button[kind="tertiary"]:hover {
            background: #343452 !important;
            color: #CBD5E1 !important;
            border-color: #6366F1 !important;
        }

        /* Input fields */
        .stTextInput input,
        input[type="text"],
        input[type="password"] {
            font-family: 'Inter', sans-serif !important;
            background: #16213E !important;
            color: #E2E8F0 !important;
            border: 1.5px solid #3D3D5C !important;
            border-radius: 0.5rem !important;
            font-size: 0.875rem !important;
            caret-color: #4F86F7 !important;
            padding: 0.5rem 0.75rem !important;
        }

        .stTextInput input:focus,
        input[type="text"]:focus,
        input[type="password"]:focus {
            border-color: #4F86F7 !important;
            box-shadow: 0 0 0 3px rgba(79,134,247,0.15) !important;
            outline: none !important;
        }

        .stTextInput input::placeholder {
            color: #475569 !important;
        }

        /* Selectbox */
        [data-testid="stSelectbox"] > div > div {
            background: #16213E !important;
            color: #E2E8F0 !important;
            border: 1.5px solid #3D3D5C !important;
            border-radius: 0.5rem !important;
            font-size: 0.875rem !important;
        }

        /* Divider */
        hr {
            border-color: #3D3D5C !important;
            margin: 1.2rem 0 !important;
        }

        /* Containers */
        [data-testid="stVerticalBlockBorderWrapper"] {
            background: #2A2A3E !important;
            border: 1px solid #3D3D5C !important;
            border-radius: 0.75rem !important;
            padding: 0.5rem !important;
        }

        /* Dataframe */
        [data-testid="stDataFrame"] {
            border-radius: 0.75rem !important;
            overflow: hidden !important;
            border: 1px solid #3D3D5C !important;
        }

        /* Warning / Info / Error / Success boxes */
        [data-testid="stAlert"] {
            border-radius: 0.6rem !important;
            font-family: 'Inter', sans-serif !important;
            border: none !important;
        }

        .stAlert > div {
            background: #2A2A3E !important;
            color: #CBD5E1 !important;
        }

        /* Spinner text */
        [data-testid="stSpinner"] p {
            color: #94A3B8 !important;
        }

        /* Camera input */
        [data-testid="stCameraInput"] {
            border-radius: 0.75rem !important;
            overflow: hidden !important;
            border: 1px solid #3D3D5C !important;
        }

        /* Toast */
        [data-testid="stToast"] {
            background: #2A2A3E !important;
            color: #E2E8F0 !important;
            border: 1px solid #3D3D5C !important;
            border-radius: 0.6rem !important;
            font-family: 'Inter', sans-serif !important;
        }

        /* Dialog / Modal */
        [data-testid="stDialog"] > div {
            background: #252537 !important;
            border: 1px solid #3D3D5C !important;
            border-radius: 0.875rem !important;
        }

        [data-testid="stDialog"] h2 {
            color: #E2E8F0 !important;
        }

        /* Subheader */
        .stSubheader {
            color: #CBD5E1 !important;
        }

        /* File uploader */
        [data-testid="stFileUploader"] {
            background: #2A2A3E !important;
            border: 1px dashed #3D3D5C !important;
            border-radius: 0.75rem !important;
        }

        /* Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #1E1E2E;
        }
        ::-webkit-scrollbar-thumb {
            background: #3D3D5C;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #4F86F7;
        }
        </style>
    """, unsafe_allow_html=True)