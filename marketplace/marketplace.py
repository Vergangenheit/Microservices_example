import os
from flask import Flask, render_template
import grpc
from grpc import Channel
from recommendations_pb2 import BookCategory, RecommendationResponse, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host: str = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel: Channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(user_id=1, category=BookCategory.MYSTERY, max_results=3)
    recommendations_response: RecommendationResponse = recommendations_client.Recommend(recommendations_request)

    return render_template("homepage.html", recommendations=recommendations_response.recommendations)


if __name__ == "__main__":
    app.run(debug=True)
