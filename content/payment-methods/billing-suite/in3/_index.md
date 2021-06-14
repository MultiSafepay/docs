---
title: 'in3'
weight: 180
meta_title: "Payment methods in3 - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: 'single'
faq: '.'
logo: '/svgs/in3.svg' 
short_description: 'Dutch post-payment solution where customers pay in 3 installments'
aliases:
    - /support-tab/magento2/payment-methods/billing-suite/in3/
    - /payment-methods/billing-suite/in3/activate-in3/
    - /payment-methods/billing-suite/in3/how-does-in3-work/
    - /payment-methods/billing-suite/in3/in3-testing/
    - /payment-methods/billing-suite/in3/refund-in3/
    - /payment-methods/billing-suite/in3/what-is-in3/
---

## About in3

in3 is a Dutch online post-payment solution where customers pay in 3 installments at no extra cost and without having to register with the Bureau Krediet Registratie (BKR). in3 processes all the installments and guarantees payout after receiving the first one. 

|   |   |   |
|---|---|---|
| **Payment type**   | Post-payment method  | |
| **API flow**  | `Direct`/ `Redirect` | [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | The Netherlands  | in3 checks the customer's country, and billing/shipping address to confirm. |
| **Currencies**  | EUR | | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/billing-suite/in3/faq/processing-refunds/) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

### Product rules

* The default minimum order amount is 100 EUR and the default maximum amount is 3000 EUR. You can adjust these limits in the backend of our [ecommerce integrations](/integrations/ecommerce-integrations/) to show or hide in3 on your checkout page depending on the order value.

* Customers can provide different billing and shipping addresses.

## Payment flow

The table below shows a successful in3 payment flow from start to finish.  

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
|  1. | The customer initiates a transaction, is redirected to in3, and enters their details. | Initialized   | Initialized  |
| 2. | in3 conducts a credit check. |   |   |
| 3. | The customer has 5 minutes to pay the first installment, or the transaction is cancelled. {{< br >}} The first installment is required to create the order. | Uncleared  | Initialized  |
| 4. | The customer pays the first installment. {{< br >}} You are now guaranteed the full payout. | Completed  | Uncleared  |
| 5. | Ship the order. | | |
| 6. | MultiSafepay adds the funds to your MultiSafepay balance (within 15 days of the first installment). | Completed | Completed |
| 7. | The customer has 30 days to pay the second installment. |  | |
| 8. | The customer has 60 days to pay the third installment. |  | |


### Other statuses

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| The customer did not pass the credit check and in3 declined the first installment. No order was created.    | Declined   | Declined   |
| The payment was declined or abandoned. | Void    | Void    |

### Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/in3/faq/processing-refunds).

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| in3 has successfully processed a full or partial refund. | Completed    | Completed   |
| in3 has declined a full or partial refund request.  | Declined      | Declined   |

## Activation

To apply for in3, email the Sales Team at <sales@multisafepay.com>

## Integration and testing

To integrate in3 using our API, see API Reference – [in3](/api/#in3).

{{< details title="View credentials and testing process" >}}

Test credentials: [API key](.com/tools/multisafepay-control/get-your-api-key/)

To test in3 transactions, follow these steps:

1. Send a [Direct or redirect](/faq/api/difference-between-direct-and-redirect/) API request.
2. The payment is processed in the test environment as **Successful**, with order status **Completed**, and transaction status **Uncleared**.
3. To change the order status to **Shipped**, either:
    - Send an [Update an order](/api/#update-an-order) API request, or 
    - Change the status in your MultiSafepay Test Control.
{{< br >}}The transaction status remains **Uncleared**.
4. No invoice is generated in the test control so you can't change the transaction (financial) status to **Completed**. Alternatively, in your live MultiSafepay Control, you can initiate the invoice process by changing the order status to **Shipped**, because the order is captured in in3.

You can also test in3 transactions by entering the following details on the in3 checkout page:
| Date of birth    | Postal code | House number |
| ------------------- | ------------------- | ----------------- |
| 01-01-1999 | 1234AB | 1 |
| 01-01-2000 | 1111AB | 1 |

Sample statuses:

- **Approved**
- **Declined**

{{< /details >}}
