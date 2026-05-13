def clean_text(text: str) -> str:
    """Remove extra whitespace and normalize line breaks."""
    lines = [line.strip() for line in text.strip().splitlines()]
    return "\n".join(line for line in lines if line)


def truncate_text(text: str, max_words: int = 500) -> str:
    """Truncate text to a maximum number of words."""
    words = text.split()
    if len(words) <= max_words:
        return text
    return " ".join(words[:max_words]) + "..."


def word_frequency(text: str) -> dict:
    """Return top 10 most frequent meaningful words."""
    stopwords = {"the", "a", "an", "and", "or", "but", "in", "on", "at",
                 "to", "for", "of", "with", "is", "are", "was", "were",
                 "it", "this", "that", "be", "as", "by", "from", "have"}

    words = [w.lower().strip(".,!?;:") for w in text.split()]
    words = [w for w in words if w and w not in stopwords]

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_freq[:10])


def count_paragraphs(text: str) -> int:
    """Count number of paragraphs in text."""
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    return len(paragraphs)


def estimate_read_time(text: str) -> str:
    """Estimate reading time based on average 200 words per minute."""
    word_count = len(text.split())
    minutes = word_count / 200
    if minutes < 1:
        return "Less than 1 minute"
    return f"{round(minutes)} minute(s)"