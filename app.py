from flask import Flask
from flask_graphql import GraphQLView
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(description="a typical hello world")

    def resolve_hello(self,info):
        return "HEllo World"

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