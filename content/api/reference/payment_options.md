---
weight: 610
meta_title: "API - Transaction statuses - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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
| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| notification_url                   | string   |  Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work/)                                                                                                    |
|

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| redirect_url                       | string   |  Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/getting-started/glossary/#uncleared), the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.              |

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| cancel_url                         | string   |  Customer will be redirected to this page after a failed payment.                     |

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| notification_method                | string   | Enables push notifications (POST,GET) default: GET.            |

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| close_window                       | bool     | true, false.                                                                          |                |

{{% /description %}}
