---
title: 'HTTP Errors'
weight: 11
meta_title: "FAQ HTTP Error - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---
> * Please note that HTTP errors are not necessarily originated from the MultiSafepay platform. They are rather generic errors you can come across while browsing the web.

Below you can find a list of the most common error codes and their explanations:

|  Error	|  Description 	           |
|-----------|--------------------------|
| HTTP 200: OK | The page responds correctly but lacks the text 'OK' in the body. |          
| HTTP 301: Moved permanently | The page has been moved permanently. The [notification URL](/faq/api/how-does-the-notification-url-work) needs to be adjusted in the account and / or the transaction request. | 
| HTTP 302: Found | The page redirects to another location. The [notification URL](/faq/api/how-does-the-notification-url-work) needs to be adjusted in the account and / or the transaction request. |                 
| HTTP 403: Forbidden | The page appears to be held behind a log in screen. This often occurs on a testing environment. Either remove the log in page or whitelist our [IP-ranges](/faq/general/ip-ranges) | 
| HTTP 404: Not found | Page does not exist. The [notification URL](/faq/api/how-does-the-notification-url-work) needs to be adjusted in the account and / or the transaction request. |
| HTTP 500: Internal server error | The server of the webshop is malfunctioning. A server administrator or web developer should be able to resolve this. |
| HTTP 503: Service not available | The function that processes the notification does not work. A server administrator or web developer should be able to solve this. | 
