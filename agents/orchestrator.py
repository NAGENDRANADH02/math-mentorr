from agents.parser_agent import parse_problem
from agents.solver_agent import solve
from agents.verifier_agent import verify
from agents.explainer_agent import explain

def run_pipeline(raw_input, retrieved_context, memory_hit=None):
    trace = []

    parsed = parse_problem(raw_input)
    trace.append("Parser Agent completed")

    if parsed["needs_clarification"]:
        return {"clarification": parsed["clarification_question"], "trace": trace}

    if memory_hit:
        trace.append("Memory reuse activated")
        solution = memory_hit["solution"]
        confidence = memory_hit["similarity"]
    else:
        solution = solve(parsed["problem_text"], retrieved_context)
        trace.append("Solver Agent completed")
        confidence = verify(solution)
        trace.append("Verifier Agent completed")

    explanation = explain(solution)
    trace.append("Explainer Agent completed")

    return {
        "solution": solution,
        "explanation": explanation,
        "confidence": confidence,
        "trace": trace,
        "parsed": parsed
    }