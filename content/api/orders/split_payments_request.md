---
weight: 240
meta_title: "API - Split payments - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
---
{{< code-block >}}

> POST - /orders

```shell
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "currency": "EUR",
    "amount": "1000",
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

```shell
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
## Split Payments
The split payment tool allows you to split the amount of a transaction over several MultiSafepay Control accounts. [Merchants](/faq/general/multisafepay-glossary/#merchant) can choose to split payments based on percentage, a fixed amount or a combination of the two.

Read more about [split payments](/tools/split-payments) on our documentation page.

**Parameters**

----------------

__type__ | string

Specifies the payment flow for the checkout process. Options: direct, redirect and paymentlink.  

----------------
__gateway__ | string

The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request.

----------------
__order_id__ | integer / string

The unique identifier from your system for the order. If the values are only numbers the type will be integer, otherwise it will be string.

----------------
__currency__ | string

The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. 

----------------
__amount__ | integer

The amount (in cents) that the customer needs to pay.

----------------
__description__ | string

A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this description will also be shown on the customer's bank statement. Max. 200 characters. HTML is not supported. Use the 'items' or 'shopping_cart' objects for this.

----------------
__payment_options__ | object

----------------
__notification_url__ | string

Endpoint where we will send the notifications to [notification_url](/faq/api/how-does-the-notification-url-work)

----------------
__notification_method__ | string

Sends push notification (POST,GET) default: GET.

----------------
__redirect_url__ | string

Customer will be redirected to this page after a successful payment. In the event that the transaction is marked with the status [uncleared](/faq/general/multisafepay-glossary/#uncleared), the customer will also be redirected to the thank-you page of the webshop. The uncleared status will not be passed on to the customer who will experience the payment as successful at all times.

----------------
__cancel_url__ | string

Customer will be redirected to this page after a failed payment.

----------------
__split_payments__ | object

----------------
__split_payments.merchant__ | integer

Affiliate AccountID of a MultiSafepay Control.   

----------------
__split_payments.percentage__ | float

Define a percentage of the amount to split.

----------------
__split_payments.fixed__ | integer

Define amount to split in cents.

----------------
__split_payments.description__ | string

Description.


{{% /description %}}
