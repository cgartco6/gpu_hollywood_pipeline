from workers.gpu_worker import process_scene


class Orchestrator:

    def run(self, plan):

        results = []

        for scene in plan["scenes"]:
            results.append(process_scene(scene))

        return results
