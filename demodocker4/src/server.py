from flask import Flask, jsonify, request
import boto3

server = Flask(__name__)
s3 = boto3.client('s3')

# Configuración para formatear la respuesta JSON
server.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@server.route("/", methods=['GET'])
def get_s3_buckets():
    region = request.args.get('region', 'us-east-1')

    # Create a new S3 client with the specified region
    s3_region = boto3.client('s3', region_name=region)

    # List S3 buckets
    response = s3_region.list_buckets()
    buckets = [bucket['Name'] for bucket in response['Buckets']]

    return jsonify(buckets)

if __name__ == "__main__":
    server.run(host='0.0.0.0')
