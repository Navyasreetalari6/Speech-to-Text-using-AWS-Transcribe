s3import boto3
import uuid

transcribe = boto3.client('transcribe')


def lambda_handler(event, context):
    try:
        # Get the filename and bucket name from the S3 event
        print(event)
        records = event.get('Records', [])
        if not records:
            print("No records found in the event.")
            return
        
        filename = records[0]['s3']['object']['key']
        bucketname = records[0]['s3']['bucket']['name']
        
        # Construct the S3 URL for the audio file
        url = "s3://" + bucketname + "/" + filename
        print(url)
        
        # Generate a unique ID for the transcription job
        myuuid = uuid.uuid1().int
        
        # Start the transcription job
        response = transcribe.start_transcription_job(
            TranscriptionJobName="mylwaudiojob" + "-" + str(myuuid), 
            LanguageCode='en-IN',
            MediaFormat='mp4',  # Specify the media format (in this case, MP4)
            Media={
                'MediaFileUri': url,
            },
            OutputBucketName="projectbucket30944",
            OutputKey="mylwaudiojob" + "-" + str(myuuid) + ".json"
        )
        
        # Print the response from the transcription job
        print(response)
    except Exception as e:
        print("An error occurred:", e)
