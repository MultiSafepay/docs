---
title : 'Uncaptured card payments'
category: 6298bd782d1cf4006032e765
order: 208
hidden: false
parentDoc: 62a727569e389a012f577acd
excerpt: Capture or decline potentially fraudulent card payments.
slug: uncaptured
---

To help reduce the risks associated with accepting credit cards, MultiSafepay's automated fraud filter reviews all card payments.

# How it works 

All card transactions are assigned a fraud score from 1-10: 10 being the most at risk of fraud. 

For higher-risk transactions, the payment is placed on hold and the [transaction status](/payment-statuses/) changes to **Uncleared**. 

| Fraud score | On hold | Action required |
|---|---|---|
| 1–5 Low risk | No | None. |
| 6–8 Medium risk | Yes | Review in your dashboard and capture or decline. |
| 8–10 High risk | Yes | MultiSafepay reviews and captures or declines. |

**Note:** High-scoring transactions aren't always fraudulent, and low-scoring ones may still carry risk.

# Reviewing uncaptured payments

When uncaptured payments are awaiting your review in your dashboard, you receive a notification in your dashboard and an email to the address provided under **Contact details** for your account.

The final decision to capture or decline lies with you, as you are solely liable for any financial damage.
For professional advice on reviewing and evaluating potential risks or fraud indicators, email <risk@multisafepay.com> 

If you take no action, uncaptured transactions automatically expire after 5 days.

<details id="how-to-review-uncaptured-payments">
<summary>How to review uncaptured payments</summary>
<br>

To review uncaptured payments, click the dashboard notification, or:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
2. Go to **Transactions** > **Uncleared transactions**.
3. Click each transaction in the list to view the **Transaction details** page, including: 
    - Basic information about the transaction, history data, and any notes
    - The fraud score
    - A risk summary – For a detailed risk report, click **More information**.
    - If the customer is enrolled for 3D Secure 
4. Evaluate the transaction (see guidance below) and:
    - To capture, click **Accept**.
    - To decline, click **Decline**.

</details>

# Evaluating uncaptured transactions
The following indicators paint a cumulative picture of uncaptured payments, but are no guarantee against fraud. If you are in any doubt about a payment, we recommend declining it and notifying the customer.

<details id="transaction-amount">
<summary>Transaction amount</summary>
<br>

Check if the transaction amount is noticeably higher or lower than average. Are you willing to risk this payment being revoked after delivering your product or service?

</details>

<details id="specific-product-or-service">
<summary>Specific product or service</summary>
<br>

The risk of fraud strongly correlates with the type of products or services you offer. Popular products among fraudsters include consumer electronics, jewelry, and clothes by well-known fashion and designer brands. These products are easily re-sold for a worthwhile value, especially when ordered in bulk. 

Consider:

- Is the product easy to re-sell?
- Does the order make sense? 
- Is the product selection or order size unusual?

</details>

<details id="customer">
<summary>Customer</summary>
<br>

You can view customer information in your dashboard and in your backend, which may contain information we do not have access to. 

Consider:

- Are they a known customer? Are they a good customer or have you had problems with them before?
- Do they fit the profile of your average customer, e.g. location, average order value?
- Check the customer's email address. Fraudsters generally use auto-generated email addresses and free email services.
- In case of doubt, contact the customer. Have you ever had contact with them before? What is your impression of them?
- Ask if the customer is willing to complete the order using a different payment method with a
payment guarantee, such as a bank transfer. 
- You can also ask the customer for a copy of their ID card and/or a credit card statement to verify that they are the cardholder.

In many cases, the cardholder did initiate the transaction, but that is no guarantee it is not fraudulent.

</details>

<details id="3d-secure">
<summary>3D Secure</summary>
<br>

[3D Secure](/cards/3ds2/) is an authentication protocol for verifying the cardholder's identity, e.g. with an additional password or code, or a credit card reader. If the customer passes authentication, you are protected against fraud-related [chargebacks](/chargebacks/).

Check if the customer is enrolled for 3D Secure. On the **Transaction details** page > **Risk summary**, their status displays as **Enrolled**.  
 
**3D Secure statuses**

| 3D Secure result | Description |
|---|---|
| Enrolled, Liability  | 3D Secure available and successfully authenticated. Liability for fraud is shifted to the cardholder and chargebacks are **not** possible. |
| Not Enrolled, Liability  | 3D Secure available, but not used or successfully authenticated. Liability for fraud is shifted to the cardholder and chargebacks are **not** possible. |
|  No Liability  | 3D Secure **not** available. You retain liability for fraud chargebacks.|

</details>

<details id="location">
<summary>Location</summary>
<br>

Does the country address match the location of the IP address and country where the credit card was issued? Discrepancies are often easily explained, e.g. vacations or business trips. 

We recommend comparing where payments were made to where the card was initially issued. Pay attention to locations that are far apart, particularly if one is in a high-risk area.

</details>

<details id="risk-report">
<summary>Risk report</summary>
<br>

For more information about the card used, in the **Transaction details** page, click **View risk report**. 

You can view the number of cards used:

- Via a specific IP address
- With a specific email address

</details>

<details id="settlement-status">
<summary>Settlement status</summary>
<br>

After you ship a [Klarna](/payment-methods/klarna/), [Afterpay](/payment-methods/afterpay/), [Betaal per Maand](/payment-methods/betaal-per-maand/), and [Pay After Delivery](/payment-methods/pay-after-delivery/) order, the order status is **Shipped** and the transaction status is **Uncleared**. At this point, the transaction is confirmed and settlement is guaranteed. The transaction status changes to **Completed** when MultiSafepay adds the funds to your MultiSafepay balance.

For [Request to Pay](/payment-methods/request-to-pay/), [Sofort](/payment-methods/sofort-banking/), and [SEPA Direct Debit](/payment-methods/sepa-direct-debit/), **Uncleared** status means MultiSafepay has not yet received settlement partially or in full. We recommend **not** shipping orders during this status.

</details>

<details id="other-indicators">
<summary>Other indicators</summary>
<br>

Under **Fraud info** (next to the fraud score), there are several other fraud risk indicators based on the email address and shipping details.

Under **History data**, there is information about the number of credit cards used from the same IP address or with the same email address. If this number is high, it may indicate a fraudster, but may also indicate a big order from a large business.

</details>

## See also 

[Viewing your uncleared balance](/account/balance/#viewing-your-uncleared-balance)
<br>

> 📘 **More info**
> For more information or support, email <support@multisafepay.com>