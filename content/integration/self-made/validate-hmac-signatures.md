---
title: 'Validate HMAC signatures'
breadcrumb_title: "Validate HMAC signatures"
layout: 'single'
meta_title: 'Build your integration – Handle notifications - Validate HMAC signatures - MultiSafepay Docs'
logo: '/svgs/Wrappers.svg'
short_description: 'Validate HMAC signatures of notifications.'
weight: 1
url: '/integrations/self-made/handle-notifications/validate-hmac-signatures/'
---

To validate the HMAC signature of `POST` notification requests in your own solution, follow these steps:

1. Base64 decode the `Auth` header value of the request.
{{< details title="Example" >}}
Before: `MTY0MTIxODg4NDowMzI3ZjUyODBlYjI5ZmNiMzE0OTAyYjYxZmMzN2E5MTExZjRjMDMxZDMxZjg1OTc4MTFlY2RjMTRjOGM4ZjM1NjkwNGM2NDgwOTY2MWMzY2ViOWZkMjczN2Y1MmUxNGU5NDJjMzJkZGIwN2E2ZDZhNzZhMDAwNDI2ZDY1ZDc4Yg==`

After:
`1641218884:0327f5280eb29fcb314902b61fc37a9111f4c031d31f8597811ecdc14c8c8f356904c64809661c3ceb9fd2737f52e14e942c32ddb07a6d6a76a000426d65d78b`
{{< /details >}}
2. Split the decoded `Auth` header value using the colon (`:`) as separator.
    - The first string is the timestamp.
    - The second string is the HMAC signature. 

    {{< details title="Example" >}}
Timestamp: `1641218884`  
HMAC signature: `0327f5280eb29fcb314902b61fc37a9111f4c031d31f8597811ecdc14c8c8f356904c64809661c3ceb9fd2737f52e14e942c32ddb07a6d6a76a000426d65d78b`
{{< /details >}}
3. Concatenate the:

    - Timestamp
    - Colon (`:`)
    - Payload of the request

    {{< details title="Example" >}}
```
1641218884:{"amount":1000,"amount_refunded":0,"costs":[{"amount":0.49,"description":"0.49 For iDEAL Transactions","transaction_id":"123456789","type":"SYSTEM"}],"created":"2022-01-03T15:08:02","currency":"EUR","custom_info":{"custom_1":null,"custom_2":null,"custom_3":null},"customer":{"address1":null,"address2":null,"city":null,"country":null,"country_name":null,"email":"","first_name":null,"house_number":null,"last_name":null,"locale":"en_US","phone1":null,"phone2":"","state":null,"zip_code":null},"description":"product description","fastcheckout":"NO","financial_status":"initialized","items":null,"modified":"2022-01-03T15:08:02","order_id":"my-order-id", ”payment_details":{"account_holder_name":null,"account_iban":"https://example.com","account_id":null,"external_transaction_id":"123456789","issuer_id":"3151","recurring_flow":null,"recurring_id":null,"recurring_model":null,"type":"IDEAL"},"payment_methods":[{"amount":1000,"currency":"EUR","description":"product description","external_transaction_id":"123456789","payment_description":"iDEAL","status":"initialized","type":"IDEAL"}],"reason":"","reason_code":"","related_transactions":null,"status":"initialized","transaction_id":"123456789","var1":null,"var2":null,"var3":null}
```
{{< /details >}}
4. SHA512 hash the concatenated string that resulted from step 3, using your API key as the HMAC key.

    If the request is valid, the hashed value from step 4 matches the HMAC signature from step 2.

    {{< details title="Example" >}}
HMAC key: `8HHhGgRWrA3O7NswjmgwyH7buPPCGnR5AkwAQyqI`

SHA512 hash: `0327f5280eb29fcb314902b61fc37a9111f4c031d31f8597811ecdc14c8c8f356904c64809661c3ceb9fd2737f52e14e942c32ddb07a6d6a76a000426d65d78b`
{{< /details >}}

    Additionally, check whether the timestamp is recent and the originating IP address is MultiSafepay's. For a list of MultiSafepay's IP addresses, email the Integration Team at <integration@multisafepay.com>

## Sample code

We provide a code sample in Python for your reference.

{{< details title="Sample notification validation in Python" >}}

``` python
#!/usr/bin/python

import argparse
import base64
import hashlib
import hmac
import sys

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-k", "--apikey", help="API key", required=True)
parser.add_argument("-p", "--payload", help="Payload", required=True)
parser.add_argument("-a", "--authheader", help="Auth header", required=True)
args = parser.parse_args()

# Step 1: Base64 decode the auth header
encoded_auth_bytes = args.authheader.encode("ascii")
decoded_auth_bytes = base64.b64decode(encoded_auth_bytes)
decoded_auth = decoded_auth_bytes.decode("ascii")

# Step 2: Split the decoded auth header
timestamp = decoded_auth.split(':')[0]
signature = decoded_auth.split(':')[1]

# Step 3: Concatenate the timestamp, colon, and payload
concatenated_string = timestamp + ":" + args.payload

# Step 4: SHA512 hash the concatenated string
hashed_value = hmac.new(args.apikey.encode(), concatenated_string.encode(), hashlib.sha512).hexdigest()

# Step 5: Compare the hashed value with the signature
if hashed_value == signature:
	print("The notification is authentic")
	sys.exit(0)
else:
	print("Error: The notification is not authentic")
	sys.exit(1)
```
{{< /details >}}