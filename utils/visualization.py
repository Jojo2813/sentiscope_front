def visualize_input_importance(text, vectorizer, model, clean_text, base_size=16, scale=40, top_n=2):
    """
    Creates a string to highlight the most important words in the user input based on model contribution.
    """
    def build_html_from_contributions(text, contrib_dict, top_positive, top_negative, base_size=16, scale=40):
    words = text.split()
    highlighted_text = ""
    for word in words:
        clean_word = word.lower().strip(".,!?")
        contrib = contrib_dict.get(clean_word, 0)
        size = base_size + min(abs(contrib) * scale, scale)
        size = round(size, 1)
        color = (
            "green" if clean_word in top_positive
            else "red" if clean_word in top_negative
            else "grey"
        )
        highlighted_text += f'<span style="font-size:{size}px; color:{color}">{word}</span> '
    return f"<p>{highlighted_text.strip()}</p>"
