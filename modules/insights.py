def generate_insights(analysis: dict, text: str) -> dict:
    """Generate actionable insights and quality score from content analysis."""

    suggestions = []
    score = 100

    # Check average sentence length
    if analysis["avg_sentence_length"] > 20:
        suggestions.append("Sentences are too long — aim for under 20 words per sentence")
        score -= 15

    # Check long sentences count
    if analysis["long_sentences_count"] > 2:
        suggestions.append(f"Found {analysis['long_sentences_count']} long sentences — break them into shorter ones")
        score -= 10

    # Check readability score
    if analysis["flesch_reading_ease"] < 50:
        suggestions.append(" Low readability score — simplify vocabulary and sentence structure")
        score -= 15

    # Check passive voice
    if analysis["passive_voice_count"] > 5:
        suggestions.append(f"High passive voice usage ({analysis['passive_voice_count']} instances) — use active voice")
        score -= 10

    # Check word count
    if analysis["word_count"] < 50:
        suggestions.append("Content is too short — add more detail and context")
        score -= 10

    # Check for action verbs in steps
    action_verbs = ["click", "open", "select", "enter", "configure", "install",
                    "run", "create", "set", "update", "delete", "save", "copy"]
    words_lower = text.lower().split()
    has_action_verbs = any(verb in words_lower for verb in action_verbs)
    if not has_action_verbs:
        suggestions.append(" Missing action verbs — use clear action words like click, select, configure")
        score -= 10

    # Check for structure indicators
    structure_words = ["step", "first", "then", "next", "finally", "note", "warning"]
    has_structure = any(word in words_lower for word in structure_words)
    if not has_structure:
        suggestions.append(" Lacks structural clarity — add transition words like first, then, next")
        score -= 10

    # Positive feedback
    if analysis["flesch_reading_ease"] >= 60:
        suggestions.append("Good readability score")
    if analysis["avg_sentence_length"] <= 15:
        suggestions.append("Sentence length is well optimized")
    if has_action_verbs:
        suggestions.append("Good use of action verbs")

    return {
        "quality_score": max(score, 0),
        "suggestions": suggestions,
        "grade": _get_grade(max(score, 0))
    }


def _get_grade(score: int) -> str:
    if score >= 90:
        return "A — Excellent"
    elif score >= 75:
        return "B — Good"
    elif score >= 60:
        return "C — Average"
    elif score >= 40:
        return "D — Needs Improvement"
    else:
        return "F — Poor"