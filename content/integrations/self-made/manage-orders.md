---
title: 'Manage orders'
breadcrumb_title: "Manage orders"
layout: 'single'
meta_title: 'Build your integration – Manage orders - MultiSafepay Docs'
logo: '/svgs/Wrappers.svg'
short_description: 'Manage orders in your own integration'
weight: 1
url: '/integrations/self-made/manage-orders/'
---

MultiSafepay provides a [RESTful API](/glossaries/multisafepay-glossary/#restful-api-application-programming-interface) that can be accessed by HTTP requests to manage your data. We support data in JSON format only.

The most important data element in our API is the **order**. Orders contain all information related to a single instance of products and/or services sold to a customer. 

Orders can be linked to multiple **transactions**. A transaction represents an instance of funds being transferred.

The most common operation to perform with our API is creating an order. To specify which payment flow the customer experiences for that order, set the order `type` to `direct` or `redirect`.

|  |  |  |
|---|---|---|
| **Direct** | The customer selects their payment method in your embedded checkout. | 
| **Redirect** | The customer is redirected first to a [payment page](/payment-pages/) to select their payment method. | 

## Prerequisites

Before making any API requests, you must:

- Have a [site API key](/websites/#site-id-api-key-and-security-code).
- Choose the test or live [environment](https://docs-api.multisafepay.com/reference/environments).

You must include your API key in the request URL as a query parameter to be able to authenticate your request.  

While building your integration we recommend using the test environment: `https://testapi.multisafepay.com/v1/json`.


## Create an order

The first operation to test when building your integration, is to [create an order](https://docs-api.multisafepay.com/reference/createorder). Here is a sample request to create a redirect order:

```
curl -X POST "https://testapi.multisafepay.com/v1/json/orders?api_key={your-test-api-key}" \
-H 'Content-Type: application/json' \
-H 'accept: application/json' \
-d '{
  "type": "redirect",
  "order_id": "my-order-id-1",
  "gateway": "",
  "currency": "EUR",
  "amount": 1000,
  "description": "Test order description",
  "payment_options": {
    "notification_url": "https://www.example.com/client/notification?type=notification",
    "notification_method": "POST",
    "redirect_url": "https://www.example.com/client/notification?type=redirect",
    "cancel_url": "https://www.example.com/client/notification?type=cancel",
    "close_window": true
  },
  "customer": {
    "locale": "nl_NL",
    "ip_address": "123.123.123.123",
    "first_name": "John",
    "last_name": "Doe",
    "company_name": "Test Company Name",
    "address1": "Kraanspoor",
    "house_number": "39C",
    "zip_code": "1033SC",
    "city": "Amsterdam",
    "country": "NL",
    "phone": "0208500500",
    "email": "jdoe@example.com",
    "referrer": "https://example.com",
    "user_agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36"
  }
}'
```

Check that you receive a response with `success` set to `true`:
```
{
  "success": true,
  "data": {
    "order_id": "my-order-id-1",
    "payment_url": "https://example.com/?lang=nl_NL"
  }
}
```
If you receive an error in the response, see [Handling errors](/errors/handling-errors/).

Otherwise, open the `payment_url` to complete the payment on the payment page. 

For further details on how to test each payment method, see [Test payment details](/testing/test-payment-details/). If this is your first time, we recommend following the steps for [iDEAL](/testing/#details-ideal).

## Get order details

To familiarize yourself with what an order looks like in our system, try making a [Get order](https://docs-api.multisafepay.com/reference/getorder) request for the order you just created, using the `order_id`.

```
curl -X GET 'https://testapi.multisafepay.com/v1/json/orders/my-order-id-1?api_key={your-test-api-key}' \ 
-H 'accept: application/json'
```
You should receive a response like this:
```
{
  "success": true,
  "data": {
    "amount": 100,
    "amount_refunded": 0,
    "costs": [
      {
        "amount": 0.00,
        "description": "0.00 For iDEAL Transactions",
        "transaction_id": 1234567,
        "type": "SYSTEM"
      }
    ],
    "created": "2021-12-07T15:56:32",
    "currency": "EUR",
    "custom_info": {
      "custom_1": null,
      "custom_2": null,
      "custom_3": null
    },
    "customer": {
      "address1": "Kraanspoor",
      "address2": null,
      "city": "Amsterdam",
      "country": "NL",
      "country_name": null,
      "email": "jdoe@example.com",
      "first_name": "John",
      "house_number": "39C",
      "last_name": "Doe",
      "locale": "nl_NL",
      "phone1": "0208500500",
      "phone2": "",
      "state": null,
      "zip_code": "1033SC"
    },
    "description": "Test Order Description",
    "fastcheckout": "NO",
    "financial_status": "completed",
    "items": null,
    "modified": "2021-12-07T15:56:40",
    "order_id": "my-order-id-1",
    "payment_details": {
      "account_bic": "INGBNL2A",
      "account_holder_name": "Jan Jansen",
      "account_iban": "NL87ABNA0000000001",
      "account_id": 1,
      "external_transaction_id": "3749936454986553",
      "issuer_id": "0031",
      "recurring_flow": null,
      "recurring_id": "998107705729622024",
      "recurring_model": null,
      "type": "IDEAL"
    },
    "payment_methods": [
      {
        "account_bic": "INGBNL2A",
        "account_holder_name": "Jan Jansen",
        "account_iban": "NL87ABNA0000000001",
        "account_id": 1,
        "amount": 100,
        "currency": "EUR",
        "description": "Test Order Description",
        "external_transaction_id": "3749936454986553",
        "payment_description": "iDEAL",
        "status": "completed",
        "type": "IDEAL"
      }
    ],
    "reason": "",
    "reason_code": "",
    "related_transactions": null,
    "status": "completed",
    "transaction_id": 2345678,
    "var1": null,
    "var2": null,
    "var3": null
  }
}
```
The most important parameter is `status`, which represents the [status of the order](/about-payments/multisafepay-statuses/), i.e. the progression of the customer’s order with you. 

The second most important parameter is `financial_status`, which represents the [status of the transaction](/about-payments/multisafepay-statuses/), i.e. the progression towards settling the funds in your account balance.

We recommend that you track the `status` parameter in your integration to understand how your order is progressing. For a detailed overview of the possible statuses, see [Status meanings](/payments/multisafepay-statuses/#status-meanings).

In this example, the `status` is **Completed**. This means that the customer has completed payment and settlement is guaranteed. The `financial_status` is also **Completed**. This means that the funds have been settled in your account balance.

Now that you know how to create an order and check its details, and know what is important to look for, it's the perfect time to introduce you to our webhook.

So that you don't have to continually poll our server to see if there are updates to your orders, we provide a webhook to send you notifications automatically. In the next section we explain what you need to do to configure this to work with your web server.

## Next steps

{{< two-buttons
href-1="/integrations/self-made" header-1="Overview" text-1="Self-made integrations" img-1="/svgs/arrow-thin-left.svg" alt-1="Left arrow" 

href-2="/integrations/self-made/configure-your-webhook" header-2="Next" text-2="Configure your webhook endpoint" img-2="/svgs/arrow-thin-right.svg" alt-2="Right arrow" >}}


