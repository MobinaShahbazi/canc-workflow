# Breast Cancer Risk Assessment and Recommendation System
## Project Overview
This project is designed to assess the risk of being diagnosed with breast cancer based on a user's medical history and personal health information. By analyzing a range of factors such as family medical history, biopsy results, and other personal health data, the system provides:
- A personalized **risk level** for breast cancer.
- **Recommendations** for future checkups or treatments.
- **Suggested timelines** for appropriate medical follow-ups.
The tool helps individuals and healthcare providers make informed decisions about breast cancer prevention, early detection, and care management.
## How It Works
1. **Risk Assessment**: The system evaluates the user's medical and personal factors to calculate the probability of developing breast cancer.
2. **Recommendations**: Based on the risk assessment, the system suggests specific checkups, treatments, and timelines for follow-ups.
3. **Ongoing Monitoring**: Users can update their medical data over time for revised assessments and recommendations.
## How Spiff Arena Is Used
In this project, I utilized **[Spiff Arena](https://github.com/sartography/spiff-arena)** to design a comprehensive workflow for processing the user’s medical data. Spiff Arena is a workflow engine that allows for the automation of complex decision-making logic. 
### Workflow Design
- The workflow starts by collecting basic user information (e.g., medical history, biopsy results, family history).
- Each step of the process is defined as a **task**, which can either be a **script task** (executing some logic) or a **DMN (Decision Model and Notation)** task (for decision-making).
- As the user moves through the workflow, additional data such as the **risk level** and **recommendations** are added.
- The workflow continues until all necessary information is gathered and the appropriate recommendations are generated.
### Example Workflow Tasks
1. **Initial Data Collection**: Gathers user information and personal medical history.
2. **Risk Calculation Task**: A script task calculates the user’s risk level for breast cancer.
3. **Recommendation Generation**: Based on the risk level, a DMN task provides personalized recommendations and advice for the user, such as when to perform follow-up screenings or tests.
Spiff Arena made it easy to structure the entire decision-making process, ensuring that the right data is collected, analyzed, and turned into actionable advice at each step of the workflow.
## Acknowledgments
We are grateful for the open-source workflow automation library **Spiff Arena**, which allowed us to define and manage the complex decision logic required in this project. You can find more details about Spiff Arena [here](https://github.com/sartography/spiff-arena).
## Running the Project Locally
### Prerequisites
Ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) (optional, if using Docker for deployment)
- [Virtual Environment](https://docs.python.org/3/tutorial/venv.html)
### Steps to Run the Project Locally
1. **First, Dockerize Spiff Arena:**
   - Open up the command line (cmd) in the directory where the `docker-compose.yml` file is located
   - Run these two commands:
     ```bash
     docker-compose pull
     docker-compose up
     ```
2. **Start the Development Server:**
   - Once Spiff Arena is up, start the development server at `http://127.0.0.1:8001`.
3. **Create a New Process Model:**
   - After the server is up, create a new process model and add the files located in `BPMN-files/v0.3` to this process model.
4. **Create an Instance Using the Client:**
   - Use the `create_instance` function in the `SpiffArenaAPIClient` class located at `create_instance/client.py` to create an instance in the workflow.
5. **Check Process Instances:**
   - Navigate to your local server at port `8001` and check the "Process Instances" section. You should see a new instance and can monitor its status, actions, etc.
**Tip:** If the token you are using has expired, you can generate a new one by following these steps:
```bash
cd .\spiffworkflow-backend\
cd .\bin\
python .\get_token
```
