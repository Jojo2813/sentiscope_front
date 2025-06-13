def visualize_input_importance(text, contrib_dict, top_positive, top_negative, base_size=16, scale=40):
    words = text.split()
    n = len(words)
    highlighted_text = ""
    i = 0

    while i < n:
        word = words[i]
        unigram = word.lower().strip(".,!?")
        bigram = ""
        contrib = 0
        color = "black"
        token_key = unigram

        # Try bigram if next word exists
        if i < n - 1:
            next_word = words[i + 1]
            bigram = f"{unigram} {next_word.lower().strip('.,!?')}"
            if bigram in contrib_dict:
                token_key = bigram
                contrib = contrib_dict[bigram]
                if bigram in top_positive:
                    color = "green"
                elif bigram in top_negative:
                    color = "red"
                else:
                    color = "grey"
                display = f"{word} {next_word}"
                i += 2  # Skip next word
            else:
                contrib = contrib_dict.get(unigram, 0)
                if unigram in top_positive:
                    color = "green"
                elif unigram in top_negative:
                    color = "red"
                else:
                    color = "grey"
                display = word
                i += 1
        else:
            contrib = contrib_dict.get(unigram, 0)
            if unigram in top_positive:
                color = "green"
            elif unigram in top_negative:
                color = "red"
            else:
                color = "grey"
            display = word
            i += 1

        size = base_size + min(abs(contrib) * scale, scale)
        size = round(size, 1)
        highlighted_text += f'<span style="font-size:{size}px; color:{color}">{display}</span> '

    return f"<p>{highlighted_text.strip()}</p>"
