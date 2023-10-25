def format_text(inp):
    text = f"""Given a target sentence construct the underlying meaning as a single function with attributes and attribute values. 

## TARGET SENTENCE: {inp["target"]}

## FUNCTION: {inp["meaning_representation"]}"""

    return text