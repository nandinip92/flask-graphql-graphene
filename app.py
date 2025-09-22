from flask import Flask
from flask_graphql import GraphQLView
import graphene
class Query(graphene.ObjectType):
    # Hello field with optional argument 'name'
    hello = graphene.String(
        name=graphene.Argument(graphene.String, default_value="World"),
        description="Say hello to someone"
    )

    # Resolver
    def resolve_hello(self, info, name):
        # If no name is provided, default_value="World" will be used
        return f"Hello {name}"

# Create a GraphQL schema using the Query type 
schema = graphene.Schema(query=Query)

# Initialize the Flask application
app = Flask(__name__)

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

# Run the Flask development server
if __name__=='__main__':
    app.run()