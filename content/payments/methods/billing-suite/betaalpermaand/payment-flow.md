---
title: 'Betaal per Maand payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Betaal per Maand payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
---

The table below shows a successful payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}
&nbsp;  
- Order status: the progression of the customer's order with you, independent of the payment
- Transaction status: the progression towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
| 1. | The customer selects Betaal per Maand at checkout and initiates a transaction. {{< br >}} To cancel the transaction at this point, email <support@multisafepay.com> | Uncleared   | Initialized  |
| 2. | Betaal per Maand authorizes the payment. | Uncleared   | Uncleared  |
| 3. | Once authorized, MultiSafepay sends a capture to Betaal per Maand. {{< br >}} The transaction appears in both your MultiSafepay account and your [backend](/getting-started/glossary/#backend) via the [notification URL](/developer/api/notification-url/). {{< br >}} You **can** cancel the transaction at this point. | Completed  | Uncleared  |
| 4. | Ship the order. {{< br >}} **Important:** You **must** manually [change the order status to Shipped](/payments/methods/billing-suite/betaalpermaand/user-guide/changing-order-status-to-shipped/) in your MultiSafepay account.  | Shipped | Uncleared | 
| 5. | [Provide the track-and-trace code](/payments/methods/billing-suite/betaalpermaand/faq/providing-track-and-trace/) to MultiSafepay. | | |
| 6. | MultiSafepay sends the track-and-trace code to Betaal per Maand to confirm shipment. | | |
| 7. | Betaal per Maand invoices the customer. Settlement is now guaranteed.  | | |
| 8. | The customer selects their preferred period and payment method for the monthly payment to Betaal per Maand. | | |
| 9. | Betaal per Maand settles the funds with MultiSafepay within 5 business days after the order status changes to **Shipped**. | Shipped    | Completed  |
| 10. | MultiSafepay settles the funds in your MultiSafepay balance within 5 business days.| | |

## Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description | Order status | Transaction status |
|---|---|---|
| Betaal per Maand has declined the payment. Betaal per Maand only provides the reason directly to the customer, for privacy and compliance reasons. | Declined   | Declined   |
| The payment was cancelled.   | Void   | Cancelled   |
| The customer did not complete the payment within the 1-day period and the transaction expired. | Expired    | Expired    |

## Refund statuses

| Description   | Order status      | Transaction status |
|----|----|---|
| The customer has requested a refund. | Reserved    | Reserved   |
| The refund was successfully processed.  | Completed      | Completed   |

