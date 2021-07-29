---
weight: 210
meta_title: "API Reference - Create a redirect order - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
---
{{< code-block >}}
> POST - /orders

```json
{
    "type": "redirect",
    "order_id": "my-order-id-1",
    "gateway": "",
    "currency": "EUR",
    "amount": 1000,
    "description": "Test Order Description",
    "google_analytics": { 
      "account": "UA-XXXXXXXXX" 
      },
    "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": true
    },
    "customer": {
        "locale": "nl_NL",
        "ip_address": "123.123.123.123",
        "first_name": "Simon",
        "last_name": "Smit",
        "company_name": "Test Company Name",
        "address1": "Kraanspoor",
        "house_number": "39C",
        "zip_code": "1033SC",
        "city": "Amsterdam",
        "country": "NL",
        "phone": "0208500500",
        "email": "simonsmit@example.com",
        "referrer": "https://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    },
    "second_chance": {
        "send_email" : true
    }
}

```


> JSON Response


```json
{
  "success": true,
  "data": {
    "order_id": "My-order-id-1",
    "payment_url": "https://payv2.multisafepay.com/connect/99wi0OTuiCaTY2nwEiEOybWpVx8MNwrJ75c/?lang=nl_NL"
  }
}
```
{{< /code-block >}}

{{< description >}}
## Create a redirect order

This is the default type of order.

**Parameters**

----------------

__type__ | string

The payment flow for the checkout process.  
Options: `redirect`, `direct`, `checkout`, `paymentlink`.

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
__google_analytics__ | object

Your Google Analytics site ID, which is injected into the payment page so you can trigger custom events and track payment metrics. Optional.  
For more information, see [Google Analytics tracking via the API](/developer/api/google-analytics-tracking).

----------------
__account__ | string

The Google Analytics Tracking-ID. See your Google Analytics dashboard. 

----------------
__redirect_url__ | string

The page the customer is redirected to after completing payment.   
If the transaction status changes to [**Uncleared**](/payments/methods/credit-and-debit-cards/user-guide/evaluating-uncleared-transactions/), the customer is also redirected to your thank-you page.   
**Note:** Customers never see an **Uncleared** status. They always experience the payment as successful.

----------------
__cancel_url__ | string

The page the customer is redirected to if the payment fails.

----------------
__customer__ | object

The customer's personal information.   
Format: Minimum two characters for the `first_name` and `last_name`.  
We recommend always requiring the customer to provide their full name, instead of initials or abbreviations.

----------------
__locale__ | string

Displays the correct language and payment methods on the payment page, and influences sending email templates.  Format: ab_CD with [ISO 639 language codes](https://www.iso.org/iso-639-language-codes.html) and [ISO 3166 country codes](https://www.iso.org/iso-3166-country-codes.html).  
Default: `en_US`.

----------------
__ip_address__ | object

The customer's IP address.  
Recommended for [post-payment](/payments/methods/billing-suite/) and [credit card](/payments/methods/credit-and-debit-cards/) payment methods. MultiSafepay [validates customer IP addresses](/developer/api/validating-customer-ip-address) to help detect fraudulent payments.

----------------
__first_name__ | string

The customer’s first name.   

----------------
__last_name__ | string

The customer’s last name.   

----------------
__address1__ | string

The first line of the customer's address.

----------------
__house_number__ | string

The customer's house number.

----------------
__zip_code__ | string

The customer's ZIP/ postal code. 

----------------
__city__ | string

The customer's city of residence.     

----------------
__country__ | string

The customer’s country of residence.  
Format: [ISO 3166-1](https://www.iso.org/iso-3166-country-codes.html).

----------------
__phone__ | string

The customer's phone number.  

----------------
__email__ | string

The customer’s email address.  
Used to send Second Chance emails and to conduct fraud checks.

----------------

__close_window__ | bool (optional)

To display the MultiSafepay payment page in a new window that automatically closes after the customer completes payment, set to `True`.    
Options: `True`, `False`. 

----------------

{{% /description %}}
