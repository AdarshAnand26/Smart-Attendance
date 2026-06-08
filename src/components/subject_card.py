import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    
    # Build stats HTML separately without f-string
    stats_html = ""
    if stats:
        stats_html += '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 4px;">'
        for icon, label, value in stats:
            stats_html += (
                '<div style="'
                'background: #16213E;'
                'border: 1px solid #3D3D5C;'
                'padding: 4px 12px;'
                'border-radius: 6px;'
                'font-size: 0.78rem;'
                'color: #CBD5E1;'
                '">'
                f'<b style="color: #E2E8F0;">{value}</b> {label}'
                '</div>'
            )
        stats_html += '</div>'

    html = (
        '<div style="'
        'background: #2A2A3E;'
        'border-left: 4px solid #4F86F7;'
        'padding: 20px 24px;'
        'border-radius: 0.75rem;'
        'border: 1px solid #3D3D5C;'
        'margin-bottom: 16px;'
        '">'
        f'<h3 style="margin: 0 0 8px 0; color: #E2E8F0; font-size: 1.05rem; font-weight: 700;">{name}</h3>'
        '<p style="color: #64748B; margin: 0 0 14px 0; font-size: 0.82rem;">'
        '<span style="'
        'background: #16213E;'
        'color: #4F86F7;'
        'padding: 2px 10px;'
        'border-radius: 4px;'
        'font-weight: 600;'
        'font-size: 0.78rem;'
        'border: 1px solid #3D3D5C;'
        f'">{code}</span>'
        '&nbsp;·&nbsp;'
        f'<span style="color: #94A3B8;">Section {section}</span>'
        '</p>'
        + stats_html +
        '</div>'
    )

    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()