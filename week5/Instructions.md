# Week 5

## More advanced querying
Review the content at https://www.caktusgroup.com/blog/2017/04/05/digging-into-django-querysets/  This will be key to this weeks discusion question.


## Review Chapters 9, 10, 11
Read the chapters and submit your work for these and the exercsises.  The primary content of these chapters is user and session management which is extremely important to site security.  One thing not really called out in user authentication chapter is the idea of using a slow hashing function.  Django defaults to good encryption algorithms in BCrypt and PBDKF2 both of which are designed to be slow.  Some excellent information on why this is good can be found in this stack overflow post: https://security.stackexchange.com/questions/4781/do-any-security-experts-recommend-bcrypt-for-password-storage
Don't forget to commit your changes for the exercise and the follow along and tag the commit as Week5


## Note
I wanted to point out that we're using HTTP for all of this testing. You never want to send passwords over HTTP connections always use HTTPS.  Your django code however would not change because real world deployments do SSL termination at the load balancer so all communication inside your network either has another form of encryption or is unencrypted.  Some great examples of load balancers are HAProxy (my preferred), NGINX, Apache2, and many many more.


