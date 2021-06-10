---
weight: 610
meta_title: "API - Transaction statuses - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
```shell 
"notification_url": "http://www.example.com/client/notification?type=notification",
```

```shell 
"redirect_url": "http://www.example.com/client/notification?type=redirect",
```

```shell
"cancel_url": "http://www.example.com/client/notification?type=cancel", 
```

```shell 
"notification_method": "POST",
```

```shell 
"close_window": "true",
```


{{< /code-block >}}

{{< description >}}
## payment_option, object 


**Parameters**

__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)              

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.              

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment. 

----------------
__notification_method__ | string

Enables push notifications (POST,GET) default: GET.   

----------------

__close_window__ | bool (optional)


Options: true, false. Set to true if you want to display the MultiSafepay payment page in a new window and want to close it automatically after the payment process.

----------------

{{% /description %}}
