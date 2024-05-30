import leetcode

leetcode_session = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiMTI0MTExMzciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6ImQ1ZTdjMTE5ZjIwMzYzNDA5NWQ4OTgyMTI2ZmQwZTRhMjdjNjIzZThlMWY5ZGU2N2U4MTQ3NDFkMDExOTYwNzIiLCJpZCI6MTI0MTExMzcsImVtYWlsIjoiYWJlbGdoaXRoQG9ha2xhbmQuZWR1IiwidXNlcm5hbWUiOiJBaG1lZEJlbGdoaXRoIiwidXNlcl9zbHVnIjoiQWhtZWRCZWxnaGl0aCIsImF2YXRhciI6Imh0dHBzOi8vYXNzZXRzLmxlZXRjb2RlLmNvbS91c2Vycy9kZWZhdWx0X2F2YXRhci5qcGciLCJyZWZyZXNoZWRfYXQiOjE3MTY5ODc0MTksImlwIjoiMTk3LjIzLjI0NS4xNDYiLCJpZGVudGl0eSI6IjgzODFjMDQ4YTlkNzAyMzBhZjEzYTEyYTc2NjYzZGM0Iiwic2Vzc2lvbl9pZCI6NjI0NzExMzgsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMH0.qIk-Rngwk0GNAjSRQoOTrO4OdV8AXVHc6WHYyxDk2Tg"
csrf_token = "MofP1fB1s6O2pGPyZxaSMcCkpHwCzhZWGxyc5Un63ckmmfwHFDk4HjxWCsiAPo0p"
configuration = leetcode.Configuration()
configuration.api_key["x-csrftoken"] = csrf_token
configuration.api_key["csrftoken"] = csrf_token
configuration.api_key["LEETCODE_SESSION"] = leetcode_session
configuration.api_key["Referer"] = "https://leetcode.com"
configuration.debug = False

api_instance =leetcode.DefaultApi(leetcode.ApiClient(configuration))
graphql_request = leetcode.GraphqlQuery(
query="""
     {
       user {
            username
            isCurrentUserPremium
         }
     }
     """,
variables=leetcode.GraphqlQueryVariables(),
)
print(api_instance.graphql_post(body=graphql_request))