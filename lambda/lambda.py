
import boto3
import botocore.config
import json
import uuid
from datetime import datetime, timezone


def blog_generate_using_bedrock(blogtopic: str) -> str:

    prompt = f"""
Write a 200-word blog on the following topic:

{blogtopic}
"""

    body = {
        "prompt": prompt,
        "max_gen_len": 800,
        "temperature": 0.5,
        "top_p": 0.9
    }

    try:
        bedrock = boto3.client(
            "bedrock-runtime",
            region_name="us-east-1",
            config=botocore.config.Config(
                read_timeout=300,
                retries={"max_attempts": 3}
            )
        )

        response = bedrock.invoke_model(
            body=json.dumps(body),
            modelId="us.meta.llama3-1-8b-instruct-v1:0",
            accept="application/json",
            contentType="application/json"
        )

        response_content = response["body"].read()

        response_data = json.loads(response_content)

        print(response_data)

        blog_details = response_data["generation"]

        return blog_details

    except Exception as e:
        print(f"Error generating blog: {e}")
        return "Error generating blog."


def save_blog_details_s3(s3_key, s3_bucket, generated_blog):

    s3 = boto3.client("s3")

    try:
        s3.put_object(
            Bucket=s3_bucket,
            Key=s3_key,
            Body=generated_blog.encode("utf-8"),
            ContentType="text/plain"
        )

        print("Blog saved to S3")

    except Exception as e:
        print(f"Error saving blog to S3: {e}")


def lambda_handler(event, context):

    event = json.loads(event["body"])

    blogtopic = event["blog_topic"]

    generated_blog = blog_generate_using_bedrock(blogtopic)

    if generated_blog:

        current_time = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
        s3_key = f"blog-output/{current_time}-{uuid.uuid4().hex[:8]}.txt"


        s3_bucket = "awsbedrock2011"

        save_blog_details_s3(
            s3_key,
            s3_bucket,
            generated_blog
        )

    else:
        print("No blog was generated")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "blog": generated_blog
        })
    }

