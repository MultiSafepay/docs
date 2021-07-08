---
title : "Disputing chargebacks"
weight: 40
meta_title: "Credit card user guide - Disputing chargebacks - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: 
    - /payment-methods/creditcards/chargebacks/dispute-chargeback/
    - /payment-methods/credit-and-debit-cards/creditcards/chargebacks/dispute-chargeback/
---
The table below sets out the process for disputing chargebacks.

|   |   |   |   |   |
|---|---|---|---|---|
| 1. | [Cardholder](/payment-methods/credit-and-debit-cards/user-guide/glossary/#cardholder)  | To find out more about a transaction, the cardholder can file a free [retrieval](/payment-methods/credit-and-debit-cards/user-guide/glossary/#retrieval) request for more information. This can help identify and clarify transactions and avoid chargebacks. {{< br >}} You can still refund the transaction at this stage.  |   
| 2.  | Cardholder  | If the cardholder still disagrees with the transaction, they request a chargeback.  | 
| 3.  | [Issuer](/payment-methods/credit-and-debit-cards/user-guide/glossary/#issuer)  | The issuer usually refunds the cardholder as soon as they request the chargeback. {{< br >}} We don't support refunding chargeback transactions from this point, because then the cardholder likely receives the refund twice. |
| 4.  | Merchant  | You have the right to dispute the chargeback, or MultiSafepay can do so on your behalf. {{< br >}} You must provide evidence that the chargeback is unjustified. {{< br >}} A separate transaction for the chargeback, connected to the original transaction, is created in your MultiSafepay account.  | 
| 5.  | Cardholder  | If the cardholder disagrees with the outcome of the dispute, the chargeback process continues.  | 
| 6.  | Merchant  | You can challenge again, but the potential costs involved are significant. {{< br >}} The card scheme and issuer may both charge fees. {{< br >}} You need to present strong **new** evidence not provided already.  | 
| 7.  | [Card scheme](/payment-methods/credit-and-debit-cards/user-guide/glossary/#card-scheme)  | The card scheme makes the final decision about the chargeback.  | 
| 8.  | Card scheme  | If the chargeback is successful, the card scheme reclaims the amount from MultiSafepay directly.  |  
| 9.  | MultiSafepay  | We debit the amount from your MultiSafepay balance.  |  
 
  
## MultiSafepay disputing on your behalf
MultiSafepay can dispute chargebacks on your behalf for a fee. 

You need to upload relevant [documentary proof](/payment-methods/credit-and-debit-cards/user-guide/chargeback-reasons-and-required-evidence/) either:

- In the **Transaction details** page of the original transaction in your MultiSafepay account, **or**
- Via our API. See API Reference – [Chargebacks](/api/#chargeback), **or**
- By email to <retrieval@multisafepay.com>

The Chargeback Team then assesses the proof and decides whether the chargeback can be disputed.

For questions about disputes, email <retrieval@multisafepay.com>

For more information about fees, email the Support Team at <support@multisafepay.com>

## See also

[Minimizing chargebacks](/payment-methods/credit-and-debit-cards/user-guide/minimizing-chargebacks/)

