# AWS Services with Scripting and the AWS CLI
## AWS Systems Manager - Session manager
- Allows you to manage your nodes from a CLI interface without worrying about open inbound ports, ssh keys, etc.
- Can Connect to both Amazon EC2 instances and non-EC2 managed nodes.

IAM is between the admin and AWS Systems Manager Session Manager.
![Aws Systems Manager](systemsmanager.png)

## Stopinator
This is a script which I believe is placed on all EC2 Tasks/instances.

This is available in the session-manager CLI. You can add the tag: `{'stopinator': 'stop'}` or `{'stopinator': 'terminate'}` and all of the instances with that tage will be stoped.
