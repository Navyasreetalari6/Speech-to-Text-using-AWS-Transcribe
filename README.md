🎙️ Speech to Text using AWS Transcribe - 
This project converts audio files (MP3) into text using AWS Transcribe. The application is built with AWS Lambda, AWS S3, and AWS Transcribe, allowing automatic transcription 
of uploaded audio files and storing the results back in S3 as a JSON file.

🚀 Features - 
Upload MP3 audio files to an S3 bucket.
Automatically trigger a Lambda function on file upload.
Lambda uses AWS Transcribe to convert speech to text.
Transcription results are saved as a JSON file in another S3 bucket or folder.
Simple and serverless architecture — no servers to manage!

🧠 Architecture - 
User uploads an audio file to the input S3 bucket.
S3 event trigger invokes the AWS Lambda function.
The Lambda function:
Starts a transcription job using AWS Transcribe.
Waits until the job completes.
Fetches the transcript and saves it back to an output S3 bucket.

🛠️ Technologies Used - 
AWS S3 – For storing input and output files.
AWS Lambda – For automating the transcription process.
AWS Transcribe – For converting speech to text.
AWS IAM – For managing permissions.
Python (Boto3) – Used for interacting with AWS services.
