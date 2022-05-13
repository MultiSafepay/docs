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

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant MF as MultiFactor
    participant Me as Merchant

    C->>Mu: Selects Pay After Delivery at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page <br> to provide their birth date, email address, bank account and phone numbers, <br> and accept the terms & conditions, <br> then redirects to your success page
    else Direct flow
    Mu->>MF: Sends order details
    end
    MF->>Mu: Authorizes the payment (within 2 business days)
    Mu->>MF: Captures the funds
    Me->>C: Ships the order
    Note over Me,C: Manually change the order status to Shipped.
    MF->>C: Sends invoice (within 24 hours of Shipped status, settlement is now guaranteed)
    C->>MF: Completes payment (within 14 days)
    MF->>Mu: Transfers funds 
    Mu->>Me: Settles funds (within 30 days of Shipped status)

{{< /mermaid >}}
&nbsp;  

### Failure to pay

If the customer fails to pay within the initial 14 day period, MultiFactor emails them reminders with new payment links, each valid for 6 days: 

- The first and second reminders are free. 
- With the third, we add a fee of 7.50 EUR to the invoice. 
- With the fourth, we add a fee of 12.50 EUR to the invoice. 

If the customer still fails to pay, the total invoice is transferred to a debt collection agency. 

To stop sending reminders, you can either:

- Credit the invoice for a zero amount, or
- Request to place the transaction on hold for up to 1 month

Email a request to place transactions on hold to <klantenservice@multifactor.nl>  
Provide the following information:

- Transaction details
- Reason for your request
- Expected date to start the billing process again

## Payment statuses

{{< details title= "Payment statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [Payment statuses](/payments/payment-statuses/).

{{< /details >}}

| Payments | Order status | Transaction status |
|---|---|---|
| MultiSafepay's risk analysis is in progress. {{< br >}} You can still cancel. | Initialized | Initialized | 
| We have authorized the transaction. {{< br >}} You can no longer cancel. You can only refund. {{< br >}} See also [Closing transactions](/payment-methods/pay-after-delivery/closing-transactions/). | Completed | Uncleared | 
| **Important:** [Manually change the order status to Shipped](/about-payments/pay-later-shipped-status/). | Shipped | Uncleared |
| MultiSafepay has collected payment.  | Shipped | Completed |
| The transaction was cancelled. | Void/Cancelled   | Void/Cancelled | 
| MultiSafepay declined the transaction. | Declined | Declined |
| The customer didn't complete payment within 90 days. | Expired | Expired | 
|**Refunds**|||
| Refund initiated. | Initialized | Initialized |  
| Refund complete. | Completed | Completed | 


