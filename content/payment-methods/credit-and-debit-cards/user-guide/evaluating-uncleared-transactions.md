---
title : "Evaluating Uncleared transactions"
weight: 70
meta_title: "Credit card user guide - Evaluating Uncleared transactions - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
read_more: "."
aliases: 
    - /faq/finance/evaluating-uncleared-card-transactions/
    - /faq/risk-and-fraud/accepting-uncleared-credit-card-payments/
---

If the transaction status of a credit card payment is **Uncleared**, it means that MultiSafepay's automated fraud filter has placed the payment on hold. The fraud filter detects increased **risk** of fraud, but doesn't prevent all fraudulent payments. Not every payment the filter places on hold is necessarily fraudulent.

There are risks associated with accepting credit card payments. You bear the risk of financial damage (e.g. due to fraud), for which neither MultiSafepay nor the cardholder is accountable.

You must review and evaluate all **Uncleared** transactions, and either authorize or decline them.

## Fraud score 
All **Uncleared** transactions are assigned a fraud score from 1-10 (10 being the most at risk of fraud). Transactions that score 10 aren't always fraudulent, and low-scoring transactions may still carry risk.

Transactions that score 6 to 8 you can accept or decline yourself in MultiSafepay account following the steps below.

Transactions that score 8 or above can can only be approved by MultiSafepay. For help with evaluating potential risks or fraud indicators, and professional advice, email the Risk Team at <risk@multisafepay.com> 

The final decision to authorize or decline transactions lies with you. MultiSafepay is not responsible nor liable for any damage after you authorize a payment.

## Reviewing Uncleared transactions

When Uncleared transactions are awaiting your approval, you receive notification in your MultiSafepay account and by email to the address provided under **Contact details** in your account.

{{< blue-notice >}} **Note:** You can only authorize or decline **Uncleared** transactions in your MultiSafepay account. If you take no action, the transaction automatically expires after 5 days. {{< /blue-notice >}}

To view the list of uncleared payments, click on the notification, or:

1. Sign in to your MultiSafepay account.
2. Go to **Transactions** > **Uncleared transactions**.
3. Click each transaction in the list to view the **Transaction details** page. 

The **Transaction details** page includes:

- Basic information about the transaction
- A fraud score
- A risk summary (righthand side). For a detailed risk report, click **More information**.
- If the customer is enrolled for 3D Secure 
- Buttons to **Accept** or **Decline** the transaction
- History data
- Transaction notes 

## Evaluating Uncleared transactions
The following indicators paint a cumulative picture of Uncleared transactions, but are no guarantee against fraud. If you are in any doubt about a transaction, we recommend declining it and notifying the customer.

{{< details title="Billing Suite payment methods" >}}

**Uncleared** status applies to a number of post-payment methods in our [Billing Suite ](/payment-methods/billing-suite/). <br>

For [Klarna](/payment-methods/billing-suite/klarna/), [Afterpay](/payment-methods/billing-suite/afterpay/), [Betaal per Maand](/payment-methods/billing-suite/betaalpermaand/) and [Pay After Delivery](/payment-methods/billing-suite/pay-after-delivery/) after you ship the order, the order status is **Shipped** and the transaction status is **Uncleared**. At this point, the transaction is confirmed and settlement is guaranteed. The transaction status then changes to **Completed** when MultiSafepay receives settlement and adds the funds to your MultiSafepay balance.

For [Request to Pay](/payment-methods/banks/request-to-pay/), [SOFORT Banking](/payment-methods/banks/sofort-banking/) and [SEPA Direct Debit](/payment-methods/banks/sepa-direct-debit/), **Uncleared** status means MultiSafepay has not yet received settlement (partially or in full, e.g. the remaining instalments of an in3 payment). We recommend **not** shipping orders during this status.

{{< /details >}}

{{< details title="Transaction amount" >}}

Check if the transaction amount is noticeably higher or lower than average. Are you willing to risk this payment being revoked after delivering your product or service?

{{< /details >}}

{{< details title="Specific product or service" >}}
The risk of fraud strongly correlates with the type of products or services you offer. Popular products among fraudsters include consumer electronics, jewelry, and clothes by well-known fashion and designer brands. These products are easily re-sold for a worthwhile value, especially when ordered in bulk. 

Consider:

- Is the product easy to re-sell?
- Does the order make sense? 
- Is the product selection or order size unusual?

{{< /details >}}

{{< details title="Customer" >}}
You can view customer information in your MultiSafepay account and in your backend, which may contain useful information we do not have. 

Consider:

- Are they a known customer? Are they a good customer or have you had problems with them before?

- Do they fit the profile of your average customer, e.g. location, average order value?

- Check the customer's email address. Fraudsters generally use auto-generated email addresses and free email services.

- In case of doubt, contact the customer. Have you ever had contact with them before? What is your impression of them?

- Ask if the customer is willing to complete the order using a different payment method – one with a
payment guarantee, such as a bank transfer. 

- You can also ask the customer for a copy of their ID card and/or a credit card statement to verify that they are the credit card holder.

In many cases, the card holder did initiate the transaction, but that is no guarantee it is not fraudulent.

{{< /details >}}

{{< details title="3D Secure" >}}

3D Secure is a security measure intended to reduce fraud that verifies the cardholder's identity. The customer completes the 3D Secure check during the payment process, e.g. by filling in an additional password or code, or by using a credit card reader. 

If a 3D Secure verification is successfully completed, you are protected against chargebacks requested due to suspected fraud. If a cardholder discovers a fraudulent payment, they can demand a refund for the payment, even if the order has already been delivered. This is called a chargeback. 

For more information about chargebacks, the risks of credit card payments, and accepting and refusing uncleared payments, see [Chargebacks](https://docs.multisafepay.com/faq/chargebacks).

Many card schemes don't yet offer 3D Secure.

If the customer is enrolled for 3D Secure, in the **Transaction details** page > **Risk summary**, their status displays as **Enrolled**.  
 
### 3D Secure statuses

| 3D Secure result            | Description      |
|---------------------|-----------|
| Enrolled Liability  | 3D Secure available and successfully verified. Liability for fraud is shifted to the cardholder. Fraud chargebacks are not possible. |
| Not Enrolled, Liability  | 3D Secure available, but not used or successfully verified. Liability for fraud is shifted to the cardholder. Fraud chargebacks are not possible |
|  No Liability  | No 3D Secure verification available. Liability not shifted. Fraud chargeback is possible.|

{{< /details >}}

{{< details title="Payment location" >}}

Does the country address match the location of the IP address and country where the credit card was issued? Discrepancies are often easily explained, e.g. vacations or business trips. 

We recommend comparing where payments were made to where the card was initially issued. Pay particular attention to locations that are far apart, particularly if one is in a high-risk area.

{{< /details >}}

{{< details title="Risk report" >}}

For more information about the card used for the transaction, in the **Transaction details** page, click **View Risk report**. 

You can view:
- Information about the number of credit cards used via a specific IP address
- The number of credit cards used in combination with a specific email address

{{< /details >}}

{{< details title="Other indicators" >}}

Under **Fraud info** (next to the fraud score), there are several other fraud risk indicators based on the email address and shipping details.

Under **History Data**, there is information about the number of credit cards used from the same IP address or with the same email address. If this number is high, it may indicate a fraudster, but may also indicate a big order from a large business.
{{< /details >}}

## See also 

[Viewing your Uncleared balance](/faq/finance/viewing-your-uncleared-balance/)