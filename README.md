🧩 Flask + GraphQL Demo

A minimal project demonstrating how Flask and GraphQL work together.
This project uses Flask as a lightweight web framework and Graphene to define a simple GraphQL schema.

## Features

- A basic hello query ({ hello }) that returns "Hello, World!"

- Integration of GraphQLView to expose a /graphql endpoint

- GraphiQL interface for interactive testing of queries in the browser

- Quick starting point for learning how to build GraphQL APIs with Flask

## Getting Started

Follow these steps to run the project on your local machine.

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/graphql-flask-demo.git
cd graphql-flask-demo
```

### 2. Create and activate a virtual environment

It’s best practice to use a virtual environment to isolate dependencies.

```bash
python -m venv venv        # Create a virtual environment

# Activate it:
# Windows (Command Prompt):
.\venv\Scripts\activate
# Windows (PowerShell):
.\venv\Scripts\Activate.ps1
# Git Bash / Linux / MacOS:
source venv/Scripts/activate  # Windows Git Bash
# source venv/bin/activate     # Linux / MacOS
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

**_Note:_**

- If you skip using a virtual environment, packages will be installed globally.
- `requirements.txt` ensures everyone uses the same package versions.

4. Run the Flask App

```bash
python app.py
```

- By default, the server runs on `http://127.0.0.1:5000`
- Open this URL in your browser and navigate to `/graphql` to access the GraphiQL interface.

Test query:

```graphql
{
  hello
}
```

Expected response:

```json
{
  "data": {
    "hello": "Hello, World!"
  }
}
```

### 5. Git Ignore

Make sure to ignore the virtual environment in Git by adding this to .gitignore:

```bash
venv/
```

This ensures that only your code and requirements.txt are tracked, while the virtual environment is excluded.

## Further Reading

- Learn more about Flask: [FLASK.md](./docs/FLASK.md)

- Build a Flask + GraphQL project from scratch: [ProjectSetUp.md](./docs/ProjectSetUp.md)

- Step-by-step guide to create the app: [BuildFlaskGraphQL.md](./docs/BuildFlaskGraphQL.md)

