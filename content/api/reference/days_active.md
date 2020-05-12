---
weight: 602
meta_title: "API - days_active - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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
