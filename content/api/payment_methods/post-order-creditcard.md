---
weight: 306
meta_title: "API - Create Credit Card order - Developers MultiSafepay"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
---

## Credit Cards

> POST - /orders 

```shell 

{
    "type": "direct",
    "order_id": "my-order-id-1",
    "gateway": "CREDITCARD",
    "currency": "EUR",
    "amount": "9743",
    "description": "Test Order Description",
   "payment_options": {
       "notification_url": "http://www.example.com/client/notification?type=notification",
        "redirect_url": "http://www.example.com/client/notification?type=redirect",
        "cancel_url": "http://www.example.com/client/notification?type=cancel", 
        "close_window": ""
    },
    "gateway_info": {
        "card_number": "4012001038443335",
        "card_holder_name": "Test Holder Name",
        "card_expiry_date": "2022",
        "card_cvc": "123"
    },
    "customer": {
        "locale": "en_US",
        "ip_address": "31.148.195.10",
        "forwarded_ip": "",
        "first_name": "John",
        "last_name": "Doe",
        "address1": "Neherkade",
        "house_number": "XI",
        "zip_code": "2521VA",
        "city": "Gravenhage",
        "state": "",
        "country": "NL",
        "email": "test@example.com",
        "referrer": "http://example.com",
        "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
    }
}
```

> JSON Response 

```shell
{
    "transaction_id": 0,
    "order_id": "",
    "created": "",
    "modified": "",
    "recurring_id": "",
    "gateway": "",
    "currency": "",
    "amount": "",
    "description": "",
    "var1": "",
    "var2": "",
    "var3": "",
    "amount_refunded": 0,
    "status": "",
    "financial_status": "",
    "reason": "",
    "reason_code": "",
    "fastcheckout": "",
    "order_total": "",
    "html_form": "",
    "payment_url": "",
    "cancel_url": "",
    "customer": {
        "locale": "",
        "ip_address": "",
        "forwarded_ip": "",
        "referrer": "",
        "user_agent": "",
        "first_name": "",
        "last_name": "",
        "company": false,
        "company_name": "",
        "address1": "",
        "address2": "",
        "house_number": "",
        "zip_code": "",
        "city": "",
        "state": "",
        "country": "",
        "phone": "",
        "email": "",
        "disable_send_email": false
    },
    "gateway_info": {
        "issuer_id": "",
        "account_id": "",
        "account_holder_name": "",
        "account_holder_city": "",
        "account_holder_country": "",
        "account_holder_iban": "",
        "account_holder_swift": "",
        "account_holder_bic": "",
        "personal_number": "",
        "gender": "",
        "phone": "",
        "referrer": "",
        "email": "",
        "user_agent": "",
        "card_number": "",
        "card_holder_name": "",
        "card_expiry_date": "",
        "card_cvc": "",
        "emandate": "",
        "qr_size": "",
        "company": "",
        "po_number": "",
        "coc": "",
        "vat": "",
        "collecting_flow": "",
        "action_on_declined": "",
        "company_type": "",
        "term_url": "",
        "birthday": "",
        "bank_account": ""
    },
    "payment_details": {
        "recurring_id": "",
        "type": "",
        "card_expiry_date": false,
        "last4": false,
        "account_id": "",
        "account_holder_name": false,
        "external_transaction_id": false,
        "account_iban": false,
        "account_bic": false
    },
    "shopping_cart": {
        "items": [
            {
                "name": "",
                "description": "",
                "unit_price": "",
                "currency": "",
                "quantity": 0,
                "created": "",
                "merchant_item_id": "",
                "tax_table_selector": "",
                "cashback": "",
                "image": "",
                "product_url": "",
                "weight": {
                    "unit": 0,
                    "value": ""
                }
            }
        ]
    },
    "checkout_options": {
        "no_shipping_method": false,
        "use_shipping_notification": false,
        "tax_tables": {
            "default": {
                "shipping_taxed": false,
                "rate": "",
                "rules": [
                    {
                        "rate": 0,
                        "country": "",
                        "world_area": false
                    }
                ]
            },
            "alternate": [
                {
                    "standalone": false,
                    "name": "",
                    "rate": "",
                    "rules": [
                        {
                            "rate": 0,
                            "country": "",
                            "world_area": false
                        }
                    ]
                }
            ]
        },
        "rounding_policy": [
            {
                "mode": "",
                "rule": ""
            }
        ],
        "shipping_methods": [
            {
                "flat_rate_shipping": [
                    {
                        "name": "",
                        "price": "",
                        "currency": "",
                        "allowed_areas": null,
                        "excluded_areas": null,
                        "id": "",
                        "type": "",
                        "provider": ""
                    }
                ],
                "pickup": [
                    {
                        "name": "",
                        "price": "",
                        "currency": "",
                        "id": "",
                        "type": "",
                        "provider": ""
                    }
                ]
            }
        ]
    },
    "order_adjustment": {
        "total_adjustment": "",
        "total_tax": ""
    },
    "costs": [
        {
            "transaction_id": 0,
            "description": "",
            "type": "",
            "amount": "",
            "status": "",
            "created": ""
        }
    ]
}
```

* All parameters shown are required field(s)

| Parameter                       | Type     | Description                                                                             |
|---------------------------------|----------|-----------------------------------------------------------------------------------------|
| type                            | string | Specifies the payment flow for the checkout process. Options: direct.                   |
| gateway                         | string | The unique gateway id to immediately direct the customer to the payment method. You retrieve these gateways using a gateway request. Options: [CREDITCARD](/payment-methods/creditcards/credit-card-payment-page/), VISA, MASTERCARD, MAESTRO, AMEX. |
| order_id                        | string | The unique identifier from your system for the order.                                   |
| currency                        | string | The currency [ISO-4217](https://www.iso.org/iso-4217-currency-codes.html) you want the customer to pay with. |
| amount                          | integer | The amount (in cents) that the customer needs to pay.                                     |
| description                     | string | A text which will be shown with the order in MultiSafepay Control. If the customer's bank supports it this will also be shown on the bank statement. Max. 200 characters. HTML is no longer supported. Use the 'items' or 'shopping_cart' objects for this. |
| payment_options                 | object | Contains the redirect_url, cancel_url and [notification_url](/faq/api/how-does-the-notification-url-work/).                             |
| customer                        | object | Contains the personal information of the customer.                                      |
| gateway_info                    | object | Contains the extra card information.                                                    |
| card_number                     | string | Full credit card number.                                                                |
| card_holder_name                | string | Name on credit card.                                                                    |
| card_expiry_date                | string | Card expiry date.                                                                        |
| card_cvc                        | string | Card CVC number. This might vary depending of the card type. Some cards like MAESTRO may not be required. |
| ip_address                      | string  | The IP address of the customer. "Required" with post payment and credit card payment methods. Due to validation of the customer IP address, we need to receive the actual IP address of the end user within the ip_address field. [More info](/faq/api/ip_address/)                                                                                               |
| forwarded_ip                    | string  | The X-FORWARDED-FOR header of the customer request when using a proxy. [More info](/faq/api/ip_address/)                                                                                                                           |


Please make sure you check out our dedicated documentation for [credit cards](/payment-methods/creditcards/)