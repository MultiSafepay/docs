---
weight: 601
meta_title: "API Reference - costs (object) - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}

```json 
"costs": [
      {
        "transaction_id": 123456789,
        "amount": 0.19,
        "description": "Refund order 258655825 for TEST TEST",
        "type": "internal",
        "created": "2019-03-01T16:14:02",
        "status": "completed"       
        }
]
```

{{< /code-block >}}

{{< description >}}

## costs (object)

May contain:  

----------------
`transaction_id` | integer

MultiSafepay's identifier for the transaction (also known as the PSP ID).

----------------
`amount` | integer | 

The amount (in cents) for the customer to pay. 

----------------
`description` | string | 

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`type` | string 

Options: `SYSTEM`, `internal`.   

----------------
`created` | string

The timestamp for when the order was created.

----------------
`currency` | string 

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html). 

----------------
`status` | string

The [order status](/api/multisafepay-statuses/) of the order. 

**Response**

----------------
`costs` | object

See [costs (object)](/api/#costs-object).

----------------


{{< /description >}}