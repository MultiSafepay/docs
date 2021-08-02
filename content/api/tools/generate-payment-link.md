---
weight: 1360
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json

{
    "type": "paymentlink",
    "order_id": "test-123",
    "gateway": "",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test order description",
    "second_chance": { 
        "send_email" : true
    },
    "payment_options": {
        "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel",
        "close_window": true
    },
    "customer": {
        "locale": "en_US"
    }
}
```


> JSON Response


```json 
{
  "success": true,
  "data": {
    "order_id": "test-123",
    "payment_url": "https://devpayv2.multisafepay.com/connect/89QENbhQYcJoP2CO0kx6pSRrw8v2JFnTynr/?lang=nl_NL"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Generating a payment link

For several scenarios, it can be useful for our merchants to generate a payment link. The payment link lets your MultiSafepay account create a unique transaction that the payment can be matched with.

### Second Chance

[Second Chance](https://docs.multisafepay.com/payments/boost/second-chance/) is an email reminder that points out to your customers of their attempted (and incomplete) payment(s) and encourages them to finalize the payment(s).

As per GDPR requirements, MultiSafepay does not submit emails by default. If you enable this option, please ensure there is a documented consent from the recipient of the payment link.

{{< alert-notice >}} Please note: Payment links will no longer send Second Chance emails by default. It is the responsibility of the merchant to include the Second Chance script in the JSON request. See the Second Chance JSON script on the right-hand side. {{< /alert-notice >}}


**Parameters**

__type__ | string | required

The payment flow for the checkout process. Fill in 'paymentlink'. It must be noted that orders with "type": "paymentlink" will be visible in your MultiSafepay account under _Tools_ > _Payment link generator_


----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters. 

----------------
__gateway__ (optional) | string 

The unique gateway ID to direct the customer straight to the payment method.  
To retrieve gateway IDs, see [Gateways](/api/#gateways).

----------------
__currency__ | string | required

The currency you want the customer to pay in.   
Format: [ISO-4217 currency codes](https://www.iso.org/iso-4217-currency-codes.html).  

----------------
__amount__ | integer | required

The amount (in cents) the customer needs to pay.

----------------
__description__ | string | required

The order description that appears in your MultiSafepay account and on the customer's bank statement (if supported by the customer's bank).   
Format: Maximum 200 characters.   
HTML is **not** supported. Use the `items` or `shopping_cart` objects for this.

----------------

__close_window__ | bool | optional


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`. 

----------------

__second_chance__ (optional) | object

Sends a payment reminder to the customer in the form of an email.

----------------

__send_email__ (optional) | boolean

Sends a Second Chance reminder in the form of an email to the customer when set to _true_. When set to _false_ or left empty, no email reminder will be sent.

----------------

The rest of the fields are optional.
{{% /description %}}