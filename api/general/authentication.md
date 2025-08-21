---
title: Authentication
category:
  uri: General
slug: authentication
position: 1
privacy:
  view: public
---

All requests to our API require authentication.

Include your [website API key](/docs/sites#site-id-api-key-and-security-code) as an HTTP header in your request: `api_key`

> ❗️ Always keep your API keys secure. Publicly exposing your credentials can compromise your account.

{/* markdown-link-check-disable */}

```curl Test API key
curl -X POST "https://testapi.multisafepay.com/v1/json/" \
--header "api_key: <your-test-API-key>"
```

```curl Live API key
curl -X POST "https://api.multisafepay.com/v1/json/" \
--header "api_key: <your-API-key>"
```

{/* markdown-link-check-enable*/}
