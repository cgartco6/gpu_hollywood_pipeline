from core.planner import Planner
from core.orchestrator import Orchestrator
from tools.ffmpeg import build_final


def run(prompt):

    planner = Planner()
    orchestrator = Orchestrator()

    plan = planner.create(prompt)
    results = orchestrator.run(plan)

    final_video = build_final(results)

    return final_video


if __name__ == "__main__":

    output = run("cyberpunk war with emotional AI narration")

    print("DONE:", output)
