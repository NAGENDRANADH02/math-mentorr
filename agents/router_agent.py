def route_topic(parsed_output):
    if "calculus" in parsed_output.lower():
        return "calculus"
    if "probability" in parsed_output.lower():
        return "probability"
    if "matrix" in parsed_output.lower():
        return "linear_algebra"
    return "algebra"