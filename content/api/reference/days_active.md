---
weight: 602
meta_title: "API - days_active - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---
{{< code-block >}}

```shell 
"days_active": 30,
 ```

```shell 
"seconds_active": 60,
```
{{< /code-block >}}

{{< description >}}
## days_active / seconds_active

The days or seconds active indicates the lifetime of a payment link.

The full documentation can be found on our FAQ page, [The lifetime of a payment link](/faq/api/lifetime-of-a-payment-link/)

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| days_active                        | string   | The number of days the payment link will be active for. Default is 30.               |
|

| Parameter                          | Type     | Description                                                                          |
|------------------------------------|----------|--------------------------------------------------------------------------------------|
| seconds_active                     | string   | The number of seconds the payment link will be active for. Default is 30 days.        |
{{< /description >}}
