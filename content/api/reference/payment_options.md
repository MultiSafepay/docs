---
weight: 610
meta_title: "API - Transaction statuses - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{% code %}}

```shell 

 "notification_url": "http://www.example.com/client/notification?type=notification",
 ```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| notification_url                   | string   |  Endpoint where we will send the notifications to. [notification_url](/faq/api/how-does-the-notification-url-work/)                                                                                                    |
|


```shell 

"redirect_url": "http://www.example.com/client/notification?type=redirect",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| redirect_url                       | string   |  Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status uncleared, the customer will also be redirected to this page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.              |


```shell

 "cancel_url": "http://www.example.com/client/notification?type=cancel", 

```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| cancel_url                         | string   |  Customer will be redirected to this page after a failed payment.                     |


```shell 

"notification_method": "POST",
```

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| notification_method                | string   | Enables push notifications (POST,GET) default: GET.            |


```shell 

"close_window": "true",
```


| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| close_window                       | bool     | true, false.                                                                          |
{{% /code %}}

{{% description %}}
## payment_option, object 

{{% /description %}}
