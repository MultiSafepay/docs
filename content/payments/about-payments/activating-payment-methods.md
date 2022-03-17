---
title: "Activating payment methods"
weight: 10
meta_title: "Activating payment methods - MultiSafepay Docs"
read_more: "."
layout: 'single'
hide_menu: 'true'
url: '/payments/activating-payment-methods/'
---
This page sets out how to activate payment methods. 

**Note:** If using a [ready-made integration](/integrations/ready-made/), first check that the payment method is supported. Once the method is activated, also enable it in your [backend](/glossaries/multisafepay-glossary/#backend).

## Activate in your dashboard

- [Banking methods](/payment-methods/banks/), except SEPA Direct Debit (see below)
- E-Invoicing

{{< details title="Activate in your dashboard" >}}

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com). 
2. Go to **Settings**. 
3. To activate the payment method for: 

- All your websites, go to **Payment methods**. 
- A specific website, go to **Website settings**, and click the relevant website. 
4. Select the checkbox for the relevant payment method. 
5. Click **Save changes**.

**Note:** If the payment method isn't visible in your dashboard, email the Integration Team at <integration@multisafepay.com> 
{{< /details >}}

## Apply to MultiSafepay

- [Credit and debit cards](/payment-methods/credit-debit-cards/), Apple Pay, and Google Pay
- AliPay, in3, Pay After Delivery, and WeChat Pay

{{< details title="Apply to MultiSafepay" >}} 
1. Email a request to the Risk Team at <risk@multisafepay.com>  

    For credit and debit cards, Apple Pay, and Google Pay, include in the request your: 
  - Average, minimum, and maximum transaction amount 
  - Annual turnover in credit card transactions

2. The Risk Team checks your eligibilty and if approved, activates the payment method for your MultiSafepay account. 

3. Once approved, for credit and debit cards, Apple Pay, and Google Pay:

- Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com/).
- Go to **Settings**.
- To activate the payment method for:
  - All your websites, go to Payment methods.
  - A specific website, go to Website settings, and click the relevant website.
- Select the checkbox for the relevant payment method.
- Click **Save changes**.

**Note:** If the payment method isn’t visible in your dashboard, email the Integration Team at <integration@multisafepay.com>

{{< /details >}}


## Own flow
{{< details title="AfterPay" >}} 
1. To check you are eligible for AfterPay, email <sales@multisafepay.com>

2. For new AfterPay clients, apply directly to AfterPay:

