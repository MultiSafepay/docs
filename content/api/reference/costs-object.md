---
weight: 601
meta_title: "API reference - costs (object) - MultiSafepay Docs"

---

{{< code-block >}}

```json 
{
  "costs":[
    {
      "transaction_id":123456789,
      "amount":0.19,
      "description":"Refund order 258655825 for TEST TEST",
      "type":"internal",
      "created":"2019-03-01T16:14:02",
      "status":"completed"
    }
  ]
}
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

The amount the customer needs to pay in the currency's smallest unit:

- Decimal currencies: Value for 10 EUR = 1000 (1000 cents)
- Zero-decimal currencies: Value for ¥10 = 10

----------------
`description` | string | 

The order description that appears in your MultiSafepay dashboard and on the customer's bank statement (if supported by their bank).   
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

The [order status](/about-payments/multisafepay-statuses/). 


{{< /description >}}