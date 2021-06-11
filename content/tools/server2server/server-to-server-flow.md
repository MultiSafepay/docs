---
title: "How to process Server to Server credit card payments?"
weight: 73
meta_title: "Server to Server flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: '.'
---
## 3D enabled request
To process a direct credit card transaction (server to server), use the _POST -/orders_ endpoint. 

The transaction request type should be "direct".    

```shell 
"type": "direct",
"gateway": "CREDITCARD",
```

When [3D Secure](/faq/general/glossary/#3d-secure) verification is required you have two option for handling the verification:

1. the recommended way is to redirect your customer directly to the payment_url that will be returned in the response. 
2. otherwise you can use the HTML form that will be returned and should be rendered.

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
    "data": { }
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