- The Netherlands: [Offerte](https://www.afterpay.nl/nl/zakelijk/offerte)
- Belgium: [Offerte aanvragen](https://www.afterpay.be/be/footer/zakelijke-partners/offerte-aanvragen)

3. For existing AfterPay clients, to activate AfterPay for your MultiSafepay account, email AfterPay Sales at <sales@afterpay.nl>  
{{< /details >}}

{{< details title="Betaal per Maand" >}}
You must:

- Have a [MultiSafepay account](/getting-started/)
- Be registered with a Dutch Chamber of Commerce (no exceptions)
- Have an annual turnover of more than 500,000 EUR (unless agreed otherwise with Betaal per Maand)
- Sell products or services to European citizens with a residential or delivery address in Netherlands (no exceptions)
- Connect to MultiSafepay via our API or [ecommerce integrations](/payments/integrations/ecommerce-platforms/)

1. Email a request to <sales@multisafepay.com>

2. We check your eligibility and connection with MultiSafepay. 

3. Let us know if you already have a Santander account. If you don't, we'll submit an application for you. 
{{< /details >}}

{{< details title="Edenred" >}}
1. Fill out the Edenred – [Registreer mijn website](https://registreermijnwebsite.edenred.be/) form, selecting the relevant checkbox for each voucher you want to offer.
2. Sign a contract with Edenred, specifying the Edenred vouchers you want to offer.
3. Receive your Edenred Merchant ID.
4. To complete activation, email your Edenred Merchant ID to <sales@multisafepay.com>
{{< /details >}}

{{< details title="Gift cards" >}}
1. To check your eligibility, email <sales@multisafepay.com> 
2. Send a request to the **card issuer**, providing your company details and MultiSafepay account ID.
3. The issuer connects you to the card using one of the following:
- [Intersolve](https://intersolve.nl/contact) (majority of gift cards)
- [Fashioncheque](https://www.fashioncheque.com/nl/customerservice)
- [123TCS](https://www.123tcs.com/#Contact)
4.  The issuer sends us the connection details and we activate the card for your account.
{{< /details >}}

{{< details title="Klarna" >}} 
**Test account**

1. At [Klarna.com](https://www.klarna.com/nl/), sign up for a test account, selecting the **Playground** environment. 
2. Under **Settings**, click **Generate new Klarna API credentials** to generate a user name and password.
3. Email these credentials to <sales@multisafepay.com> 
4. MultiSafepay connects to Klarna. 
5. Test payments in your test environment. 

We recommend testing Klarna payments via the Klarna Portal to experience the full functionality. You can also test from your MultiSafepay dashboard with more limited functionality.

**Live account**

1. Sign up for a live Klarna account:

- Via the Klarna website, selecting the **Production** environment, **or**  
- Email your Klarna account manager or <verkoop@klarna.com>
2. Specify MultiSafepay as your PSP and the countries you want to activate Klarna for.
3. Sign an agreement with Klarna, including pricing.
4. MultiSafepay activates Klarna for your MultiSafepay account. 
5. If using a ready-made integration, activate Klarna in your [backend](/glossaries/multisafepay-glossary/#backend).

For questions, see Klarna – [Klantenservice](https://www.klarna.com/nl/klantenservice).

For support, email the Integration Team at <integration@multisafepay.com>
{{< /details >}}

{{< details title="PayPal" >}}
The instructions below are for the PayPal interface in English. If your PayPal webpage is in another language, you can change the language easily by clicking the links at the bottom right of the page.

**Configuring your PayPal account**

To configure your PayPal account, follow these steps:

1. Sign in to [Paypal.com](https://www.paypal.com) with your business account.
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
3. From the dropdown menu, select **Western European languages (including English)**.
4. Click **More options**.
5. From the **Encoding** dropdown menu, select **UTF-8**.
6. Select the **Yes** checkbox.
7. Click **Save**.

For support or if any steps are inaccurate, email the Integration Team at <integration@multisafepay.com>

{{< alert-notice >}} **Known issue:** If your PayPal business account isn't yet fully verified or approved, you might get a PayPal error 10002: Restricted account. {{< /alert-notice >}}

For support or if any steps are inaccurate, email the Integration Team at <integration@multisafepay.com>

For further support, see PayPal – [Contact us](https://www.paypal.com/us/smarthelp/contact-us).

**Configuring your MultiSafepay account**

To configure your MultiSafepay account for PayPal, follow these steps:

1. Sign in to [Paypal.com](https://www.paypal.com) with your business account.
2. Mouse over your account name in the top-right corner, and then select **Account settings**.
3. On the **Business information** tab, copy your PayPal Merchant ID.
4. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
5. Go to **Settings**. 
6. To activate PayPal for:

- All your websites:
    - Go to **Payment methods**, and then select **PayPal**.
    - In the **PayPal Merchant ID** field, paste in your ID.

- A specific website:
    - Go to **Website settings**, and click the relevant website.
    - Under **Payment methods**, select the **PayPal** checkbox.

**Note:** You can link each website to a separate PayPal business account, or all websites can use your main PayPal business account.

7. Click **Save changes**.

**Note:** If PayPal is not visible as a payment method in your MultiSafepay dashboard, email the Integration Team at <integration@multisafepay.com> 

Your account is now configured. We strongly recommend [testing some transactions](/payment-methods/paypal/integration-testing/) before processing live payments. 
{{< /details >}}

{{< details title="Paysafecard" >}}
Paysafecard doesn't require activation.

Search for outlets that sell Paysafecard:

- English-language site: [Find sales outlets](https://www.paysafecard.com/en/find-sales-outlet-1/)
- Dutch-language site: [Verkooppunten zoeken](https://www.paysafecard.com/nl/verkooppunt-vinden-1/)

For any questions, email the Sales Team at <sales@multisafepay.com>
{{< /details >}}

{{< details title="SEPA Direct Debit" >}} 
1. Email a request to the Risk Team at <risk@multisafepay.com>

- Include in the request the following information:
    - Monthly and annual SEPA Direct Debit transaction volume
    - Minimum and maximum transaction amount
    - Type of products sold using this payment method
    - One-off and/or [recurring payments](/features/recurring-payments/)
    - Subscriptions: Monthly, quarterly, or annual
- Depending on the details provided, the Risk Team sends you a form requesting additional information.
- Fill out and sign the form, and send it back to the Risk Team.

2. The Risk Team checks your eligibilty and if approved, activates the payment method for your MultiSafepay account.
{{< /details >}}





 








