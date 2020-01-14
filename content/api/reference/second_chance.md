---
weight: 602
meta_title: "API - second_chance - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

{{% code %}}
```shell 

 "second_chance": {
   "send_email": false
},
 ```
{{% /code %}}
{{% description %}}
## Second Chance

If the customer didn't finish the payment, MultiSafepay can send reminders on your behalf.

It is possible to enable/disable the second chance message per transaction. The system uses the following rules:

(*) provided that the conditions above are fulfilled.



| Parameter                         | Type     | Description     |
|-----------------------------------|----------|-----------------|
| second_chance                     | object   |When __no value is stated__, second chance reminders will be sent .                 |
| send_email                        | string   |When this parameter is set to __false__, second chance reminders will not be sent.                 |
| send_email                        | string   |When this parameter is set to __true__, second chance reminders will be sent.            |

The full documentation can be found in the documentation [Second Chance](/tools/second-chance/how-does-it-work/).
{{% /description %}}