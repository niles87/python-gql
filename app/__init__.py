from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_sqlalchemy import SQLAlchemy
from ariadne import QueryType, graphql_sync, make_executable_schema
from ariadne.constants import PLAYGROUND_HTML


app = Flask(__name__)

app.config.from_object("config.Development")

mongo = PyMongo(app)
sql_alch = SQLAlchemy(app)

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()
schema = make_executable_schema(type_defs, query)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    # On GET request serve GraphQL Playground
    # You don't need to provide Playground if you don't want to
    # but keep on mind this will not prohibit clients from
    # exploring your API using desktop GraphQL Playground app.
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
