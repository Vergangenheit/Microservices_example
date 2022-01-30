from recommendations import RecommendationService

from recommendations_pb2 import BookCategory, RecommendationRequest, RecommendationResponse


def test_recommendations():
    service = RecommendationService()
    request = RecommendationRequest(
        user_id=1, category=BookCategory.MISTERY, max_results=1
    )
    response: RecommendationResponse = service.Recommend(request, None)
    assert len(response.recommendations) == 1
