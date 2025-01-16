---
title: 'HTTP errors'
category: 62962df622e99600810c117d
order: 3
hidden: false
slug: 'http-errors'
---
HTTP response status codes don't necessarily originate from the MultiSafepay platform. They are generic errors you can encounter while browsing the web.

This table lists the most common HTTP error codes and descriptions:

| Error | Description |
|---|---|
| HTTP 204: No content | The page is responding correctly but is missing the text `OK` in the body. |          
| HTTP 301: Moved permanently | The page has moved permanently. Check if your [webhook endpoint](/docs/webhook/) is configured correctly in your MultiSafepay account and/or the API request. | 
| HTTP 302: Found | The page redirects to another location. Check if your [webhook endpoint](/docs/webhook/) is configured correctly in your MultiSafepay account and/or the API request. |                 
| HTTP 403: Forbidden | The page appears to require a login. This often occurs in a testing environment. Either remove the login page, or add our IP ranges to your allow list. For a list of MultiSafepay IP addresses, email <integration@multisafepay.com> | 
| HTTP 404: Not found | The page doesn't exist. Check that your [webhook endpoint](/docs/webhook/) is configured correctly in your MultiSafepay account and/or the API request. |
| HTTP 500: Internal server error | The webshop server is malfunctioning. Contact your server administrator or web developer to resolve this. |
| HTTP 503: Service not available | The function that processes the notification isn't working. Contact your server administrator or web developer to resolve this. | 

<br>

---

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:integration@multisafepay.com\">integration@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]

[Top of page](#)