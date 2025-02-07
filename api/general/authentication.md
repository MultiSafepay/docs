---
title: Authentication
category: 623dacddb0cbdd0394b9f5a9
slug: 'authentication'
order: 2
hidden: false
---

All requests to our API require authentication. 

Include your [website API key](/docs/sites#site-id-api-key-and-security-code) as an HTTP header in your request: `api_key`
[block:callout]
{
  "type": "danger",
  "body": "Always keep your API keys secure. Publicly exposing your credentials can compromise your account."
}
[/block]

<!-- markdown-link-check-disable -->
[block:code]
{
  "codes": [
    {
      "code": "curl -X POST \"https://testapi.multisafepay.com/v1/json/\" \\\n--header \"api_key: <your-test-API-key>\"",
      "language": "curl",
      "name": "Test API key"
    }
  ]
}
[/block]

[block:code]
{
  "codes": [
    {
      "code": "curl -X POST \"https://api.multisafepay.com/v1/json/\" \\\n--header \"api_key: <your-API-key>\"",
      "language": "curl",
      "name": "Live API key"
    }
  ]
}
[/block]
<!-- markdown-link-check-enable-->
