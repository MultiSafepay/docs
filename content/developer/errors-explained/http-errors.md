---
title: 'HTTP errors'
weight: 5
meta_title: "Errors - HTTP errors - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases:
    - /faq/errors-explained/http-errors
---
> **Note:** HTTP errors don't necessarily originate from the MultiSafepay platform. They are generic errors you can encounter while browsing the web.

The following table lists the most common HTTP error codes and descriptions:

|  Error	|  Description 	           |
|-----------|--------------------------|
| HTTP 200: OK | The page is responding correctly but is missing the text `OK` in the body. |          
| HTTP 301: Moved permanently | The page has moved permanently. Adjust where we send the [notification URL](/developer/api/notification-url) to in your MultiSafepay account and/or the transaction request. | 
| HTTP 302: Found | The page redirects to another location. Adjust where we send the [notification URL](/developer/api/notification-url) to in your MultiSafepay account and/or the transaction request. |                 
| HTTP 403: Forbidden | The page appears require a log-in. This often occurs in a testing environment. Either remove the log-in page or add our [IP-ranges](/faq/general/ip-ranges) to your allow list. | 
| HTTP 404: Not found | The page doesn't exist. Adjust where we send the [notification URL](/developer/api/notification-url) to in your MultiSafepay account and/or the transaction request. |
| HTTP 500: Internal server error | The webshop server is malfunctioning. Contact your server administrator or web developer to resolve this. |
| HTTP 503: Service not available | The function that processes the notification isn't working. Contact your server administrator or web developer to resolve this. | 
