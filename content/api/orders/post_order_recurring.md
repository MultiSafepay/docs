---
weight: 230
meta_title: "API Reference - Recurring payments - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---

{{< code-block >}}
>  POST - /orders

```json
{
   "type":"redirect",
   "gateway":"CREDITCARD",
   "order_id":"my-order-id-1",
   "currency":"EUR",
   "recurring_model":"unscheduled",
   "recurring_id":"hC6HdH7_5Tg",
   "recurring_flow":"token",
   "amount":10000,
   "description":"Tokenization - ALL - Original unscheduled",
   "payment_options":{
      "notification_url":"http://www.example.com/client/notification?type=notification",
      "redirect_url":"http://www.example.com/client/notification?type=redirect",
      "cancel_url":"http://www.example.com/client/notification?type=cancel",
      "close_window":true
   },
   "customer":{
      "locale":"en_NL",
      "ip_address":"85.149.25.654",
      "forwarded_ip":"",
      "first_name":"null",
      "last_name":"null",
      "address1":"Kraanspoor",
      "house_number":"39",
      "zip_code":"1033 SC",
      "city":"Amsterdam",
      "state":"",
      "country":"NL",
      "birthday":"07061993",
      "gender":"male",
      "phone":"0612345678",
      "email":"example@multisafepay.com",
      "referrer":"http://example.com",
      "user_agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
      "reference":"AutoQAReference"
   }
}
```

> JSON Response

```json
{
   "success":true,
   "data":{
      "order_id":"my-order-id-1",
      "payment_url":"https://payv2.multisafepay.com/connect/82v6HsoQhaR823uIZ7hexDMwQyielzLrdox/?lang=nl_NL"
   }
}
```

{{< /code-block >}}

{{< description >}}
## Recurring payments

You can initiate [recurring payments](/payments/features/recurring-payments/) using [tokenization](/payments/features/tokenization/) for the following payment methods:

* VISA
* MasterCard
* Maestro
* Bancontact
* American Express
* iDEAL
* SOFORT
* Direct debit

Customers can make the initial payment using iDEAL, Bancontact, or SOFORT, followed by recurring payments using SEPA Direct Debit. 

### Processing recurring payments

1. Submit a standard transaction request with recurring payments enabled. 
2. Request the token by [retreiving the order](https://docs.multisafepay.com/api/#retrieve-an-order).
3. Make recurring payment requests as required.

**Parameters**

----------------

__type__ | string | required

The payment flow for the checkout process.  
Options: `direct`.

----------------
__gateway__ | string | required

The payment method used for the checkout process.  
Options: AMEX, DIRDEB, MASTERCARD, VISA.  
Use DIRDEB when the initial payment was made using IDEAL, DIRECTBANK (Sofort) and DIRDEB. 

----------------
__order_id__ | integer / string | required

Your unique identifier for the order.  
If the values are numbers only, the type is `integer`. Otherwise, it is `string`.  
Format: Maximum 50 characters.

----------------
__recurring_id__ | integer

The unique identifier for the recurring payment.

----------------
__recurring_flow__ | string

The tokenization method used to create the recurring payment.  
Options: `token`

----------------

__recurring_model__ | string

The type of recurring method used in the transaction request.  
Options: `unscheduled`, `subscription`, `cardonfile`.

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
__payment_options__ | object | required

See [payment_options (object)](/api/#payment-options-object).

----------------
__notification_url__ | string

Endpoint for MultiSafepay to send status updates and other notifications to.   
For more information, see [notification_url](/developer/api/notification-url).

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

__close_window__ | bool | optional


To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.   
Options: `True`, `False`.   

----------------

{{< /description >}}
