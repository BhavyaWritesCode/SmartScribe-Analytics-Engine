try:
    # textstat is an optional dependency; if unavailable, fall back to simpler estimators
    import textstat
except Exception:
    # Catch ImportError and any other import-related issues
    textstat = None


def _fallback_flesch_reading_ease(text: str) -> float:
    sentences = [s for s in text.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    words = text.split()
    syllables = sum(max(1, len([c for c in w if c.lower() in 'aeiouy'])) for w in words)
    ASL = len(words) / len(sentences) if sentences else 0
    ASW = syllables / len(words) if words else 0
    return 206.835 - 1.015 * ASL - 84.6 * ASW


def _fallback_flesch_kincaid_grade(text: str) -> float:
    sentences = [s for s in text.replace('!', '.').replace('?', '.').split('.') if s.strip()]
    words = text.split()
    syllables = sum(max(1, len([c for c in w if c.lower() in 'aeiouy'])) for w in words)
    ASL = len(words) / len(sentences) if sentences else 0
    ASW = syllables / len(words) if words else 0
    return 0.39 * ASL + 11.8 * ASW - 15.59


def _fallback_text_standard(text: str, float_output: bool = True) -> float:
    fk = _fallback_flesch_kincaid_grade(text)
    if fk < 1:
        standard = 1
    elif fk < 3:
        standard = 2
    elif fk < 6:
        standard = 5
    elif fk < 9:
        standard = 8
    elif fk < 12:
        standard = 11
    else:
        standard = 14
    return float(standard) if float_output else standard


def analyze_content(text: str) -> dict:
    """Analyze content for readability, complexity, and structure metrics."""

    sentences = [s.strip() for s in text.split('.') if s.strip()]
    words = text.split()

    avg_sentence_length = len(words) / len(sentences) if sentences else 0
    long_sentences = [s for s in sentences if len(s.split()) > 25]

    passive_indicators = ['was', 'were', 'been', 'being', 'is', 'are', 'by']
    passive_count = sum(1 for word in words if word.lower() in passive_indicators)

    if textstat is not None:
        flesch = textstat.flesch_reading_ease(text)
        fk = textstat.flesch_kincaid_grade(text)
        standard = textstat.text_standard(text, float_output=True)
    else:
        flesch = _fallback_flesch_reading_ease(text)
        fk = _fallback_flesch_kincaid_grade(text)
        standard = _fallback_text_standard(text, float_output=True)

    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "avg_sentence_length": round(avg_sentence_length, 2),
        "flesch_reading_ease": round(flesch, 2),
        "flesch_kincaid_grade": round(fk, 2),
        "readability_score": round(standard, 2),
        "long_sentences_count": len(long_sentences),
        "passive_voice_count": passive_count,
        "long_sentences": long_sentences
    }