---
title: 'Pay After Delivery payment flow'
breadcrumb_title: 'Payment flow'
weight: 30
meta_title: "Pay After Delivery payment flow - MultiSafepay Docs"
short_description: "Flow from start to finish and status change descriptions"
layout: 'child'
logo: '/logo/Payment_methods/Pay_After_Delivery.svg'
url: '/payment-methods/pay-after-delivery/payment-flow/'
aliases:
    - /payments/methods/billing-suite/pay-after-delivery/payment-flow/
---

This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant MF as MultiFactor
    participant Me as Merchant

    C->>Mu: Selects Pay After Delivery at checkout
    Mu->>C: Connects to MultiFactor (direct/redirect)
    MF->>Mu: Authorizes the payment (within 2 business days)
    Mu->>MF: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped! 
    MF->>C: Sends invoice (within 24 hours of Shipped status)
    Note over MF,C: Settlement is now guaranteed!
    C->>MF: Completes payment (within 14 days)
    MF->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 30 days of Shipped status)

{{< /mermaid >}}
&nbsp;  
|  |  |  |
|---|---|---|
| **Direct flow** | The order details are sent directly to MultiFactor. | 
| **Redirect flow** | The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to: {{< br >}} - Agree to the terms and conditions {{< br >}} - Provide their birth date, bank account, email address, and phone number {{< br >}} They are then redirected to your success page. | 

### Failure to pay

If the customer fails to pay within the initial 14 day period, MultiFactor emails them reminders with new payment links, each valid for 6 days: 

- The first and second reminders are free. 
- With the third, we add a fee of 7.50 EUR to the invoice. 
- With the fourth, we add a fee of 12.50 EUR to the invoice. 

If the customer still fails to pay, the total invoice is transferred to a debt collection agency. 

To stop sending reminders, you can either:

- Credit the invoice for a zero amount, or
- Request to place the transaction on hold for up to 1 month

Email requests to place transactions on hold to <klantenservice@multifactor.nl>  
Provide the following information:

- Transaction details
- Reason for your request
- Expected date to start the billing process again

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has initiated a transaction. {{< br >}} You can still cancel it. | Uncleared   | Uncleared | 
| Pay After Delivery has authorized the payment. {{< br >}} You can no longer cancel. You can only refund. {{< br >}} See [Closing transactions](/payments/methods/billing-suite/pay-after-delivery/faq/closing-transactions). | Completed | Uncleared | 
| **Important:** [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). | Shipped | Uncleared |
| The transaction is complete.  | Shipped | Completed |
| The transaction was cancelled. | Void   | Cancelled | 
| The customer did not complete payment within 90 days and the transaction expired. | Expired | Expired | 

## Refund statuses

| Description | Order status | Transaction status |
|---|---|---|
| The customer has requested a refund. | Initialized | Initialized |  
| The refund is complete. | Completed | Completed | 


