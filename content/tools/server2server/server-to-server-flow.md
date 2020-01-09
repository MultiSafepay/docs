---
title: "How to process Server to Server credit card payments?"
weight: 73
meta_title: "Server to Server flow - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---
## 3D enabled request
To process a direct credit card transaction (server to server), use the _POST -/orders_ endpoint. 

The transaction request type should be "direct".    

```shell 
"type": "direct",
"gateway": "CREDITCARD",
```

When 3D secure verification is required, the HTML form will be returned and should be rendered.

```shell 
"customer_verification": {
     "html": "<html>\n<head>\n<title>3D Html form</title>....",
     "type": "form" 
}
```

Once the customer has successfully processed the verification step to finalize the payment, the <i>notification_url</i> will notify the ecommerce platform with a completed status. Order details can be called through a GET -/orders/{order_id} . 

## Non 3D request 
When no 3D verification is required, the transaction status response will be processed directly and no form will be sent.

```shell 

    "success": true,
    "data": {
```

## POST notification
Optionally, POST notification can be enabled, meaning that the transaction status is automatically sent to the notification_url via a POST call. 

By default this parameter is 'GET'.      

```shell 
"payment_options": {
    {
        "notification_url": "https://my.notificatio.url",
        "notification_method" : "POST",
        "cancel_url": null,
        "redirect_url": null,
    }
```

Use our API reference on [server to server](/api/#server-to-server) for more information on how to process a direct credit card payment.

<br>

