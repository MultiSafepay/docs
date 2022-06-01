---
title : "Disputing chargebacks"
weight: 40
meta_title: "Disputing chargebacks - MultiSafepay Docs"
read_more: "."
short_description: "To dispute a chargeback, provide evidence that the chargeback is unjustified"
url: "/chargebacks/disputing/"
aliases: 
    - /payment-methods/creditcards/chargebacks/dispute-chargeback/
    - /payment-methods/credit-and-debit-cards/creditcards/chargebacks/dispute-chargeback/
    - /payments/chargebacks/disputing
---
The table below sets out the process for disputing chargebacks.

|   |   |   |   |   |
|---|---|---|---|---|
| 1. | [Cardholder](/glossaries/credit-cards/#cardholder)  | To find out more about a transaction, the cardholder can file a free [retrieval](/credit-cards-user-guide/glossary/#retrieval) request for more information. This can help identify and clarify transactions and avoid chargebacks. {{< br >}} You can still refund the transaction at this stage.  |   
| 2.  | Cardholder  | If the cardholder still disagrees with the transaction, they request a chargeback.  | 
| 3.  | [Issuer](/glossaries/credit-cards/#issuer)  | The issuer usually refunds the cardholder as soon as they request the chargeback. {{< br >}} We don't support refunding chargeback transactions from this point, because then the cardholder likely receives the refund twice. |
| 4.  | Merchant  | MultiSafepay can dispute the chargeback on your behalf. {{< br >}} You must provide evidence that the chargeback is unjustified. {{< br >}} A separate transaction for the chargeback, connected to the original transaction, is created under your MultiSafepay account.  | 
| 5.  | Cardholder  | If the cardholder disagrees with the outcome of the dispute, the chargeback process continues.  | 
| 6.  | Merchant  | You can dispute again, but the potential costs involved are significant. {{< br >}} The card scheme may charge fees. {{< br >}} You need to present strong **new** evidence not provided already.  | 
| 7.  | [Card scheme](/glossaries/credit-cards/#card-scheme)  | The card scheme makes the final decision about the chargeback.  | 
| 8.  | Card scheme  | If the chargeback is unsuccessful, the card scheme reclaims the amount from MultiSafepay directly.  |  
| 9.  | MultiSafepay  | We debit the amount from your MultiSafepay balance.  |  
 
  
## MultiSafepay disputing on your behalf
MultiSafepay can dispute chargebacks on your behalf for a fee. 

You need to upload relevant [documentary proof](/payments/chargebacks/reasons/) either:

- In the **Transaction details** page of the original transaction in your MultiSafepay dashboard, **or**
- Via our API, see API reference – [Challenge chargebacks](https://docs-api.multisafepay.com/reference/challengechargeback), **or**
- By email to <retrieval@multisafepay.com>

The Chargeback Team then assesses the proof and decides whether the chargeback can be disputed.

For questions about disputes, email <retrieval@multisafepay.com>

For more information about fees, email <support@multisafepay.com>

## See also

[Minimizing chargebacks](/payments/chargebacks/minimizing/)

