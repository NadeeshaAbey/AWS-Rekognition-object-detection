import boto3

# Set up the Rekognition client
rekognition = boto3.client('rekognition', region_name='us-east-1')

# Specify your S3 bucket and image
bucket_name = 'my-rekognition-bucket-21320'  # Replace with your bucket name
image_name = 'test-image.jpeg'

# Call Rekognition to detect objects
response = rekognition.detect_labels(
    Image={
        'S3Object': {
            'Bucket': bucket_name,
            'Name': image_name
        }
    },
    MaxLabels=10  # Get up to 10 objects
)

# Print the results
print("Detected objects:")
for label in response['Labels']:
    print(f"{label['Name']} (Confidence: {label['Confidence']:.2f}%)")