---
title: "Integration and API requests"
breadcrumb_title: "Integration and API requests"
weight: 40
layout: child
meta_title: "Server to Server - Integration and API requests - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Integrating Server to Server in your ecommerce platform via our API"
---

To integrate Server to Server using our API, see API Reference – [Server to Server](/api/#server-to-server).

{{< details title="3D Secure requests" >}}

Make a `direct` POST `/orders` request. 

```shell 
"type": "direct",
"gateway": "CREDITCARD",
```

We recommend redirecting customers to the `payment_url` returned in the response. 

Otherwise, you can use the rendered HTML form returned in the response.

```shell 
    "customer_verification": {
         "html": "<html>\n<head>\n<title>3D Html form</title>....",
         "type": "form" 
    }
```

Once the customer has successfully processed the verification step to finalize the payment, we send **Completed** status to your backend via the `notification_url`.

To retrieve more information about the order, make a GET `/orders/{order_id}` request. 

{{< /details >}}

{{< details title="Non-3D Secure requests" >}}

When 3D Secure verification is required, the transaction status response is processed directly and no HTML form is returned.

```shell 

    "success": true,
    "data": { }
```

{{< /details >}}

{{< details title="POST notifications" >}}

## POST notifications
Optionally, to automatically send the transaction status to the `notification_url` via a POST call (instead of the default GET method), enable POST notifications.

```shell 
"payment_options": {
    {
        "notification_url": "https://my.notificatio.url",
        "notification_method" : "POST",
        "cancel_url": null,
        "redirect_url": null,
    }
```
{{< /details >}}