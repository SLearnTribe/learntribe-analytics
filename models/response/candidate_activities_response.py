class CandidateActivitiesResponse:
    def __init__(self, completed, jobsApplied, interview_calls):
        self.completed = completed
        self.jobsApplied = jobsApplied
        self.interview_calls = interview_calls

    def __getattr__(self, name: str):
        return self.__dict__[f"{name}"]

    def __setattr__(self, name: str, value):
        self.__dict__[f"{name}"] = value

# class CandidateActivitiesResponse:
    # def __init__(self, completed, jobsApplied, interview_calls):
    #     self._completed = completed
    #     self._jobs_applied = jobsApplied
    #     self._interview_calls = interview_calls
    #
    # @property
    # def completed(self):
    #     return self._completed
    #
    # @completed.setter
    # def completed(self, value):
    #     self._completed = value
    #
    # @property
    # def jobsApplied(self):
    #     return self._jobs_applied
    #
    # @jobsApplied.setter
    # def jobsApplied(self, value):
    #     self._jobs_applied = value
    #
    # @property
    # def interview_calls(self):
    #     return self._interview_calls
    #
    # @interview_calls.setter
    # def interview_calls(self, value):
    #     self._interview_calls = value
