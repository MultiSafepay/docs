---
title : "How does the notification URL work?"
meta_title: "FAQ API - Notification URL - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
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

__Please note:__ Within the notification url, the *transaction_id* should have the same value as the *order_id*

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
5. Calculate hmac/sha512 of step 4 using your [API key](/faq/general/glossary/#api-key) as the HMAC key.
6. Only allow the request if this hash matches the sha512hex from step 3 and the timestamp is recent enough.

## GET vs POST notification
The advantage of implementing the POST notification is that your webserver will save on roundtrips in communication.

With the POST notification your webserver does not have to request the transaction status from our API anymore, but will get the changed transaction directly in the notification payload.

The security requirement you must implement is to always validate the payload so you know the POST notification comes from MultiSafepay and has not been tampered with.

### Response
As response, MultiSafepay expects an _OK_ in the body of the response. A response containing the code '200' in the body will not be accepted.

If an _OK_ is not received, MultiSafepay will repeat this notification. The notification with a timestamp is repeated 15 minutes and 30 minutes after the payment has taken place.

### Error in offline actions

In your [MultiSafepay Contol](https://merchant.multisafepay.com/), there is a paragraph at the bottom of the page named _Offline Actions_ which can tell you the notifications our server has sent to your webshop. If you see an error here, this indicates that our server has a problem reaching your webshop or our server did not retrieve the correct response. There should be an _OK_ in the body of the response.

### Note:

* Always use **https** in the notification_url
* A notification URL supplied in your [MultiSafepay Control](https://merchant.multisafepay.com) will be leading. This means that we will use the provided notification URL available in your MultiSafepay Control first
* If the notification URL in the website settings is empty or not returning an OK (for whatever reason), we will call the notification URL from the transaction
* Port numbers should not be included in the notification URL. Our platform only processes standard ports due to security reasons
* Please make sure that our [IP ranges](/faq/general/ip-ranges) are authorized to reach the notification URL.
