import textstat

def analyze_content(text: str) -> dict:
    """Analyze content for readability, complexity, and structure metrics."""
    
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    words = text.split()
    
    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    
    long_sentences = [s for s in sentences if len(s.split()) > 25]
    
    passive_indicators = ['was', 'were', 'been', 'being', 'is', 'are', 'by']
    passive_count = sum(1 for word in words if word.lower() in passive_indicators)
    
    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "avg_sentence_length": round(avg_sentence_length, 2),
        "flesch_reading_ease": round(textstat.flesch_reading_ease(text), 2),
        "flesch_kincaid_grade": round(textstat.flesch_kincaid_grade(text), 2),
        "readability_score": round(textstat.text_standard(text, float_output=True), 2),
        "long_sentences_count": len(long_sentences),
        "passive_voice_count": passive_count,
        "long_sentences": long_sentences
    }