import streamlit as st

def header_home():
    st.markdown("""
        <div style="
            text-align: center;
            padding: 3rem 0 2rem 0;
        ">
            <div style="
                display: inline-block;
                background: #2A2A3E;
                color: #6366F1;
                font-size: 0.68rem;
                font-weight: 600;
                letter-spacing: 3px;
                text-transform: uppercase;
                padding: 6px 16px;
                border-radius: 20px;
                border: 1px solid #3D3D5C;
                margin-bottom: 20px;
            ">AI-Powered Attendance System</div>
            <h1 style="
                font-size: 3rem;
                font-weight: 800;
                color: #E2E8F0 !important;
                margin: 0 0 14px 0;
                letter-spacing: -1.5px;
                line-height: 1.1;
            ">Smart Attendance</h1>
            <p style="
                color: #64748B !important;
                font-size: 0.9rem;
                margin: 0;
                letter-spacing: 0.2px;
            ">Automated attendance tracking powered by facial recognition</p>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    st.markdown("""
        <div style="
            display: flex;
            align-items: center;
            gap: 10px;
            padding: 4px 0;
        ">
            <div style="
                width: 36px;
                height: 36px;
                background: #2A2A3E;
                border-radius: 8px;
                border: 1px solid #3D3D5C;
                display: flex;
                align-items: center;
                justify-content: center;
            ">
                <div style="
                    width: 10px;
                    height: 10px;
                    background: #4F86F7;
                    border-radius: 50%;
                "></div>
            </div>
            <div>
                <p style="
                    font-size: 0.92rem;
                    font-weight: 700;
                    color: #E2E8F0 !important;
                    margin: 0;
                    line-height: 1.2;
                ">Smart Attendance</p>
                <p style="
                    font-size: 0.68rem;
                    color: #4F86F7 !important;
                    margin: 1px 0 0 0;
                    line-height: 1;
                    letter-spacing: 0.5px;
                ">AI ATTENDANCE SYSTEM</p>
            </div>
        </div>
    """, unsafe_allow_html=True)