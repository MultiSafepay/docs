---
title: 'Request to Pay'
category: 6298bd782d1cf4006032e765
order: 112
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'request-to-pay'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Payment_methods/RTP.svg" width="60" align="right" style="margin: 20px; max-height: 75px"/>

Request to Pay is a Deutsche Bank payment method based on the PSD2 Open Banking API. Customers are redirected to Deutsche Bank online banking to authenticate themselves, and authorize a secure SEPA transfer. Settlement is instant (if supported) or within 24 hours. 

The funds are transferred directly to your business bank account, instead of your account balance, which simplifies reconciliation.

Read how Request to Pay can benefit your business on [multisafepay.com](https://www.multisafepay.com/solutions/payment-methods/request-to-pay)

> ⚠️ Availability
> Request to Pay is currently not available to new merchants. It is still supported for existing merchants. 

| Overview | Details |
|---|---|
| **Amount limits** | Minimum amount: 1 EUR, maximum amount: 15,000 EUR |
| **Chargebacks**  | No  | 
| **Countries**  | Germany – More countries will follow as more banks migrate to PSD2 APIs.  | 
| **Currencies**  | EUR | 
| **Expiration** | Transactions expire after 1 hour. |
| **Payment pages** | [Yes](/payment-pages/) (current version only) |
| **Refunds** | [Yes](/refunds/): Full and partial <br> All refunds are processed by Deutsche Bank. |
| **Second Chance** | [Yes](/second-chance/) |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

{{< mermaid class="text-center" >}}

sequenceDiagram
    autonumber
    participant C as Customer
    participant Mu as MultiSafepay
    participant D as Deutsche Bank
    participant Me as Merchant

    C->>Mu: Selects Request to Pay at checkout
    alt Redirect flow
    Mu->>C: Redirects to payment page to select their bank, <br> then to online banking
    else Direct flow
    Mu->>C: Redirects customer to online banking
    end
    C->>D: Authenticates account and authorizes SEPA bank transfer
    D->>Mu: Transfers funds (within 24 hours, <br> if Instant SEPA not supported)
    Mu->>Me: Settles funds
    
{{< /mermaid >}}

# Payment statuses  

- **Order status:** Changes as the customer's order with you progresses towards shipment 
- **Transaction status:** Changes as the funds progress towards settlement in your account balance

<details id="payment-statuses">
<summary>Payment statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| The customer has been redirected to Deutsche Bank. | Initialized | Initialized |
| Deutsche Bank has authorized the transaction and is transfering the funds. | Completed  | Uncleared |
| MultiSafepay has collected payment. | Completed | Completed |
| Deutsche Bank declined the transaction. | Declined | Declined   |
| The customer cancelled the transaction at Deutsche Bank. | Void | Void |
| The customer didn't complete payment within 1 hour. | Expired | Expired |

</details>

<details id="refund-statuses">
<summary>Refund statuses</summary>
<br>

| Description | Order | Transaction |
|---|---|---|
| Refund initiated. | Reserved | Reserved |
| Refund complete. | Completed | Completed |
| Refund declined. | Declined | Declined |

</details>

# Activation

You can activate Request to Pay yourself in your dashboard. 

<details id="how-to-activate-request-to-pay"> 
<summary>How to activate Request to Pay</summary>
<br>

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

> 💬  Support
> If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

</details>

# Integration

| Integration | Details |
|---|---|
| **API** | [Create order](https://docs-api.multisafepay.com/reference/createorder) > Banking order <br> Examples > Request to Pay direct/redirect |
| **Ready-made integrations** | **Not** supported in our [ready-made integrations](/integrations/ready-made/). |
<br>

> ℹ️ Testing
> You can't test Request to Pay in your MultiSafepay test account. You can only make test payments in your MultiSafepay live account.
<br>

---

> 💬  Support
> Email <support@multisafepay.com>
[Top of page](#)
