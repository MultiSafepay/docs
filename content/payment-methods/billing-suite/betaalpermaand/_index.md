---
title: 'Betaal per Maand'
weight: 210
meta_title: "Payment methods - Betaal per Maand - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
layout: 'single'
faq: '.'
logo: '/logo/Payment_methods/betaalpermaand.svg' 
short_description: 'Dutch buy now pay later service with Santander based on a one-off post-payment or monthly installments.'
aliases:
    - /support-tab/magento2/payment-methods/betaalplan
    - /payment-methods/billing-suite/betaalplan
    - /payment-methods/betaalplan/
    - /payment-methods/betaalpermaand/activate-betaalplan
    - /payment-methods/betaalpermaand/betaal-per-maand-testing
    - /payment-methods/betaalpermaand/how-does-betaalplan-work
    - /payment-methods/betaalpermaand/refund-betaalplan
    - /payment-methods/betaalpermaand/what-is-betaalplan
---

## About Betaal per Maand
Betaal per Maand is an online buy now pay later service offered in collaboration with Santander. MultiSafepay is the only payment service provider that supports Betaaal per Maand online.

Customers pay for orders after receiving them as a one-off post-payment or in monthly installments. They are only charged for the items they keep from the order. 

Betaal per Maand bears the risk and guarantees payout. 


|   |   |   |
|---|---|---|
| **Payment type**   | Buy now pay later  | |
| **API flow**  | `Direct`| [More information](/faq/api/difference-between-direct-and-redirect) |
| **Countries**  | The Netherlands  | |
| **Currencies**  | EUR | [More information](https://docs.multisafepay.com/faq/general/supported-currencies/) | 
| **Refunds**  | Full and partial  | [More information](/payment-methods/billing-suite/betaalpermaand/faq/processing-refunds/) | 
| **Recurring payments**  | No | [More information](/tools/recurring-payments)  |
| **Chargebacks**  | No | [More information](/faq/chargebacks)  |

### Product rules

- You cannot [adjust payment link lifetimes](/faq/api/lifetime-of-a-payment-link).

- See also User guide – [Known errors](/payment-methods/billing-suite/betaalpermaand/faq/known-errors/).

{{< details title="Gift cards" >}}
&nbsp;  
Post-payment methods do not generally support entering [gift card](/payment-methods/prepaid-cards/gift-cards) details **after** the order is placed (for a whole or partial payment). This is because, as the collecting party, Klarna requires very precise order specifications. 

Our platform would interpret the gift card as a discount (not included in the shopping cart specification) and wouldn't generate the correct order information, e.g. for tax purposes. 

Customers can enter gift card details **before** placing the order, i.e. on your checkout page, before the API request. You are solely responsible for enabling this feature. Failure to follow this rule so can produce unexpected errors and complications.

{{< /details >}}

## Payment flow

The table below shows a successful Betaal per Maand payment flow from start to finish.  

In your MultiSafepay Control > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
|  1. | The customer initiates a transaction. {{< br >}} Betaal per Maand has not yet received payment. {{< br >}} You cannot reject orders at this stage. | Uncleared   | Initialized  |
|  2. | Betaal per Maand approves or declines the transaction. | Uncleared   | Uncleared  |
| | The transaction is successful. {{< br >}} You can reject orders at this stage. | Completed  | Uncleared  |
|  | The transaction appears in both your MultiSafepay Control and the backend of your ecommerce integration via the [Notification URL](/faq/api/notification-url/). | | |
| 3. | Ship the order. | | |
| 4. | [Change the order status to Shipped](/payment-methods/billing-suite/betaalpermaand/faq/changing-order-status-to-shipped/).  | Shipped | Uncleared | 
| 5. | [Provide the track-and-trace code](/payment-methods/billing-suite/betaalpermaand/faq/providing-track-and-trace/) to MultiSafepay. | | |
| 6. | MultiSafepay sends the track-and-trace code to Betaal per Maand to confirm shipment. | | |
| 7. | MultiSafepay sends a capture to Betaal per Maand. |  |  |
| 8. | Betaal per Maand confirms the transaction. | | |
| 9. | Betaal per Maand sends the customer an invoice. Your payout is now guaranteed.  | | |
| 10. | The customer selects their preferred period and payment method for the monthly payment to Betaal per Maand. | | |
| 11. | Betaal per Maand pays the funds to MultiSafepay within 5 business days after the order status changes to **Shipped**. | Shipped    | Completed  |
| 12. | MultiSafepay adds the funds to your MultiSafepay balance within 5 business days.| | |

### Return process 
If the customer returns some items from the order, you can [pauze the collection period](/payment-methods/billing-suite/betaalpermaand/faq/pauzing-collection-period/) for 2 to 4 weeks.

### Other statuses

| Description | Order status | Transaction status |
|---|---|---|
| Betaal per Maand has rejected the transaction. Betaal per Maand only provides the reason directly to the customer, for privacy and compliance reasons. | Declined   | Declined   |
| The transaction was cancelled.   | Void   | Cancelled   |
| The customer did not complete the transaction, and it expired. | Expired    | Expired    |

### Refund statuses

For how to process refunds, see [Processing refunds](/payment-methods/billing-suite/betaalpermaand/#processing-refunds).

| Description                      | Order status      | Transaction status |
|--------------------------------|-----------|-----------------------------------------------------------------------------------------|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |

### Activation

**1.** To apply for Betaal per Maand:

**Note:** If you already have an active working relationship with Santander for any other product, you are considered a Santander client.

| MultiSafepay account | Santander account | Step | Instructions |
|---|---|---|---|
| Yes   | No  | 1. | Email your application to your account manager at <sales@multisafepay.com> |
|   |  | 2. | MultiSafepay checks your connection and your eligibility. |
|   |  | 3. | MultiSafepay submits your application to Betaal per Maand. |
| No  | No | 1. | [Create a MultiSafepay account](/guides/getting-started/). |
|   |  | 2. | MultiSafepay submits your application to Betaal per Maand during your onboarding process. |
| No  | Yes | 1. | [Create a MultiSafepay account](/guides/getting-started/) or email your account manager at <sales@multisafepay.com> |

{{< details title="View eligibility criteria" >}}

To be eligible for Betaal per Maand, you must:

- Be registered with a Dutch Chamber of Commerce (no exceptions)
- Have an annual turnover of more than 500,000 EUR (unless agreed otherwise with Betaal per Maand)
- Sell products or services to European citizens with a residential or delivery address in Netherlands (no exceptions)
- Be able to connect to MultiSafepay via our API or [ecommerce integrations](/integrations/ecommerce-integrations/)

The following order amounts also apply:

- Minimum order amount 250 EUR
- Maximum order amount 8000 EUR

{{< /details >}}

**2.** To activate Betaal per Maand, email the Sales Team at <sales@multisafepay.com>

## Integration and testing

To integrate Betaal per Maand using our API, see API Reference – [Betaal per Maand](/api/#santander-betaal-per-maand).

{{< details title="View testing process" >}}

You cannot test Betaal per Maand in MultiSafepay Test Control. 

When activating Betaal per Maand as a payment method in your live MultiSafepay Control, you can test it before going live.

{{< /details >}}

