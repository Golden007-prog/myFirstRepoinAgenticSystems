import json
import os

# Step 1: Store a JSON-formatted string representing an API response
api_response_json = '''
{
  "id": "req_123",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
'''

# Step 2: Parse the JSON string into a Python dictionary using json.loads()
parsed_response = json.loads(api_response_json)

# Step 3: Extract values from the parsed object (including nested fields)
request_id = parsed_response["id"]
status = parsed_response["status"]
text_result = parsed_response["result"]["text"]
confidence_score = parsed_response["result"]["confidence"]

# Step 4: Print the extracted information
print(f"Request ID: {request_id}")
print(f"Status: {status}")
print(f"Text: {text_result}")
print(f"Confidence: {confidence_score}")

# Step 5: Check confidence score and print a warning if below 0.9
if confidence_score < 0.9:
    print("Warning: Confidence score is below 0.9")

# Step 6: Create a new Python dictionary representing a follow-up result
follow_up_result = {
    "original_request_id": request_id,
    "follow_up_status": "processed",
    "follow_up_result": {
        "summary": f"Successfully processed: {text_result}",
        "original_confidence": confidence_score,
        "requires_review": confidence_score < 0.9
    }
}

# Step 7: Convert the dictionary to a JSON string using json.dumps()
follow_up_json = json.dumps(follow_up_result, indent=2)

# Step 8: Write the JSON output to response.json in the same directory
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "response.json")
with open(output_path, "w") as json_file:
    json_file.write(follow_up_json)

print(f"\nFollow-up response saved to: response.json")
