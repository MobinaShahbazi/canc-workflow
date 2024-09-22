import requests

from input_management import reformed_data


class SpiffArenaAPIClient:

    def __init__(self):
        self.base_api_url = 'http://localhost:8000//v1.0'
        self.project_location = 'internship:breast-cancer-screening'
        self.access_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6InNwaWZmd29ya2Zsb3dfYmFja2VuZF9vcGVuX2lkIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwOi8vbG9jYWxob3N0OjgwMDAvb3BlbmlkIiwiYXVkIjpbInNwaWZmd29ya2Zsb3ctYmFja2VuZCIsIkpYZVFFeG0wSmhRUEx1bWdIdElJcWY1MmJEYWxIejBxIl0sImlhdCI6MTcyNzAyNjU1NiwiZXhwIjoxNzI3MTk5MzU3LCJzdWIiOiJhZG1pbiIsImVtYWlsIjoiYWRtaW5AZXhhbXBsZS5jb20iLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJBZG1pbiJ9.ENO6ZYKmn3GdRIQr8MPCWM7jTDHMB2W_dhDN8NGy3oyw5qsHUoPiC65m3GyekMBKdelFr402Ak2hAhcB_LflyJAtQpG253XfPhZ_sbM25XtEo5LcoK5sWqfgK9eYXsx34zX7Pmsg7XRFqEBJX5Le5ht6H_L3LcLViAJ9pLRLjJR4teV261MVOk3x2aUL5LpNEsHBWkka9_RoZVve4CpGd-eN7j-gKD6vRRSxl4cdVEwaJw_PEaUVr-Dbmbizqz7MmoW234kESMrAZ4jRcw_7kf-ToOpoVjaXBOwlMQ41pEYmbg2OJjcLsap9la-YgD5TzQIYFaqCJyPTqctVhw757A'
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

    def create_instance(self,msa_name):
        instance_id = self.direct_call(msa_name, {})['process_instance']['id']
        task_id = self.trigger_process(instance_id)['results'][0]['task_id']  # task id of form task (user task)
        self.put_data(reformed_data, instance_id, task_id)
        end_event_id = self.get_end_event_id(instance_id)
        return self.get_task_data(instance_id,end_event_id)



client_inctance = SpiffArenaAPIClient()
print(client_inctance.create_instance('start'))