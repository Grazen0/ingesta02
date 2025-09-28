import boto3
import csv
from mysql.connector import connect

DB_HOST = 'mysql_bd'
DB_PORT = '3306'
DB_USERNAME = 'root'
DB_PASSWORD = 'utec'
DB_DATABASE = 'db'

FILE_NAME = "data.csv"
S3_BUCKET = "jgrayson-bucket"


with connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_DATABASE,
) as conn:
    with conn.cursor() as cursor:
        _ = cursor.execute("select * from students")
        rows = cursor.fetchall()

with open(FILE_NAME, 'w') as file:
    writer =csv.writer(file)
    writer.writerows(rows)

print(f"Archivo {FILE_NAME} generado.")

s3 = boto3.client("s3")
response = s3.upload_file(FILE_NAME, S3_BUCKET, FILE_NAME)
print(f"Response: {response}")
print("Ingesta completa")
