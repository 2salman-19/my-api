# my-api
 <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FastAPI Project</title>
</head>

<body>

    <h1>FastAPI Project</h1>

    <h2>Overview</h2>

    <p>This FastAPI project provides an API for predicting meal plans, calorie requirements, and workout plans based on user input. The project utilizes scikit-learn models for predictions and incorporates various Python libraries for efficient development.</p>

    <h2>Getting Started</h2>

    <h3>Installation</h3>

    <ol>
        <li>
            <p><strong>Clone the repository:</strong></p>

            <pre><code>git clone https://github.com/your/repository.git</code></pre>
        </li>
        <li>
            <p><strong>Install the required packages:</strong></p>

            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
    </ol>

    <h3>Running the API</h3>

    <p>Run the FastAPI application using the following command:</p>

    <pre><code>uvicorn app:app --reload</code></pre>

    <p>The API will be accessible at <a href="http://127.0.0.1:8000">http://127.0.0.1:8000</a>.</p>

    <h2>Project Structure</h2>

    <ul>
        <li><strong>app.py:</strong> Contains the FastAPI application and API endpoint definitions.</li>
        <li><strong>meal_plan.pkl:</strong> Scikit-learn model for predicting meal plans.</li>
        <li><strong>calories.pkl:</strong> Scikit-learn model for predicting calorie requirements.</li>
        <li><strong>workout_plan.pkl:</strong> Scikit-learn model for predicting workout plans.</li>
        <li><strong>requirements.txt:</strong> List of Python dependencies.</li>
    </ul>

    <h2>API Endpoints</h2>

    <h3>POST /predict_all</h3>

    <h4>Description</h4>

    <p>Predicts meal plans, calorie requirements, and workout plans based on user input.</p>

    <h4>Request Parameters</h4>

    <ul>
        <li><strong>Age</strong> (int, required): Age of the person.</li>
        <li><strong>Gender</strong> (str, required): Gender of the person.</li>
        <li><strong>Height</strong> (float, required): Height of the person.</li>
        <li><strong>Weight</strong> (float, required): Weight of the person.</li>
        <li><strong>Fitness_Level</strong> (str, required): Fitness level of the person.</li>
        <li><strong>Fitness_Goal</strong> (str, required): Fitness goal of the person.</li>
        <li><strong>Medical_History</strong> (str, required): Medical history of the person.</li>
    </ul>

    <h4>Example Request</h4>

    <pre><code>{
  "Age": 25,
  "Gender": "Male",
  "Height": 175.0,
  "Weight": 70.0,
  "Fitness_Level": "Intermediate",
  "Fitness_Goal": "Weight Loss",
  "Medical_History": "No known issues"
}</code></pre>

    <h4>Example Response</h4>

    <pre><code>{
  "meal_plan": "Balanced Diet",
  "calories": 2000,
  "workout_plan": "Cardio and Strength Training"
}</code></pre>

    <h2>Model Loading</h2>

    <p>The API loads scikit-learn models (<strong>meal_plan.pkl</strong>, <strong>calories.pkl</strong>, and <strong>workout_plan.pkl</strong>) during startup. Ensure that these models are available in the same directory as the API script.</p>

    <h2>Error Handling</h2>

    <p>If there is an error loading the models or making predictions, the API will respond with an HTTP 500 status code and an error message.</p>

    <h2>Dependencies</h2>

    <pre><code>annotated-types==0.6.0
anyio==4.2.0
click==8.1.7
colorama==0.4.6
exceptiongroup==1.2.0
fastapi==0.108.0
h11==0.14.0
idna==3.6
joblib==1.3.2
numpy==1.26.2
pandas==2.1.4
pydantic==2.5.3
pydantic_core==2.14.6
python-dateutil==2.8.2
pytz==2023.3.post1
scikit-learn==1.3.2
scipy==1.11.4
six==1.16.0
sniffio==1.3.0
starlette==0.32.0.post1
threadpoolctl==3.2.0
typing_extensions==4.9.0
tzdata==2023.4
uvicorn==0.25.0</code></pre>

    <h2>Salman</h2>

    <p>Salman siddique <br>03074721563</p>

</body>

</html>

