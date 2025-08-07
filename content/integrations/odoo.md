---
title: Odoo
category:
  uri: Integrations
slug: odoo
position: 1
privacy:
  view: public
parent:
  uri: archived-integrations
content:
  excerpt: Technical manual for MultiSafepay's free plugin.
---
> ❗️ Important:
>
> This plugin is at end-of-life. It may contain security vulnerabilities, compatibility issues, and lack the latest features. MultiSafepay provides no support for these plugins.

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/logo/Plugins/Odoo.svg" width="100" align="right" style={{margin: '20px', maxHeight: '75px'}} />

<div style={{display: 'flex', flexWrap: 'wrap'}}>
  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#006ba1', color: '#ffffff', textDecoration: 'none'}} href="https://github.com/MultiSafepay/official-odoo-integration/archive/13.0-develop.zip" target="_self"><span>Download</span><i className="icon icon-download" style={{marginLeft: '0.6em'}}> </i></a>

  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/official-odoo-integration" target="_blank"><i className="icon-external-link" /> <span>Source code</span></a>

  <a className="suggestEdits" style={{display: 'inline-flex', borderRadius: '5px', padding: '10px 20px', margin: '10px', fontSize: '1rem', backgroundColor: '#DFEBF6', color: '#0a59a1', textDecoration: 'none'}} href="https://github.com/MultiSafepay/official-odoo-integration/blob/13.0-develop/CHANGELOG.md" target="_blank"><span>Changelog</span></a>
</div>

# Prerequisites

* [MultiSafepay account](/docs/getting-started-guide/)
* Odoo 13.0
* Tested on Python 3.6

# Installation

  **💡 Tip!** We recommend first installing the plugin in a test environment, following the Odoo installation procedure. Always make a backup.

1. Download the ZIP archive with module.
2. Unpack the content of the .ZIP file.
3. In your Odoo server (`/mnt/extra-addons/`), under **Custom apps**, add the **payment\_multisafepay\_official** folder.
4. Install the required Python dependencies:
   ```
   pip3 install -r requirements.txt
   ```
   Alternatively, you can install them manually:
   ```
   pip3 install multisafepay==0.2.0
   ```
   For more information about dependencies, see Python - <a href="https://pypi.org/project/multisafepay" target="_blank">MultiSafepay</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
5. Restart your Odoo server.
6. In your Odoo <Glossary>backend</Glossary>, activate developer mode.
7. Go to the **Apps menu** > **Update apps list**.
8. Search for and open the MultiSafepay payments module `payment_multisafepay_official`.
9. Click **Install**.

# Configuration

1. Sign in to your Odoo backend.
2. Go to the **Invoicing** or **Website** menu > **Configuration** > **Payment acquirers**.
3. Select **MultiSafepay** payment acquirer.
4. Go to **Edit** mode.
5. To change the <Glossary>acquirer</Glossary> state, click **Enabled** or **Test**. (Default: Disabled)
6. Enter **Live** and/or **Test** **API key**.
7. On the **Configuration tab**, set **Journal**, and then click **Save**.
8. To get payment methods from your MultiSafepay account, go the **Configuration** tab, click **Pull payment methods**.\
   Make sure the relevant payment methods are activated for your account.
9. Configure each payment method separately:

   <details id="payment-method-settings">
     <summary>Payment method settings</summary>

     <br />

     * Name
     * State
     * Country: Disabled for some payment methods
     * Customer group
     * Order amount: Disabled for some payment methods
     * Supported currency: Some payment methods process transactions only in EUR. Orders not created in EUR are converted to the required currency, using **Odoo platform currency rate**. This can only be configured by a system administrator.
   </details>

   <br />

***

# User guide

## Generic gateways

The plugin supports generic gateways, which allows you to add a payment method manually. This is particularly useful for integrating gift cards specific to your business.

Supported since release: 1.1.0, July 2nd 2021.

<details id="how-to-configure-generic-gateways">
  <summary>How to configure generic gateways</summary>

  <br />

  1. Sign in to your Odoo backend.
  2. Go to **Invoicing** > **Payment method** > **Other payment acquirer** > **MultiSafepay**.
  3. In the **Title** field, set the relevant [payment method gateway IDs](/reference/gateway-ids/).
  4. Set the gateway logo and name.
