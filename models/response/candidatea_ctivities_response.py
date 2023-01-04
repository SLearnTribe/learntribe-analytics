class CandidateActivitiesResponse:
    def __init__(self, completed, jobs_applied, interview_calls):
        self.completed = completed
        self.jobs_applied = jobs_applied
        self.interview_calls = interview_calls

    def __getattr__(self, name: str):
        return self.__dict__[f"{name}"]

    def __setattr__(self, name: str, value):
        self.__dict__[f"{name}"] = value

