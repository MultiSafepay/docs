---
title: 'Klarna payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Klarna payment flow - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
short_description: "Flow from start to finish, including order and transaction status changes"
layout: 'child'
logo: '/logo/Payment_methods/Klarna.svg'
---

The table below shows a successful Betaal per Maand payment flow from start to finish.  

{{< details title="About order and transaction statuses" >}}

In your MultiSafepay account > **Transaction overview** > **Transaction details** page under **Status history**, there are two statuses that change as the flow progresses: 

- Order status: indicates the status of the customer's order with the merchant independent of the payment
- Transaction status: indicates the status of the payment

{{< /details >}}

### Payment flow

|                       | Flow      | Order status | Transaction status |
|--------------------------------|-----------|---|-----------------------------------------------------------------------------------------|
|  1. | The customer initiates a transaction. | Uncleared   | Initialized  |
|  2. | Betaal per Maand authorizes the payment. | Uncleared   | Uncleared  |
| 3. | Once authorized, MultiSafepay sends a capture to Betaal per Maand. | Completed  | Uncleared  |
|  | The transaction appears in both your MultiSafepay Control and the backend of your ecommerce integration via the [Notification URL](/faq/api/notification-url/). | | |
| 4. | Ship the order. | | |
| 5. | [Change the order status to Shipped](/payment-methods/billing-suite/betaalpermaand/faq/changing-order-status-to-shipped/).  | Shipped | Uncleared | 
| 6. | [Provide the track-and-trace code](/payment-methods/billing-suite/betaalpermaand/faq/providing-track-and-trace/) to MultiSafepay. | | |
| 7. | MultiSafepay sends the track-and-trace code to Betaal per Maand to confirm shipment. | | |
| 8. | Betaal per Maand invoices the customer. Settlement is now guaranteed.  | | |
| 9. | The customer selects their preferred period and payment method for the monthly payment to Betaal per Maand. | | |
| 10. | Betaal per Maand settles the funds with MultiSafepay within 5 business days after the order status changes to **Shipped**. | Shipped    | Completed  |
| 11. | MultiSafepay adds the funds to your MultiSafepay balance within 5 business days.| | |

### Unsuccessful statuses
You can cancel payments before the funds are captured. After the funds are captured you can only process a refund.

| Description | Order status | Transaction status |
|---|---|---|
| Betaal per Maand has declined the payment. Betaal per Maand only provides the reason directly to the customer, for privacy and compliance reasons. | Declined   | Declined   |
| The payment was cancelled.   | Void   | Cancelled   |
| The customer did not complete the payment, and it expired. | Expired    | Expired    |

For refund statuses, see [Processing refunds](/payment-methods/billing-suite/betaalpermaand/user-guide/processing-refunds).

