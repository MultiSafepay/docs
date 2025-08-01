---
title: Payment methods
category:
  uri: Getting started
slug: payment-methods
position: 10
privacy:
  view: public
parent:
  uri: manage-account
content:
  excerpt: Activate payment methods for your account.
---

MultiSafepay offers a wide range of payment methods.

<Cards columns={5}>
  <Card title="Banking methods" href="/docs/banking-methods" icon="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Banks.png" />

  <Card title="Buy Now Pay Later" href="/docs/bnpl" icon="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/BNPL.png" />

  <Card title="Credit and debit cards" href="/docs/cards" icon="https://raw.githubusercontent.com/MultiSafepay/MultiSafepay-icons/master/methods/creditcard2.png" />

  <Card title="Prepaid cards" href="/docs/prepaid-cards" icon="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/PrepaidCards.png" />
</Cards>

<Card title="Wallets" href="/docs/wallets" icon="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/img/Digital.png" />

<HTMLBlock>{`
<style>

b {
  color: #384248 !important;
}

.auto-grid {
  --auto-grid-min-size: 175px;

  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(var(--auto-grid-min-size), 1fr));
}

.card-container {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2); /* this adds the "card" effect */
  padding: 16px;
  text-align: center;
  border-radius: 5px;
  margin: 8px
}

.card-container:hover {
  box-shadow: 0 8px 16px 0 rgb(0 0 0 / 20%);
  transform: translateY(-0.2rem);
  transition: all 0.2s;
  cursor: pointer;
}

</style>
`}</HTMLBlock>

### Activation

Some payment methods, especially Banking methods, can be activated directly via your dashboard.

#### How to activate standard payment methods

1. Sign in to your <a href="https://merchant.multisafepay.com" target="_blank">MultiSafepay dashboard</a> <i class="fa fa-external-link" style={{ fontSize: "12px", color: "#8b929e" }} />.
2. To activate the payment method for:

* All websites, go to **Settings** > **Payment methods**.
* A specific website, go to **Websites**, and then click the relevant website.\
  This overwrites your global selection. Only the payment methods selected for the website will then be available.

3. Select the checkbox for the payment method, and then click **Save changes**.

**💡 Tip**: if you do not set website-specific methods, the global configuration will be applied.

💬  **Support:** If the payment method isn't visible in your dashboard, email [support@multisafepay.com](mailto:support@multisafepay.com)

For instructions to activate additional payment methods, see the respective pages and follow individual activation steps.

If you use a [ready-made integration](/docs/our-integrations/), first check that the payment method is supported.

### Testing

Before you start processing real transactions, test each payment method.  For more information - see [Testing payment methods](/docs/testing)

<br />

***

<HTMLBlock>{`
<blockquote class="callout callout_info">
    <h3 class="callout-heading false">
        <span class="callout-icon">💬</span>
        <p>Support</p>
    </h3>
    <p>Email <a href="mailto:support@multisafepay.com">support@multisafepay.com</a></p>
</blockquote>
`}</HTMLBlock>

[Top of page](#)
