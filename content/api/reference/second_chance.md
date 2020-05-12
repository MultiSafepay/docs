---
weight: 602
meta_title: "API - second_chance - Developers MultiSafepay"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for Payment Methods, Tools and General Questions as well as the contact details of our Support and Integration Teams."
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



| Parameter                         | Type     | Description     |
|-----------------------------------|----------|-----------------|
| second_chance                     | object   |When __no value is stated__, Second Chance reminders will be sent .                 |
| send_email                        | string   |When this parameter is set to __false__, Second Chance reminders will not be sent.                 |
| send_email                        | string   |When this parameter is set to __true__, Second Chance reminders will be sent.            |

The full documentation can be found in the documentation [Second Chance](/tools/second-chance/how-does-it-work/)
{{% /description %}}