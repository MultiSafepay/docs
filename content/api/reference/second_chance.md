---
weight: 602
meta_title: "API - second_chance - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
```shell 

 "second_chance": {
   "send_email": false
},
 ```
{{< /code-block >}}
{{< description >}}
## Second Chance

If the customer didn't finish the payment, MultiSafepay can send reminders on your behalf.

It is possible to enable/disable the Second Chance message per transaction. The system uses the following rules:

(*) provided that the conditions above are fulfilled.


**Parameters**

__second_chance__ | object

When __no value is stated__, Second Chance reminders will be sent.

----------------
__send_email__ | string

When this parameter is set to __false__, Second Chance reminders will not be sent.

----------------
__send_email__ | string

When this parameter is set to __true__, Second Chance reminders will be sent.

----------------

**Suppress Email Second Chance after cancellation**

When a customer makes an order, goes to the checkout page but returns, and tries again, some webshops create a second order. If the second chance is on, the customer will receive emails for the first order, even when the second order is paid.

Cancellation of the first order doesn't suppress the second chance email.

To suppress the second chance email you have to add these parameters in the update of the order:
``` 
"status": "cancelled",
"exclude_order": 1
```


The full documentation can be found in the documentation [Second Chance](/tools/second-chance/how-does-it-work)
{{% /description %}}