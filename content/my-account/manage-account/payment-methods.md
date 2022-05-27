---
title: "Payment methods"
weight: 3
meta_title: "Payment methods - MultiSafepay Docs"
read_more: "."
layout: 'single'
url: '/account/payment-methods/'
aliases:
    - /payments/activating-payment-methods/
---

MultiSafepay offers a wide range of [payment methods](/payment-methods/).

You can enable payment methods for your account yourself in your dashboard, but for some you need to apply to MultiSafepay first. Other methods with specific requirements follow their own activation flow. 

| Activation flow | Payment methods |
|---|---|
| [Apply to MultiSafepay](/payments/activating-payment-methods/#apply-to-multisafepay) | [Cards](/payment-methods/credit-debit-cards/) and [wallets](/payment-methods/wallets/) (**except** PayPal), {{< br >}} Dotpay, in3, Pay After Delivery, {{< br >}} SEPA Direct Debit |
| [Enable in dashboard](/payments/activating-payment-methods/#enable-in-dashboard) | [Banking methods](/payment-methods/banks), E-Invoicing   |
| [Own flow](/payments/activating-payment-methods/#own-flow) | AfterPay, Betaal per Maand, Klarna, {{< br >}} Edenred, gift cards, Paysafecard, {{< br >}} PayPal |

{{< blue-notice >}} If you use a [ready-made integration](/integrations/ready-made/), first check that the payment method is supported. Once the method is activated, also enable it in your backend.{{< /blue-notice >}}

## Apply to MultiSafepay 

1. Email a request to <risk@multisafepay.com> 
{{< details title="Cards, Apple Pay, and Google Pay" >}} 
 
Include in the request your: 
  
- Average, minimum, and maximum transaction amount 
- Annual turnover 
{{< /details>}}
{{< details title="SEPA Direct Debit" >}} 
- Include in the request the following information:
    - Monthly and annual SEPA Direct Debit transaction volume
    - Minimum and maximum transaction amount
    - Type of products sold using this payment method
    - Whether you want to accept [recurring payments](/features/recurring-payments/)
    - Whether any subscriptions are monthly, quarterly, or annual
- Depending on the details provided, we may ask for additional information.
- We send you an agreement to sign and email back to us.
{{< /details >}}
2. We check your eligibilty and if approved, activate the payment method for your account. 
3. Once approved, enable the method in your dashboard as below.

## Enable in dashboard

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Settings**. 
3. To enable the payment method for:
    - All sites, go to **Payment methods**.
    - A specific site, go to **Website settings**, and click the relevant site.
4. Select the checkbox for the relevant payment method, and then click **Save changes**.

**Note:** If the payment method isn't visible in your dashboard, email <integration@multisafepay.com> 

## Own flow

### AfterPay
{{< details title="AfterPay activation" >}} 
1. To check you are eligible for AfterPay, email <sales@multisafepay.com>

2. For new AfterPay clients, apply directly to AfterPay:

- The Netherlands: [Offerte](https://www.afterpay.nl/nl/zakelijk/offerte)
- Belgium: [Offerte aanvragen](https://www.afterpay.be/be/footer/zakelijke-partners/offerte-aanvragen)

3. For existing AfterPay clients, to activate AfterPay for your MultiSafepay account, email AfterPay Sales at <sales@afterpay.nl>  
{{< /details >}}
### Betaal per Maand
{{< details title="Betaal per Maand activation" >}}
You must:

- Have a [MultiSafepay account](/getting-started/)
- Be registered with a Dutch Chamber of Commerce (no exceptions)
- Have an annual turnover of more than 500,000 EUR (unless agreed otherwise with Betaal per Maand)
- Sell products or services to European citizens with a residential or delivery address in the Netherlands (no exceptions)
- Connect to MultiSafepay via our API or [ready-made integrations](/integrations/ready-made/)

1. Email a request to <sales@multisafepay.com>
2. In the request, let us know if you already have a Santander account. If you don't, we'll submit an application for you. 
3. We check your eligibility and type of connection. 
4. Once approved, we activate the payment method for your account.
{{< /details >}}
### Edenred
{{< details title="Edenred activation" >}}
1. Fill out the Edenred – [Registreer mijn website](https://registreermijnwebsite.edenred.be/) form, selecting the relevant checkbox for each voucher you want to offer.
2. Sign a contract with Edenred. They'll give you an Edenred Merchant ID.
3. Email your Edenred Merchant ID to <sales@multisafepay.com>
4. We activate the payment method for your account.
{{< /details >}}
### Gift cards
{{< details title="Gift cards activation" >}}
1. To check your eligibility, email <sales@multisafepay.com> 
2. Send a request to the **card issuer**, providing your company details and MultiSafepay account ID.
3. The issuer connects you to the card via either:
- [Intersolve](https://intersolve.nl/contact) (majority of gift cards)
- [Fashioncheque](https://www.fashioncheque.com/nl/customerservice)
- [123TCS](https://www.123tcs.com/#Contact)
4.  The issuer sends us the connection details and we activate the card for your account.
{{< /details >}}
### Klarna
{{< details title="Klarna activation" >}} 
**Test account**

1. At [Klarna.com](https://www.klarna.com/nl/), sign up for a test account, selecting the **Playground** environment. 
2. Under **Settings**, click **Generate new Klarna API credentials** to generate a user name and password.
3. Email these credentials to <sales@multisafepay.com> 
4. MultiSafepay connects to Klarna. 

We recommend testing Klarna payments via the Klarna Portal to experience the full functionality. You can also test from your **test** MultiSafepay dashboard with more limited functionality.

**Live account**

1. Sign up for a live Klarna account:

- Via the Klarna website, selecting the **Production** environment, **or**  
- Email your Klarna account manager or <verkoop@klarna.com>
2. Specify MultiSafepay as your payment service provider and the countries you want to activate Klarna for.
3. Sign an agreement with Klarna, including pricing.
4. We activate Klarna for your MultiSafepay account. 
5. If using a ready-made integration, activate Klarna in your [backend](/glossaries/multisafepay-glossary/#backend).

For questions, see Klarna – [Klantenservice](https://www.klarna.com/nl/klantenservice).

For support, email <integration@multisafepay.com>
{{< /details >}}
### PayPal
{{< details title="PayPal activation" >}}

**Configuring your PayPal account**

To configure your PayPal account, follow these steps:

1. Sign in to your business account at [Paypal.com](https://www.paypal.com).
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Account access** tab, under **API access**, click **Update**.
4. Under **Pre-built payment solution**, click **Grant API permission**.
5. In the **Third-party permission username** field, enter `paypal_api1.multisafepay.com`. 
7. Click **Lookup**.  
8. Select the checkboxes of the relevant permissions:  
    - Use Express Checkout to process payments.
    - Issue a refund for a specific transaction.
    - Process your customers' credit or debit card payments.
    - Obtain information about a single transaction.

To complete the configuration, change the language encoding setting of your PayPal account to **UTF-8**:

1. Click PayPal – [Profile language encoding](https://www.paypal.com/cgi-bin/customerprofileweb?cmd=_profile-language-encoding).
2. Next to **Language coding for PayPal buttons**, click **Edit**.
3. From the list, select **Western European languages (including English)**.
4. Click **More options**.
5. From the **Encoding** list, select **UTF-8**.
6. Select the **Yes** checkbox, and then click **Save**.

**Support**  

- Email <integration@multisafepay.com>
- PayPal – [Contact us](https://www.paypal.com/us/smarthelp/contact-us)

{{< alert-notice >}} **Known issue:** If your PayPal business account isn't yet fully verified or approved, you might get a PayPal error 10002: Restricted account. {{< /alert-notice >}}

**Configuring your MultiSafepay account**

To configure your MultiSafepay account for PayPal, follow these steps:

1. Sign in to your business account at [Paypal.com](https://www.paypal.com).
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Business information** tab, copy your PayPal Merchant ID.
4. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com), and then go to **Settings**. 
5. To activate PayPal for:

- All your sites:
    - Go to **Payment methods**, and then select **PayPal**.
    - In the **PayPal Merchant ID** field, paste your ID, and click **Save changes**.

- A specific site:
    - Go to **Website settings**, and click the relevant site.
    - Under **Payment methods**, select the **PayPal** checkbox, and click **Save changes**.

**Notes:** 

- You can link each site to a separate PayPal business account, or all sites can use your main PayPal business account.
- If PayPal isn't visible as a payment method in your dashboard, email <integration@multisafepay.com> 

Your account is now configured!  
We strongly recommend [testing transactions](/payment-methods/paypal/integration-testing/) before processing live payments. 
{{< /details >}}
### Paysafecard
{{< details title="Paysafecard activation" >}}
Paysafecard doesn't require activation.

Search for outlets that sell Paysafecard:

- English-language site: [Find sales outlets](https://www.paysafecard.com/en/find-sales-outlet-1/)
- Dutch-language site: [Verkooppunten zoeken](https://www.paysafecard.com/nl/verkooppunt-vinden-1/)

For any questions, email <sales@multisafepay.com>
{{< /details >}}



