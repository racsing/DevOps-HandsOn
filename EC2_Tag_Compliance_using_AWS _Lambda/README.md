## EC2 Tag Compliance using AWS Lambda

### Requirements:</br>
  A) Creation of EventBridge Rule</br>
  B) Creation of IAM Role with necessary permissions</br>
  C) Creation of Lambda function</br>
  D) SeS Email verification</br>
  E) EC2 servers</br>

### Assumptions:</br>
  A) Considered 'running' instances only for checking the tags compliance</br>
  B) Default Region selected - US West (N. California) us-west-1</br>
  C) Considered that, CASE of tags will match exactly, Hence not performed extra manipulation on CASE.</br>
  D) Considered that 'CreatedBy' tag will always be present (already mentioned in the problem statement).</br>
  
### Steps: </br>
  A) _EventBridge Rule: Created a CloudWatch Events Rule That Triggers on a Schedule of 1 hours. </br>_
  
  <img width="300" alt="Screenshot 2022-05-28 at 16 09 01" src="https://user-images.githubusercontent.com/96699659/170821978-2cf54a04-6785-43de-84ce-00d0ea7c625d.png"></br>

  B) _IAM Role: Created an iam role to provide necessary permissions to lambda such as, ec2 and ses.</br>_
  
  <img width="300" alt="Screenshot 2022-05-28 at 16 17 37" src="https://user-images.githubusercontent.com/96699659/170822469-12c2d269-25f5-4879-bae1-e4aec7833840.png"></br>
 
  C) _SES: Verification of emails is necessary to send email through Amazon SES.</br>_
  
  <img width="300" alt="Screenshot 2022-05-28 at 16 19 43" src="https://user-images.githubusercontent.com/96699659/170822414-f17e6371-c8f8-45ab-86a8-881fd3b176ac.png"></br>
  
  D) _Lambda function: Created a lambda by uploading the required python script and attaching necessary roles and polices.</br>_
  
  <img width="300" alt="Screenshot 2022-05-28 at 16 42 19" src="https://user-images.githubusercontent.com/96699659/170823126-b35b05e9-a4dd-4e68-8974-d734e80bdeff.png"></br>
  
  E) _EC2 servers: To test the script for tag compliance, launced two ec2's, one server with missing environment tag.</br>_
  
  <img align="left" width="300" alt="Screenshot 2022-05-28 at 16 33 11" src="https://user-images.githubusercontent.com/96699659/170822964-8cb9995a-22fd-4d70-a181-8154e261a262.png"><img align="" width="300" alt="Screenshot 2022-05-28 at 16 33 16" src="https://user-images.githubusercontent.com/96699659/170822966-a0761d8f-16ca-404c-94c4-df73797ec30f.png"></br>
  
  F)_Email Response: Received email after instance was not compliant with required tags</br>_

</br><img width="200" alt="Screenshot_2022-05-28-16-54-10-59_e307a3f9df9f380ebaf106e1dc980bb6" src="https://user-images.githubusercontent.com/96699659/170823441-30adf275-7692-4e94-8213-be04483bf64b.jpg"></br>



