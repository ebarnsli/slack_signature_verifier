# SLACK SIGNATURE VERIFIER

https://pypi.org/project/slack-signature-verifier/#description

## Use
    - pass in post request from slack and your apps signing secret
    - returns whether request is valid message from slack
    
```
 slack_request = {
    body: "example_body",
    headers: {
        "X-Slack-Signature": "signature_from_slack"
        "X-Slack-Request-Timestamp": "EPOCH_TIMESTAMP"
    }
 }
 
 is_valid_request = verify_slack_signature(slack_request, os.envrion["SLACK_SIGNING_SECRET"])
 
```
