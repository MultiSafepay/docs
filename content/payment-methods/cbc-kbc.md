---
title: 'CBC/KBC'
category: 6298bd782d1cf4006032e765
order: 6
hidden: false
parentDoc: 62a728d48b97080046c1d220
slug: 'cbc-kbc'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/cbc.svg" width="60" alt="CBC/KBC logo" style={{ margin: "30px", maxHeight: "75px", float: "right" }} />

<span>
  An online banking payment method of two of Belgium's largest banks: <a href="https://www.cbc.be/particuliers/fr.html" target="_blank" rel="noopener noreferrer">CBC</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} /> which serves the French speaking population, and <a href="https://www.kbc.be/particulieren/nl.html" target="_blank" rel="noopener noreferrer">KBC</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} /> which serves the Dutch-speaking population.
</span>

<p>
  The payment method functions the same for both the CBC branch and the KBC branch. However, MultiSafepay's payment<Glossary>gateway</Glossary> includes the branches as separate options because customers of one branch can't pay through the other.
</p>

<p>
  Read how CBC/KBC can benefit your business on <a href="https://www.multisafepay.com/solutions/payment-methods/kbccbc" target="_blank" rel="noopener noreferrer">multisafepay.com</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} />
</p>

| Supports                                                      | Details                                                           |
| ------------------------------------------------------------- | ----------------------------------------------------------------- |
| [Countries](/docs/payment-methods#payment-methods-by-country) | Belgium                                                           |
| [Currencies](/docs/currencies/)                               | EUR                                                               |
| [Chargebacks](/docs/chargebacks/)                             | No                                                                |
| [Payment pages](/docs/payment-pages/)                         | Yes (current version only)                                        |
| [Refunds](/docs/refund-payments/)                             | Yes: Full and partial (1 business day after payment is completed) |
| [Second Chance](/docs/second-chance/)                         | Yes                                                               |

# Payment flow

This diagram shows the flow for a successful transaction. Click to magnify.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/diagrams/svg/cbc-kbc-payment-flow.svg" alt="CBC/KBC payment flow" style={{ display: "block", marginLeft: "auto", marginRight: "auto", maxWidth: "750px", width: "100%" }} />

**⚠️ Note:** MultiSafepay doesn’t automatically receive the customer's IBAN when a transaction is completed, but we import our bank statements daily. All incoming payments are then completed.

# Payment statuses

The table below sets out the <Glossary>order status</Glossary> and <Glossary>transaction status</Glossary> for payments and refunds.

| Description                                           | Order status | Transaction status |
| ----------------------------------------------------- | ------------ | ------------------ |
| The customer has been redirected to their bank.       | Initialized  | Initialized        |
| MultiSafepay has collected payment.                   | Completed    | Completed          |
| The transaction was cancelled by you or the customer. | Void         | Void               |
| The customer didn't complete payment within 5 days.   | Expired      | Expired            |
| **Refunds:** Refund initiated.                        | Initialized  | Initialized        |
| **Refunds:** Refund complete.                         | Completed    | Completed          |

<br />

**⚠️ Note:** If the customer doesn’t click the **Return to website** button, MultiSafepay doesn’t receive an update and the transaction status remains **Initialized**. We import our bank statements daily and match all incoming payments.

# Activation

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank" rel="noopener noreferrer">MultiSafepay dashboard</a> <i className="fa fa-external-link" style={{ fontSize: 12, color: "#8b929e" }} />.
2. To activate the payment method for:
   * All websites, go to **Settings** > **Payment methods**.
   * A specific website, go to **Websites**, and then click the relevant website.
3. Select the checkbox for the payment method, and then click **Save changes**.

💬  **Support:** If the payment method isn't visible in your dashboard, email <a href="mailto:support@multisafepay.com">[support@multisafepay.com](mailto:support@multisafepay.com)</a>

# Integration

### API

* See API reference – [Create order](/reference/createorder/) > Banking order.

<details id="example-requests">
  <summary>Example requests</summary>

  <br />

  For example requests, on the <a href="/reference/createorder/">Create order</a> page, in the black sandbox, see **Examples** > **CBC/KBC direct/redirect**.

  <div style={{ textAlign: "center" }}>
    <img src="https://raw.githubusercontent.com/MultiSafepay/docs/refs/heads/master/static/gifs/sandbox-test.gif" alt="MultiSafepay Sandbox Test Process GIF" style={{ width: "40%", height: "auto" }} />
  </div>
</details>

* Transactions expire after 5 days.

### Ready-made integrations

* [Craft Commerce](/docs/craft-commerce/)
* [OpenCart](/docs/opencart/)
* [Magento 1](/docs/magento-1/) & [Magento 2](/docs/magento-2/)
* [PrestaShop](/docs/prestashop/)
* [Shopware 5](/docs/shopware-5/)
* [Shopware 6](/docs/shopware-6/)
* [WooCommerce](/docs/woocommerce/)

### Testing

To test CBC/KBC payments, see Testing payment methods - [Banking methods](/docs/testing#banking-methods).<br />

***

<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>

[Top of page](#)