---
title : "Card payment flow"
weight: 1
layout: 'single'
meta_title: "Card payment flow - MultiSafepay Docs"
short_description: "Flow and statuses from start to finish."
read_more: "."
url: '/payment-methods/credit-debit-cards/payment-flow/'
aliases:
    - /payment-methods/credit-and-debit-cards/american-express/how-does-american-express-work/
    - /payments/methods/credit-and-debit-cards/american-express/payment-flow/
    - /payment-methods/amex/payment-flow/
    - /payments/methods/credit-and-debit-cards/cartes-bancaires/payment-flow/
    - /payment-methods/cartes-bancaires/payment-flow/
---
This diagram shows the flow for a successful transaction.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant A as American Express
    participant Me as Merchant
    participant CB as Customer's bank

    C->>Mu: Selects credit/debit card at checkout
    Mu->>C: Connects to card scheme (redirect only)
    C->>A: Enters payment details, passes 3D Secure authentication, <br> and completes payment
    Mu->>Me: Runs fraud filter and provides risk report
    Me->>Mu: Authorizes transaction
    alt MultiSafepay collects
        CB->>Mu: Transfers funds 
        Mu->>Me: Settles funds
    else With American Express MID
        CB->>A: Transfers funds
        A->>Me: Settles funds
    end
    
{{< /mermaid >}}
&nbsp;  
**Redirect flow:** The customer is redirected to a [MultiSafepay payment page](/payment-pages/) to complete payment.  
**Direct flow:** To process direct card payments, see [Handling cardholder data](/features/handling-cardholder-data/).

### American Express merchant account number

If you use your American Express merchant account number:
    
- American Express settles the funds directly in your business bank account.
- You are automatically added to the Safekey directory. 
- All currencies are supported.  
  
For more information, email the Support Team at <support@multisafepay.com>

## Payment statuses

{{< details title= "About order and transaction statuses" >}}

**Order status:** Changes as the customer's order with you progresses towards shipment (independent of payment)

**Transaction status:** Changes as the funds progress towards settlement in your MultiSafepay balance

For more information, see [About MultiSafepay statuses](/about-payments/multisafepay-statuses/).

{{< /details >}}

| Description | Order status | Transaction status |
|---|---|---|
| The customer has been redirected to 3D Secure and the card scheme is authorizing the transaction. | Initialized | Initialized |
| **AMEX collecting flow:** {{< br >}} 3D Secure authentication was sucessful. American Express collects. | Completed | Initialized |
| 3D Secure authentication was sucessful, but the transaction is flagged for potential fraud risk. [Manually capture or decline the transaction](/about-payments/uncleared-transactions/). | Uncleared | Uncleared |
| 3D Secure authentication successful and MultiSafepay has collected payment. | Completed | Completed |
| Payment wasn't captured manually or within 5 days. | Void | Void/Cancelled |
| The customer didn't complete 3D Secure authentication within 1 hour. | Expired | Expired |
| The customer failed 3D Secure authentication or cancelled the payment. {{< br >}} See [Declined status](/payment-methods/credit-debit-cards/payment-flow/#declined-status) below. | Declined | Declined   |

## Declined status

Here are some reasons why a card payment may be declined. Only the customer can contact their card issuer to find out the specific reason.

- Our automated fraud filter declined the transaction. Email <support@multisafepay.com> 
- Do not honor: The reason is not shared with MultiSafepay. The cardholder must contact the issuer.
- 3D authentication failed
- The card has expired.
- The customer has insufficient credit on their card to complete payment. 
- You currently mandate 3D&nbsp;Secure. See [Flexible 3D](/features/3d-secure/flexible/) and [Dynamic 3D](/features/3d-secure/dynamic/).

For any questions, email the Support Team at <support@multisafepay.com>

## Refund/chargeback statuses

| Description | Order status | Transaction status |
|---|---|---|
| The refund/chargeback is initiated. | Reserved    | Reserved   |
| The refund/chargeback is complete.  | Completed      | Completed   |



