import requests


class SpiffArenaAPIClient:

    def __init__(self):
        self.base_api_url = 'http://localhost:8000//v1.0'
        self.project_location = 'internship:breast-cancer-screening'
        self.access_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6InNwaWZmd29ya2Zsb3dfYmFja2VuZF9vcGVuX2lkIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwMDAvb3BlbmlkIiwiYXVkIjpbInNwaWZmd29ya2Zsb3ctYmFja2VuZCIsIkpYZVFFeG0wSmhRUEx1bWdIdElJcWY1MmJEYWxIejBxIl0sImlhdCI6MTcyNjYwMjA5MCwiZXhwIjoxNzI2Nzc0ODkwLCJzdWIiOiJhZG1pbiIsImVtYWlsIjoiYWRtaW5AZXhhbXBsZS5jb20iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJBZG1pbiJ9.KeIkNcnWfr69WGmDMFKf34A1DqRJNqHKSyf10r-P3f7IsGS83B5MgeIAbUVMiZ5NFOSG-RAGgiMM7DRAnvTwUT9AghjPNcCt4TCuQcZR4KMmULVt9AD0BwCGGR0ttrIalfhTl8nIiyWEjnI2N-h1sIVyUixxtFEeXEPyrYFLgryRvoc3ZweyxfZ2NmMT88P7I4whsrl11BPigR0i0BvwmEZyEupg6HJ7BuEYJhTecMbI2NU5uouymBPdBcIUa87ccHSx-BB7lmWM2G5ae0bkmt39qPfsqrjjmYyOzQn-4njtk1Ld-OAbMXERunb1eju3hp7K67Jht045gtZSIlhKzQ'

    def http_request(self, method, url, body=None):
        request = requests.Request(method, url, json=body, headers={'Authorization': self.access_token})
        prepared = request.prepare()
        with requests.Session() as session:
            response = session.send(prepared)
        return response.json()


    def direct_call(self, name, body):
        response = self.http_request(method='POST', url=f'{self.base_api_url}/messages/{name}?execution_mode=synchronous',
                                     body=body)
        return response


    def trigger_process(self, instance_id):
        response = self.http_request(method='GET', url=f'{self.base_api_url}/tasks?process_instance_id={instance_id}')
        return response


    def put_data(self, form, instance_id, task_id):
        response = self.http_request(method='PUT', url=f'{self.base_api_url}/tasks/{instance_id}/{task_id}', body=form)
        return response


    def get_task_data(self, instance_id, task_id):
        response = self.http_request(method='GET',
                                     url=f'{self.base_api_url}/task-data/{self.project_location}/{instance_id}/{task_id}')
        return response["data"]


    def get_process_instance_status(self, instance_id):
        response = self.http_request(method='GET',
                                     url=f'{self.base_api_url}/process-instances/{self.project_location}/{instance_id}')
        return response["status"]


    def get_end_event_id(self, instance_id):
        tasks = self.http_request(method='GET',
                                  url=f'{self.base_api_url}/process-instances/{self.project_location}/{instance_id}/task-info')
        for task in tasks:
            if task["typename"] == "EndEvent":
                end_event_id = task['guid']
        return end_event_id

#
# client = SpiffArenaAPIClient()
# print(client.get_task_data(4,'f37338af-df02-4f1a-8e35-b9b5d4179e8d'))