# IAI-SLE
#  Simple AI Agent Using If-Else

A beginner-friendly **Python AI agent** built using simple `if-elif-else` statements. This project demonstrates how a basic conversational program can respond to different user inputs.

# Features

* Responds to a greeting (`hello`)
* Gives a basic weather response (`weather`)
* Provides a Python study suggestion (`study`)
* Exits the program when the user types `bye`
* Handles unknown commands with a default response

##  Technologies Used

* **Python 3**
* `if-elif-else` statements
* `while` loop
* `input()` function
* `print()` function

##  Project Structure

```text
simple-ai-agent/
│
├── agent.py
└── README.md
```

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/simple-ai-agent.git
```

### 2. Navigate to the project folder

```bash
cd simple-ai-agent
```

### 3. Run the Python program

```bash
python agent.py
```

##  Example

```text
Simple AI Agent
Type 'hello', 'weather', 'study', or 'bye'.

You: hello
AI: Hello! How can I help you?

You: study
AI: Great! Let's study Python. Start with variables and if-else statements.

You: weather
AI: I can't check live weather yet, but I hope it's nice outside!

You: bye
AI: Goodbye!
```

##  How It Works

The program continuously asks the user for input using a `while` loop.

The input is converted to lowercase and checked using `if-elif-else` conditions:

* If the user enters `hello`, the agent gives a greeting.
* If the user enters `weather`, it gives a weather-related response.
* If the user enters `study`, it suggests studying Python.
* If the user enters `bye`, the program exits.
* For any other input, the agent says it doesn't understand.

##  Learning Objectives

This project is useful for beginners who want to learn:

* Variables
* User input
* Conditional statements
* `while` loops
* String methods such as `.lower()`
* Basic chatbot/agent logic

##  Future Improvements

Some possible improvements include:

* Add more commands and responses
* Connect the agent to a live weather API
* Add a simple GUI
* Use functions to organize the code
* Add natural language processing
* Connect the agent to an AI API

##  Author

**Your Name**

If you found this project useful, consider giving the repository a ⭐.
