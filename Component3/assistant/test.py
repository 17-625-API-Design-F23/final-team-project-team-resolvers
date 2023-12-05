import unittest
import bithub_pb2
from server import AIAssistantService  # Assuming server.py contains AIAssistantService

class TestAIAssistantService(unittest.TestCase):
    def test_generate_pr_description(self):
        service = AIAssistantService()
        request = bithub_pb2.PRDescriptionRequest(repository_url="http://example.com/repo", branch_name="main")
        response = service.GeneratePRDescription(request, None)
        self.assertEqual(response.description, "Mock PR Description")
    # Other test cases implemented similarly
