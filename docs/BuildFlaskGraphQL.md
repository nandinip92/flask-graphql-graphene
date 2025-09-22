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

# # Define a GraphQL schema with a query type
# class Query(graphene.ObjectType):
#     # Define a simple "hello" field that returns a string
#     hello = graphene.String(description='A typical hello world')

#     # Resolver function for the "hello" field
#     # This function returns the value of the field when queried
#     def resolve_hello(self, info):
#         return 'Hello, World!'

# Define the root Query type for GraphQL
class Query(graphene.ObjectType):
    # Define a "hello" field with an optional argument "name"
    hello = graphene.String(
        name=graphene.Argument(graphene.String, default_value="World"),  # Optional argument with default
        description="Say hello to someone"  # Description shown in GraphiQL or schema introspection
    )

    # Resolver function for the "hello" field
    def resolve_hello(self, info, name):
        """
        This function is called whenever the 'hello' field is queried.
        - 'info' contains request context (not used here)
        - 'name' is provided by the client or defaults to "World"
        """
        return f"Hello {name}"  # Returns a greeting string

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

### Understanding the Query Class and hello Field

- Our `Query` class extends `graphene.ObjectType`, which is how Graphene defines the root of a GraphQL schema.

- Within the `Query` class, we define a field called `hello`.

**Field Definition**

```python
hello = graphene.String(
    name=graphene.Argument(graphene.String, default_value="World"),  # Optional argument with default
    description="Say hello to someone"  # Description shown in GraphiQL or schema introspection
)
```

- Every field must have a **return type**. Here, `hello` returns a `String`.

- Fields can also **accept arguments**. In this case:

  - `name` is an optional argument of type `String`.
  - `default_value="World"` ensures that if no name is provided, `"World"` is used.

- `description` provides developer-friendly documentation visible in GraphiQL or other tools.

**Argument Explanation**

```python
name = graphene.Argument(graphene.String, default_value="World")
```

- name = graphene.Argument(graphene.String, default_value="World")
  Argument() specifies that this is an argument to the field.
- Its type (graphene.String) defines what type of value it accepts.
- default_value is used when the client does not provide an argument.

**Resolver Function**

```python
def resolve_hello(self, info, name):
    return f"Hello {name}"
```

- The resolver defines the logic executed when a field is queried.

- It must be named as `resolve\_<field_name>`; here, the field is `hello`, so the resolver is `resolve_hello`.

- Arguments passed to the field (like `name`) are received by the resolver.

- The function returns the value for the field; in this case, it returns `"Hello <name>"`.

### Summuary of what is happening in GraphQL Query:

- The `Query` class defines what data the API provides.

- The `hello` field is a string field that can optionally accept a name argument:

- If a `name` is provided, it returns `"Hello <name>".`

- If no `name` is provided, it defaults to `"World"` and returns `"Hello World"`.

- The `description` of the field (`"Say hello to someone"`) is displayed in GraphiQL or other tools for developer-friendly documentation.

- The `resolve_hello` method is the resolver that returns the actual data for the hello query.

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
