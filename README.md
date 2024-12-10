<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Fee Analysis - User Manual</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 20px 10px;
            text-align: center;
        }
        header h1 {
            margin: 0;
        }
        section {
            padding: 20px;
            margin: 20px auto;
            max-width: 800px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-left: 3px solid #4CAF50;
            font-family: monospace;
            overflow-x: auto;
        }
        ol {
            padding-left: 20px;
        }
        .execution-time {
            display: flex;
            justify-content: space-between;
            margin-top: 20px;
        }
        .execution-time div {
            width: 45%;
            padding: 10px;
            text-align: center;
            background-color: #e8f5e9;
            border: 1px solid #4CAF50;
            border-radius: 5px;
        }
        .execution-time h3 {
            color: #4CAF50;
        }
    </style>
</head>
<body>
    <header>
        <h1>Student Fee Analysis</h1>
        <p>Analyzing fee submission patterns for students</p>
    </header>

    <section>
        <h2 style="color: #4CAF50;">Overview</h2>
        <p>
            This project aims to identify the most frequent day of the month students submit their fees,
            based on a dataset of students and their payment records. The system supports both
            linear and parallel implementations to optimize execution time.
        </p>
    </section>

    <section>
        <h2 style="color: #4CAF50;">Setup Instructions</h2>
        <p>Follow these steps to set up and run the project:</p>
        <ol>
            <li>
                <strong>Create a virtual environment:</strong>
                <pre>python -m venv venv</pre>
            </li>
            <li>
                <strong>Activate the virtual environment:</strong>
                <pre>
Windows: venv\Scripts\activate
Mac/Ubuntu: source venv/bin/activate
                </pre>
            </li>
            <li>
                <strong>Install dependencies:</strong>
                <pre>pip install -r requirements.txt</pre>
            </li>
            <li>
                <strong>Run the script linearly:</strong>
                <pre>python linear.py</pre>
            </li>
            <li>
                <strong>Run the script parallel:</strong>
                <pre>python parallel.py</pre>
            </li>
        </ol>
    </section>

    <section>
        <h2 style="color: #4CAF50;">Execution Time Comparison</h2>
        <p>The project implements two approaches:</p>
        <ol>
            <li><strong>Linear Implementation:</strong> Processes data sequentially, suitable for smaller datasets.</li>
            <li><strong>Parallel Implementation:</strong> Leverages multithreading to optimize performance on larger datasets.</li>
        </ol>
        <div class="execution-time">
            <div>
                <h3>Linear Execution</h3>
                <p>Start Time: <strong>2024-12-10 19:42:38.056700</strong></p>
                <p>End Time: <strong>2024-12-10 19:42:56.945347</strong></p>
                <p><strong>Total Time:</strong> 18.88 seconds</p>
            </div>
            <div>
                <h3>Parallel Execution</h3>
                <p>Start Time: <strong>2024-12-10 19:47:44.715000</strong></p>
                <p>End Time: <strong>2024-12-10 19:47:48.288306</strong></p>
                <p><strong>Total Time:</strong> 03.57 seconds</p>
            </div>
        </div>
    </section>
</body>
</html>
#   P D C - a s s i g n m e n t  
 #   P D C - a s s i g n m e n t  
 #   P D C - a s s i g n m e n t  
 