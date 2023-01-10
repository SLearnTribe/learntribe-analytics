class HrHiringsResponse:
    def __init__(self):
        self._job_title = ""
        self._skills = ""
        self._job_posted_on = ""
        self._job_status = ""
        self._job_count = 0

    @property
    def job_title(self):
        return self._job_title

    @job_title.setter
    def job_title(self, value):
        self._job_title = value

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        self._skills = value

    @property
    def job_posted_on(self):
        return self._job_posted_on

    @job_posted_on.setter
    def job_posted_on(self, value):
        self._job_posted_on = value

    @property
    def job_status(self):
        return self._job_status

    @job_status.setter
    def job_status(self, value):
        self._job_status = value

    @property
    def job_count(self):
        return self._job_count

    @job_count.setter
    def job_count(self, value):
        self._job_count = value
