class CandidateActivitiesResponse:
    def __init__(self, completed, jobs_applied, interview_calls):
        self.completed = completed
        self.jobs_applied = jobs_applied
        self.interview_calls = interview_calls

    def __getattr__(self, name: str):
        return self.__dict__[f"{name}"]

    def __setattr__(self, name: str, value):
        self.__dict__[f"{name}"] = value

# class CandidateActivitiesResponse:
    # def __init__(self, completed, jobs_applied, interview_calls):
    #     self._completed = completed
    #     self._jobs_applied = jobs_applied
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
    # def jobs_applied(self):
    #     return self._jobs_applied
    #
    # @jobs_applied.setter
    # def jobs_applied(self, value):
    #     self._jobs_applied = value
    #
    # @property
    # def interview_calls(self):
    #     return self._interview_calls
    #
    # @interview_calls.setter
    # def interview_calls(self, value):
    #     self._interview_calls = value