</details>

## Orders

<details id="how-to-create-orders">
  <summary>How to create orders</summary>

  <br />

  1. Select the payment method on the checkout page, and then click **Pay now**.
  2. Provide any required information (e.g. bank account number), and confirm payment.
  3. When the transaction is completed, you receive a *Order \{ order ID } Confirmed* <a href="https://docs.multisafepay.com/docs/webhook" target="_blank">webhook notification</a> <i className="fa fa-external-link" style={{fontSize:'12px',color:'#8b929e'}} />.
</details>

<details id="how-to-ship-orders">
  <summary>How to ship orders</summary>

  <br />

  1. Go to the **Website** menu> **Orders**, and then select the relevant order.
  2. To mark the order as **Shipped**, go to **Delivery** and **Validate transfer**.\
     The transaction status changes to **Shipped**.
  3. Under **Order details**, you can create an invoice. Its status is **Paid** right away because the order was prepaid.
  4. If you want to update the invoice ID of the transaction with MultiSafepay, go to **Configuration** > **Payment transactions**, select the relevant transaction, and then click **Update invoice ID**.
</details>

## Payment methods

<details id="supported-payment-methods">
  <summary>Supported payment methods</summary>

  <br />

  * Cards: [All](/docs/card-payments/)
  * <Glossary>BNPL</Glossary>: All, except Billink.
  * Wallets: [Alipay](/docs/alipay/), [Apple Pay](/docs/apple-pay/), [PayPal](/docs/paypal/)
  * Banking methods:
    * [Bancontact](/docs/bancontact/)
    * [Bank transfer](/docs/bank-transfer/)
    * [Belfius](/docs/belfius/)
    * [CBC/KBC](/docs/cbc-kbc/)
    * [Dotpay](/docs/dotpay/)
    * [EPS](/docs/eps/)
    * [Giropay](/docs/giropay/)
    * [iDEAL](/docs/ideal/)
    * [Direct debit](/docs/direct-debit/)
    * [Sofort](/docs/sofort/)
    * [Trustly](/docs/trustly/)
</details>

## Refunds

<details id="how-to-refund-orders">
  <summary>How to refund orders</summary>

  <br />

  In your Odoo backend, you can only refund **Completed** orders.

  1. To create a refund invoice, go to **Order invoices**, and then click **Add credit note**.
  2. Enter a **Refund reason** and check the invoice lines you want to return, and then click **Post**.
  3. To create a refund request, click **Refund with MultiSafepay**.
  4. If the request is created successfully, the invoice status changes.
  5. When the status of the MultiSafepay refund transaction changes to **Completed**, the status of the refund invoice changes to **Paid**.
</details>

<details id="how-to-refund-bnpl">
  <summary>How to refund BNPL orders</summary>

  <br />

  For <Glossary>BNPL</Glossary> orders, the refund request must include a `shopping_cart` object where:

  * The `item_quantity` must not be more than `quantity` in the original order.
  * The `item_price` must be equal to the `unit_price` in the original order.

  **⚠️ Note:** You cannot refund BNPL orders if a gift card or promo code was used for the original order.
</details>

## Updates

You can update in your <Glossary>backend</Glossary>.

<details id="how-to-update-the-plugin">
  <summary>How to update the plugin</summary>

  <br />

  1. Sign in to your Odoo backend.
  2. Go to the **Apps** menu.
  3. Search for and open the **MultiSafepay payments** module.
  4. Click **Upgrade**.
</details>

<br />

***

<blockquote className="callout callout_info">
  <h3 className="callout-heading false">
    <span className="callout-icon">💬</span>
    <p>Support</p>
  </h3>

  <p>Contact MultiSafepay:</p>

  <ul>
    <li>Telephone: <a href="tel:+310208500500">+31 (0)20 8500 500</a></li>
    <li>Email: <a href="mailto:integration@multisafepay.com">[integration@multisafepay.com](mailto:integration@multisafepay.com)</a></li>
    <li>GitHub: <a href="https://github.com/MultiSafepay/official-odoo-integration/issues" target="_blank"> create a technical issue</a></li>
  </ul>
</blockquote>

[Top of page](#)
