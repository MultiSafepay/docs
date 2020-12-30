---
weight: 602
meta_title: "API - days_active - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

```shell 
"days_active": 30,
 ```

```shell 
"seconds_active": 60,
```

```shell 
"description": "Test Order Description",
```
{{< /code-block >}}

{{< description >}}
## days_active / seconds_active

The days or seconds active indicates the lifetime of a payment link.

* If seconds_active is sent in the API request and larger than 0, then seconds_active will be used
* If days_active is sent in the API request then days_active is used
* If nothing is sent, then 30 days will be set by default
* If both seconds_active and days_active are sent in the API request, then seconds_active is used if the value is larger than 0.

The full documentation can be found on our FAQ page, [The lifetime of a payment link](/faq/api/lifetime-of-a-payment-link)

**Parameters**

__days_active__ | string

The number of days the payment link will be active for. Default is 30.

----------------
__seconds_active__ | string

The number of seconds the payment link will be active for. Default is 30 days.

----------------

__description__ | string

A text that can be added to the order. The text will be printed on the bank statement of the customer, within the limits of their bank. _Please note: MultiSafepay will remove all html tags and cut the remaining text at 200 charachters_

{{< /description >}}
