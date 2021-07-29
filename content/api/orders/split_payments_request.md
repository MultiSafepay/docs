---
weight: 240
meta_title: "API Reference - Split payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}

> POST - /orders

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": 1000,
    "description": "Split Payment Order",
    "affiliate": {
        "split_payments": [
            {
                "merchant": 1001001,
                "fixed": 112,
                "description": "Fixed fee"
            },
            {
                "merchant": 1001001,
                "percentage": 11.2,
                "description": "Percentage fee"
            }
        ]
    }
}
```

> JSON Response

```json
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=en_US"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Split payments
Split the amount of a transaction between multiple MultiSafepay accounts, based on a percentage, a fixed amount, or a combination of the two.

For more information, see [Split payments](/payments/features/split-payments/).

**Parameters**

----------------

__type__ | string

The payment flow for the checkout process.  
Options: `direct`, `redirect`, `paymentlink`.  

----------------
__gateway__ | string

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
__order_id__ | integer / string

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.

----------------
__currency__ | string

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer

The amount (in cents) the customer needs to pay.

----------------
__description__ | string

Text that appears with the order in your MultiSafepay account and on the customer's bank statment (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is not supported. Use the `items` or `shopping_cart` objects for this.

----------------
__payment_options__ | object

Contains the `redirect_url`, `cancel_url`, and [`notification_url`](/developer/api/notification-url).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
See also [notification_url](/developer/api/notification-url).

----------------
__notification_method__ | string

Sends push notification.  
Options: `POST`, `GET`. Default: `GET`.

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------
__split_payments__ | object

----------------
__split_payments.merchant__ | integer

The account ID of the [affiliated MultiSafepay account](/account/partner-account-control/).   

----------------
__split_payments.percentage__ | float

Specify a percentage of the amount to split.

----------------
__split_payments.fixed__ | integer

Specify the amount to split in cents.

----------------
__split_payments.description__ | string

The description of the split payment.


{{% /description %}}
