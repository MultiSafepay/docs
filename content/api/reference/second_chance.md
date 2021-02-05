---
weight: 602
meta_title: "API - second_chance - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---

{{< code-block >}}
```shell 

 "second_chance": {
   "send_email": true
},
 ```
{{< /code-block >}}
{{< description >}}
## Second Chance

If the customer didn't finish the payment, you can send a reminder in the form of a payment link.

As per GDPR requirements MultiSafepay does not submit emails by default. Please ensure that when enabling this option, there is a documented consent from the receiver for submitting an email related to the respective payment link.

It is possible to enable/disable the Second Chance message per transaction. The system uses the following rules:

(*) provided that the conditions above are fulfilled.


**Parameters**

__second_chance__ | object

Sends a payment reminder to the customer in the form of an email.

__send_email__ | boolean

Sends a Second Chance reminder in the form of an email to the customer when set to _true_. When set to _false_ or left empty, no email reminder will be sent.

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