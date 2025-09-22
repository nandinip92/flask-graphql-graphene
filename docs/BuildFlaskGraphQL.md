# Build a Basic Flask + GraphQL App

This guide walks you through creating a minimal Flask app with GraphQL support using Graphene.
We define a simple query that returns "Hello, World!" and expose it via a /graphql endpoint with an interactive GraphiQL interface.

## Create a Basic Flask APP with GraphQL

1. Create a new Python file, let’s say app.py— 👉 Checkout [app.py]

```python
# Import the necessary modules
from flask import Flask                  # Flask is the web framework
from flask_graphql import GraphQLView   # Provides a GraphQL endpoint for Flask
import graphene                         # Graphene is a Python library to build GraphQL schemas

# Define a GraphQL schema with a query type
class Query(graphene.ObjectType):
    # Define a simple "hello" field that returns a string
    hello = graphene.String(description='A typical hello world')

    # Resolver function for the "hello" field
    # This function returns the value of the field when queried
    def resolve_hello(self, info):
        return 'Hello, World!'

# Create a GraphQL schema using the Query type
schema = graphene.Schema(query=Query)

# Initialize the Flask application
app = Flask(__name__)

# Add a URL route for GraphQL
# '/graphql' endpoint will handle GraphQL queries
# graphiql=True enables the interactive GraphiQL interface in the browser
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

# Run the Flask development server
if __name__ == '__main__':
    # By default, the server runs on http://127.0.0.1:5000
    app.run()

```

## 2. High-Level Explanation

### Imports:

- `Flask` handles web requests and routing.
- `GraphQLView` creates a GraphQL endpoint in Flask.
- `graphene` defines the GraphQL schema, types, and resolvers.

### GraphQL Query:

- The `Query` class defines what data the API provides.
- The `hello` field returns `"Hello, World!"` via the `resolve_hello` method.

### Schema:

- `schema = graphene.Schema(query=Query)` sets the root query for the GraphQL API.

### Flask App & Route:

- The Flask app is initialized with `app = Flask(__name__)`.

- `/graphql` endpoint is added and connected to the GraphQL schema.

- `graphiql=True` enables the interactive GraphiQL interface for testing queries in the browser.

### Run Server:

`app.run()` starts the development server on `http://127.0.0.1:5000`.

---

**Resource Link:**

https://medium.com/four-o-four/how-aliens-learn-graphql-with-python-flask-and-graphene-310bda97c824

https://medium.com/featurepreneur/build-graphql-apis-in-flask-using-graphene-4750f81ab204
