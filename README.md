# 🧩 Flask + GraphQL Demo

This is a minimal project demonstrating how Flask and GraphQL work together.
It uses Flask as the lightweight web framework and Graphene to define a simple GraphQL schema.

The demo includes:

- A basic `hello` query (`{ hello }`) that returns `"Hello, World!"`
- Integration of GraphQLView to expose a `/graphql` endpoint
- Support for the GraphiQL interface to interactively test queries in the browser
- This project serves as a quick starting point for learning how to build GraphQL APIs with Flask.

**👉 Checkout [FLASK.md](./docs/FLASK.md) to know more about Flask.**

## Project setup

### 1. Create a new directory for you project and navigateinto it

```bash
mkdir graphql-flask-demo
cd graphql-flask-demo
```

### 2. Create a virtual environment and activate it:

It’s best practice to use a virtual environment for each Python project. This isolates your project’s dependencies from other projects or the system Python, avoids version conflicts, and makes it easier to share your project with others.

```bash
python -m venv venv        # Create a virtual environment

# Activate it:
# Windows(command prompt):
.\venv\Scripts\activate

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

#git bash of windows
source venv/Scripts/activate

# Linux/MacOS:
source venv/bin/activate

```

While activated, any packages you install will only affect this project.

#### Why Create a Virtual Environment?

1. Isolate Dependencies

   - Each Python project may need different libraries or different versions of the same library.
   - A virtual environment ensures that your project’s dependencies don’t conflict with other projects or the system Python.

2. Avoid System Pollution

   - Installing packages globally can clutter your system Python and might require admin rights.
   - With a virtual environment, all packages are stored inside the project folder.

3. Reproducibility

   - Virtual environments make it easier to share your project with others.
   - Using `requirements.txt` with `pip install -r requirements.txt`, others can recreate the exact environment you used.

4. Safe Experimentation

   - You can try out new packages or versions without affecting other projects or your system Python.

### 3. Install Required Dependencies

With the virtual environment active, install Flask, Flask-GraphQL, and Graphene:

```bash
pip install Flask Flask-GraphQL graphene

```

### 4. Save Dependencies to requirements.txt

After installing the packages, generate a requirements.txt file so others (or yourself on another machine) can recreate the same environment:

```bash
pip freeze > requirements.txt
```

- This file will list all installed packages with exact versions
- Example content of `requirements.txt`:

```ini
Flask==2.3.2
Flask-GraphQL==2.0.1
graphene==3.2.1
```

- Share this file in your repository. Others can install the same packages with:

```bash
pip install -r requirements.txt
```

**_Note:_**

- If someone clones your repo, they can install all required packages at once using:

```bash
pip install -r requirements.txt

```

### 5. Add `.gitignore`

Make sure to ignore your virtual environment folder in Git so it doesn’t get committed to the repository.

Add this to your .gitignore file:

```bash
venv/
```

This ensures that only your code and requirements.txt are tracked, while the virtual environment (which can be recreated anytime) is excluded.

**Important:**

- Make sure you run this after creating and **activating** the virtual environment to ensure all packages are installed inside it.
- If the **virtual environment is not active**, the packages will be installed globally on your system Python, which may cause conflicts with other projects.


