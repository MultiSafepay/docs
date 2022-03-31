---
title: 'HTTP errors'
weight: 5
meta_title: "HTTP errors - MultiSafepay Docs"
read_more: "."
aliases:
    - /faq/errors-explained/http-errors
---
> **Note:** HTTP errors don't necessarily originate from the MultiSafepay platform. They are generic errors you can encounter while browsing the web.

The following table lists the most common HTTP error codes and descriptions:

|  Error	|  Description 	           |
|-----------|--------------------------|
| HTTP 200: OK | The page is responding correctly but is missing the text `OK` in the body. |          
| HTTP 301: Moved permanently | The page has moved permanently. Check your [webhook endpoint](/integrations/self-made/configure-your-webhook/) is configured correctly in your MultiSafepay account and/or the API request. | 
| HTTP 302: Found | The page redirects to another location. Check your [webhook endpoint](/integrations/self-made/configure-your-webhook/) is configured correctly in your MultiSafepay account and/or the API request. |                 
| HTTP 403: Forbidden | The page appears to require a login. This often occurs in a testing environment. Either remove the login page, or add our IP ranges to your allow list. For a list of MultiSafepay IP addresses, email <integration@multisafepay.com> | 
| HTTP 404: Not found | The page doesn't exist. Check that your [webhook endpoint](/integrations/self-made/configure-your-webhook/) is configured correctly in your MultiSafepay account and/or the API request. |
| HTTP 500: Internal server error | The webshop server is malfunctioning. Contact your server administrator or web developer to resolve this. |
| HTTP 503: Service not available | The function that processes the notification isn't working. Contact your server administrator or web developer to resolve this. | 
