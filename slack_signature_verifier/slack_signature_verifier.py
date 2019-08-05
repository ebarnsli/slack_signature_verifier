import hashlib
import hmac

def verify_slack_signature(slack_post_request, slack_signing_secret):
    slack_signature = slack_post_request['headers']['X-Slack-Signature']
    slack_request_timestamp = slack_post_request['headers']['X-Slack-Request-Timestamp']
    request_body = slack_post_request["body"]

    basestring = f"v0:{slack_request_timestamp}:{request_body}".encode('utf-8')
    my_signature = 'v0=' + hmac.new(slack_signing_secret, basestring, hashlib.sha256).hexdigest()

    return hmac.compare_digest(my_signature, slack_signature)
