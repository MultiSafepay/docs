---
weight: 210
meta_title: "API reference - Send second chance emails - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
aliases:
    - /api/#second-chance
    - /faq/api/disable-second-chance
    - /faq/api/disabling-second-chance
    - /developer/api/disabling-second-chance/
---

{{< code-block >}}
```json 
{
  "second_chance":{
    "send_email":true
  }
}
 ```
{{< /code-block >}}
{{< description >}}
### Send second chance emails

If a customer initiated a transaction but didn't complete payment, you can email a reminder containing a payment link.

For more information and requirements, see [Second Chance](/payments/boost/second-chance/).

You can enable/disable Second Chance emails in each transaction request. 

See also [Adjust payment link lifetimes](/api/#adjust-payment-link-lifetimes).


**Parameters**

----------------
`second_chance` | object | required

Sends a reminder email to the customer containing a payment link.  

Contains:  

`send_email` | boolean | required

Options:  

- `true`, sends reminder emails.  
- `false` or left empty, doesn't send reminder emails.   

----------------

**Suppressing Second Chance emails after cancellation**

When a customer places an order, goes to the checkout page, doesn't complete payment, but later returns and tries again, some webshops create a second order. If Second Chance emails are enabled, the customer still receives emails for the first order, even after they complete payment for the second order.

Cancelling the first order does **not** suppress Second Chance emails.

To suppress Second Chance emails, send a `PATCH /orders` request containing the following parameters:
``` 
"status": "cancelled",
"exclude_order": 1
```

{{% /description %}}
