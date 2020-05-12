---
title : "How does the notification URL work?"
meta_title: "FAQ API - Notification URL - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---
## Notification
Our API will notify your web server when the status of a transaction changes.  
We will add 2 parameters to the notification:  

* Transactionid  
* Timestamp.  

MultiSafepay will always call the notification_url with the timestamp parameter. 

When MultiSafepay calls the notification_url without a timestamp, the call should be ignored.  
The call should also be ignored when the same order status is received. 

## Example
In a request we receive:  
_This request is done through a GET request_.

```
"order_id": 12345,  
"notification_url": https://yourdomain.com/index/paymentprovidernotification?invoice_id=840,
```

When the status of this transaction changes, we will notify the web server with this URL:
https://yourdomain.com/index/paymentprovidernotification?invoice_id=840&transactionid=12345&timestamp=140292929

Carry out the following 3 tasks within your custom implementation: 

1. Perform a status request on the order using the _transactionid_ provided
2. Update the status of the order within your own systems
3. Return an OK message. We expect an empty page with just OK in the body of the response on this request, with a HTTP 200 OK in the header.

### Note:

* Always use (http or https) in the URL
* A notification URL supplied in your [MultiSafepay Control](https://merchant.multisafepay.com) will be leading. This means that we will use the provided notification URL available in your MultiSafepay Control first 
* Port numbers should not be included in the notification URL. Our platform only processes standard ports due to security reasons. 

 
### Response
As response, MultiSafepay expects an empty page with just OK in the body of the response on this request, with a HTTP 200 OK in the header.
When an OK is not received, MultiSafepay will repeat this notification. The notification with timestamp is repeated twice within 15 minutes. 

Please make sure that our [IP ranges](/faq/general/ip-ranges/) is authorized to process the notification URL.

When our systems call the code at your notification_url, your code can perform a GET request on our [API](/api/#retrieve-an-order) to receive the actual status of the transaction. The field __status__ is relevant for further processing of the order.
