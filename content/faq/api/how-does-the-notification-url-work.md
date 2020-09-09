---
title : "How does the notification URL work?"
meta_title: "FAQ API - Notification URL - MultiSafepay Support"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---
## Notification
Our notifications are webhooks where our API will notify your web server when the status of a transaction changes. 

The notification webhooks are triggered by events made by both your customers (e.g. completing a payment) and you (e.g. creating a refund).
  
We will add 2 parameters to the notification request:

* transactionid  
* timestamp. 

For a POST notification we will also add the order data to the body of the request.

MultiSafepay will always call the notification_url with the timestamp parameter. 

When MultiSafepay calls the notification_url without a timestamp, the call can safely be ignored.  
The call should also be ignored for further processing when the same order status is received. 

Our API provides a GET and POST notification.

## GET notification example
From your webserver we received the following transaction request:

```
"order_id": 12345,  
"payment_options": {
    "notification_url": "https://yourdomain.com/index/paymentprovidernotification?invoice_id=840",
}
```

When the status of this transaction changes, we will notify your web server with this URL through a **GET** request.
https://yourdomain.com/index/paymentprovidernotification?invoice_id=840&transactionid=12345&timestamp=140292929

Carry out the following 3 tasks within your custom implementation: 

1. Perform a [status request](/api/#retrieve-an-order) on the order using the provided _transactionid_
2. Read the **status** field from the response and update the status of the order within your own systems
3. Return an OK message. We expect an empty page with only OK in the body of the response on this request, with a HTTP 200 OK in the header.

## POST notification example
From your webserver we receive the following transaction request:

```
"order_id": 12345,  
"payment_options": {
    "notification_url": "https://yourdomain.com/index/paymentprovidernotification?invoice_id=840",
    "notification_method": "POST",
}
```

When the status of this transaction changes, we will notify your web server with this URL through a **POST** request.
https://yourdomain.com/index/paymentprovidernotification?invoice_id=840&transactionid=12345&timestamp=140292929

Carry out the following 3 tasks within your custom implementation: 

1. Validate the **POST** request.
2. Read the **status** field from the response and update the status of the order within your own systems
3. Return an OK message. We expect an empty page with only OK in the body of the response on this request, with a HTTP 200 OK in the header.

## POST notification validation
Before accepting the order data, the POST notification request must be validated by comparing the provided and calculated signature/hash.

The calculation of this signature/hash:

1. Base64 decode the Auth header.
2. Explode/split the resulting string using the colon as separator.
3. The first part is the timestamp, the second part is sha512hex of the payload.
4. Concatenate timestamp, colon, and original payload.
5. Calculate hmac/sha512 of step 4 using your API Key as the HMAC key.
6. Only allow the request if this hash matches the sha512hex from step 3 and the timestamp is recent enough.

## GET vs POST notification
The advantage of implementing the POST notification is that your webserver will save on roundtrips in communication.

With the POST notification your webserver does not have to request the transaction status from our API anymore, but will get the changed transaction directly in the notification payload.

The security requirement you must implement is to always validate the payload so you know the POST notification comes from MultiSafepay and has not been tampered with.

### Response
As response, MultiSafepay expects an empty page with just OK in the body of the response on this request, with a HTTP 200 OK in the header.
When an OK is not received, MultiSafepay will repeat this notification. The notification with timestamp is repeated twice within 15 minutes. 

### Note:

* Always use **https** in the notification_url
* A notification URL supplied in your [MultiSafepay Control](https://merchant.multisafepay.com) will be leading. This means that we will use the provided notification URL available in your MultiSafepay Control first 
* Port numbers should not be included in the notification URL. Our platform only processes standard ports due to security reasons. 
* Please make sure that our [IP ranges](/faq/general/ip-ranges) are authorized to reach the notification URL.
