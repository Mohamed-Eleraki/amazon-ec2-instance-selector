# import json
# from google.cloud import aiplatform

# # Function to load data from a JSON file
# def load_json_data(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# # Define your file path
# json_file_path = 'issues.json'

# # Load input data from the JSON file
# data = load_json_data(json_file_path)

# # Extract test values from the loaded data
# # test_values1 = data.get("test_values1")
# # test_values2 = data.get("test_values2")

# # Replace 'PROJ_ID', 'REGION', and 'ENDPOINT_ID' with actual inputs
# project_id = 'your-project-id'
# region = 'your-region'
# endpoint_id = 'your-endpoint-id'

# # Initialize the endpoint
# # endpoint = aiplatform.Endpoint(
# #     endpoint_name=f'projects/{project_id}/locations/{region}/endpoints/{endpoint_id}'
# # )

# # Predict using the loaded test input values
# # predict_responses = endpoint.predict(data)

# # Output prediction results
# print("Prediction for input json:\n")
# # print(predict_responses)

# # Save the results to a file (prediction_results.json)
# # with open('prediction_results.json', 'w') as output_file:
# #     json.dump(predict_responses, output_file)