---
weight: 607
meta_title: "API reference - payment_methods (object) - MultiSafepay Docs"

---
{{< code-block >}}
```json 
{
  "payment_methods":[
    {
      "account_id":10071970,
      "amount":9743,
      "currency":"EUR",
      "description":"Test order description",
      "payment_description":"SOFORT Banking",
      "status":"initialized",
      "type":"DIRECTBANK"
    }
  ]
}
```


{{< /code-block >}}

{{< description >}}
## payment methods (object)

May contain:  

**Parameters**

----------------
`account_id` | string

The international bank account number (IBAN) to be charged for the transaction.             

----------------
`amount` | integer 

The amount (in cents) for the customer to pay.              

----------------
`currency` | string 

The currency you want the customer to pay with.  
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).

----------------
`description` | string 

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------
`payment_description` | string

The payment method.

----------------
`status` | string 

The [order status](/payments/multisafepay-statuses/). 

----------------
`external_transaction_id` | string

The order reference number from a third party, e.g. the payment method.

----------------
`account_holder_name` | string

The name of the account holder to be charged for the transaction.

----------------
`type` | string 

The payment gateway.    

----------------
`card_expiry_date` | string 

The expiry date of the credit card.    

----------------
`last4` | string 

The last 4 digits of the credit card number.    

----------------


{{% /description %}}