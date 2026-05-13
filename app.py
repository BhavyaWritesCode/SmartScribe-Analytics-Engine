import streamlit as st
from modules.analyzer import analyze_content
from modules.improver import improve_content
from modules.structure import generate_structure
from modules.xml_generator import generate_dita_xml
from modules.insights import generate_insights
from utils.helpers import clean_text, estimate_read_time, word_frequency, count_paragraphs

def load_css(file_path: str):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("assets/style.css")

st.set_page_config(
    page_title="SmartScribe Analytics Engine",
    page_icon="docs",
    layout="wide"
)

st.title("SmartScribe Analytics Engine")
st.caption("AI-powered content intelligence, optimization and structured documentation platform")

st.divider()

# --- Sidebar ---
with st.sidebar:
    st.header("Settings")
    persona = st.selectbox(
        "Target Audience",
        ["Engineer", "End Customer", "Sales"],
        help="AI will adjust tone and structure based on selected audience"
    )
    topic_type = st.selectbox(
        "DITA Topic Type",
        ["task", "concept", "reference"],
        help="Select the type of DITA XML output"
    )
    st.divider()
    st.markdown("**Workflow Stage**")
    stage = st.radio(
        "Current Stage",
        ["Draft", "Review", "Publish"],
        help="Simulate content pipeline stage"
    )

st.divider()

# --- Input ---
st.subheader("Input Content")
raw_text = st.text_area(
    "Paste your raw content here",
    height=200,
    placeholder="Enter your documentation, instructions, or any unstructured text..."
)

run = st.button("Analyze and Optimize", type="primary", use_container_width=True)

if run:
    if not raw_text.strip():
        st.warning("Please enter some content before running.")
    else:
        text = clean_text(raw_text)

        # --- Tabs ---
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "Content Analysis",
            "AI Improved Content",
            "Structured Output",
            "DITA XML",
            "Insights"
        ])

        # Tab 1 - Analysis
        with tab1:
            st.subheader("Content Analysis")
            analysis = analyze_content(text)

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Word Count", analysis["word_count"])
            col2.metric("Sentence Count", analysis["sentence_count"])
            col3.metric("Avg Sentence Length", analysis["avg_sentence_length"])
            col4.metric("Flesch Reading Ease", analysis["flesch_reading_ease"])

            col5, col6, col7, col8 = st.columns(4)
            col5.metric("FK Grade Level", analysis["flesch_kincaid_grade"])
            col6.metric("Readability Score", analysis["readability_score"])
            col7.metric("Long Sentences", analysis["long_sentences_count"])
            col8.metric("Passive Voice Count", analysis["passive_voice_count"])

            st.divider()
            col_left, col_right = st.columns(2)

            with col_left:
                st.markdown("**Read Time**")
                st.info(estimate_read_time(text))
                st.markdown("**Paragraph Count**")
                st.info(count_paragraphs(text))

            with col_right:
                st.markdown("**Top Keywords**")
                freq = word_frequency(text)
                for word, count in freq.items():
                    st.write(f"`{word}` — {count} times")

            if analysis["long_sentences"]:
                st.divider()
                st.markdown("**Long Sentences Detected**")
                for s in analysis["long_sentences"]:
                    st.warning(s)

        # Tab 2 - AI Improved Content
        with tab2:
            st.subheader(f"AI Improved Content — {persona} Persona")
            with st.spinner("Improving content with Groq AI..."):
                improved = improve_content(text, persona)
            st.text_area("Improved Content", value=improved, height=300)

            st.divider()
            st.markdown("**Improvement Analysis**")
            improved_analysis = analyze_content(improved)
            col1, col2 = st.columns(2)
            col1.metric(
                "Flesch Reading Ease",
                improved_analysis["flesch_reading_ease"],
                delta=round(improved_analysis["flesch_reading_ease"] - analysis["flesch_reading_ease"], 2)
            )
            col2.metric(
                "Avg Sentence Length",
                improved_analysis["avg_sentence_length"],
                delta=round(improved_analysis["avg_sentence_length"] - analysis["avg_sentence_length"], 2),
                delta_color="inverse"
            )

        # Tab 3 - Structured Output
        with tab3:
            st.subheader("Structured Content")
            with st.spinner("Generating structure..."):
                structure = generate_structure(text)

            st.markdown(f"**Title:** {structure['title']}")
            st.markdown(f"**Summary:** {structure['summary']}")

            st.markdown("**Steps:**")
            for i, step in enumerate(structure["steps"], 1):
                st.markdown(f"{i}. {step}")

            st.markdown(f"**Notes:** {structure['notes']}")

        # Tab 4 - DITA XML
        with tab4:
            st.subheader(f"DITA XML Output — {topic_type.capitalize()} Type")
            if "structure" not in dir():
                with st.spinner("Generating structure for XML..."):
                    structure = generate_structure(text)
            xml_output = generate_dita_xml(structure, topic_type)
            st.code(xml_output, language="xml")
            st.download_button(
                label="Download XML",
                data=xml_output,
                file_name=f"smartscribe_{topic_type}.xml",
                mime="text/xml"
            )

        # Tab 5 - Insights
        with tab5:
            st.subheader("Content Insights")
            if "analysis" not in dir():
                analysis = analyze_content(text)
            insights = generate_insights(analysis, text)

            col1, col2 = st.columns(2)
            col1.metric("Quality Score", f"{insights['quality_score']} / 100")
            col2.metric("Grade", insights["grade"])

            st.divider()
            st.markdown("**Suggestions**")
            for suggestion in insights["suggestions"]:
                st.write(suggestion)

            st.divider()
            st.markdown("**Workflow Stage**")
            stages = ["Draft", "Review", "Publish"]
            current_index = stages.index(stage)
            for i, s in enumerate(stages):
                if i < current_index:
                    st.success(f"[Completed] {s}")
                elif i == current_index:
                    st.info(f"[Current] {s}")
                else:
                    st.warning(f"[Pending] {s}")