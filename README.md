# CSecureDataX
This project uses a database (SQL/No SQL) to store and retrieve data, along with cloud technologies like AWS, which is used for data transfer and storage. An open-source encryption/decryption algorithm like AES is used to encrypt the data, along with a key management mechanism to ensure secure encryption/decryption.

The methodology used to solve the problem involves encrypting the data on-premises using Python Boto3, creating a data table using SQL, and transferring it to the AWS S3 bucket while ensuring encryption using the KMS key. This approach ensures that the data is secured both at rest and in transit.

The scope of the proposed solution includes providing a reliable and secure way of transferring data across different estates while ensuring data protection. The solution can be used for a variety of use cases, such as transferring customer data with demographics.

Overall, the project's objective is to provide data protection by encrypting the data while in transit and at rest, ensuring that unauthorized access is prevented. The solution uses open-source encryption algorithms and cloud technologies to provide a scalable, secure, and reliable way of transferring data.
