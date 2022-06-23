---
title: "Exact"
category: 62962dee7af1c800355771a1
order: 204
hidden: false
parentDoc: 629f40cdef2c3001bbd78848
slug: 'exact'
---

<img src="https://raw.githubusercontent.com/MultiSafepay/docs/master/static/svgs/Exact.svg" width="150" align ="right" style="margin: 20px; max-height: 75px"/>
<br>

You can import MultiSafepay [accountant export](/accounting/reports/accountant-export/) reports (in MT940 format) into [Exact](https://www.exact.com/nl) Globe or Online. 

# Prerequisites
<details id="prerequisites">
<summary>Prerequisites</summary>
<br>

- You must first provide Exact with an additional international bank account number (IBAN). This can be a dummy (placeholder) IBAN.  

- Exact Basic / Standard package doesn't support the MT940 import function. You need at least Exact Advanced.  

- Lightspeed users must request Lightspeed to make an adjustment to make sure order numbers appear in the correct fields in Exact Online to successfully match the MultiSafepay MT940.

- Exact Globe and Exact Online both import and match MultiSafepay MT940 reports provided that:
    - Your accounting package can process MT940 files.
    - The order numbers in the MT940 files also appear in the correct invoice fields in your accounting platform.
    - The customer's name and order amounts that appear in the exported MT940 files match your accounting platform.

</details>

# Generating dummy IBANs

<details id="generating-dummy-ibans">
<summary>Generating dummy IBANs</summary>
<br>

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** drop-down menu, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.  
A dummy IBAN and BIC code are generated.

</details >

# Submitting IBANs

<details id="submitting-ibans-to-exact-globe">
<summary>Submitting IBANs to Exact Globe</summary>
<br>

1. Sign in and go to **Bank accounts**.
2. Click **New**.
3. Under **Type**, select **Payment service provider**. 
4. Enter the dummy IBAN and select the same bank as before, e.g. ING Group.
5. Click **Save**.  
    You can now register all transactions linked to this IBAN.

</details>

<details id="submitting-ibans-to-exact-online">
<summary>Submitting IBANs to Exact Online</summary>
<br>

1. Sign in and go to **Financial** > **Banking & Cash** > **Bank accounts** > **Overview**.
2. Click **New**.
3. Enter your dummy IBAN, and then click **Save**.  
    You can now register all transactions linked to this IBAN.

</details>

# Generating accountant exports

<details id="generating-accountant-exports" >
<summary>Generating accountant exports</summary>
<br>

To export MT940 reports from your MultiSafepay dashboard, follow these steps:

1. Sign in to your [MultiSafepay dashboard](https://merchant.multisafepay.com).
2. Go to **Reports** > **Accountant Export**:  
    - In **Data Selection**, select a date range.
    - In the **Report Type** field, select **MT940**.
3. Click **Advanced options**:
    - In the **Bank Account / IBAN** field, enter the dummy IBAN.
    - In the **BIC** field, enter the dummy BIC code.

</details>

# Importing into Exact Online

<details id="importing-into-exact-online">
<summary>Importing into Exact Online</summary>
<br>

To import an MT940 report into Exact Online, follow these steps:

1. Sign in to your Exact Online account.
2. Go to **Financial** > **Banking & Cash** > **Statements** > **Import**.
3. Click **Choose File**, and then select the MT940 file you want to upload.
4. Click **Import**.

</details>

# Denovit integration

You can automatically insert MultiSafepay [payment links](/payments/checkout/payment-link/) into Exact invoices using the [Denovit payment link module](https://www.denovit.nl/Exact-PaymentLink).

<details id="setting-up-denovit">
<summary>Setting up Denovit</summary>
<br>

1. Sign in to your Denovit account.
2. Go to your **Dashboard**, and then select the **Paylink** module. 
3. Connect to your Exact account.
4. Under **PSP settings**, enter your [MultiSafepay API key](/glossaries/multisafepay-glossary/#api-key) and the payment conditions you use in Exact. 
5. Adjust other settings as relevant, e.g. personalize your email template, thank-you page, or notification email to improve customer experience.

For each new invoice in Exact, if you:

- **Email**: The customer receives a second email containing a payment link, in addition to the normal email.
- **Print and process**: The customer receives an email containing a payment link.

</details >

# xCore integration

Automatically reconciling sales from your site with payments received via MultiSafepay saves time and increases accuracy.

xCore offers two reconciliation apps for Exact accounting tools. The apps automatically retrieve the details of all payments for the day from MultiSafepay, and then match each payment to the corresponding open item in Exact.

## Exact Online

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FMc6_ZV1AoT8%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DMc6_ZV1AoT8&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FMc6_ZV1AoT8%2Fhqdefault.jpg&key=f2aa6fc3595946d0afc3d76cbbd25dc3&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=Mc6_ZV1AoT8&feature=youtu.be",
  "title": "Demo - MultiSafepay Aflettermodule Exact Online xCore",
  "favicon": "https://www.youtube.com/s/desktop/d4eb50c8/img/favicon.ico",
  "image": "https://i.ytimg.com/vi/Mc6_ZV1AoT8/hqdefault.jpg"
}
[/block]
<br>

For more information, see xCore – [Afletteren 2.0 Exact Online with MultiSafepay](https://xcore.nl/afletteren-2-0-exact-online-multisafepay/).

## Exact Globe

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fa74k2vJVhxQ%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Da74k2vJVhxQ&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2Fa74k2vJVhxQ%2Fhqdefault.jpg&key=f2aa6fc3595946d0afc3d76cbbd25dc3&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=a74k2vJVhxQ&feature=youtu.be",
  "title": "Demo - Afletteren Exact Globe",
  "favicon": "https://www.youtube.com/s/desktop/d4eb50c8/img/favicon.ico",
  "image": "https://i.ytimg.com/vi/a74k2vJVhxQ/hqdefault.jpg"
}
[/block]
<br>

For more information, see xCore – [Afletteren MultiSafepay met Exact Globe](https://xcore.nl/afletteren-exact-globe-multisafepay/).

[block:html]
{
  "html": "<blockquote class=\"callout callout_info\">\n    <h3 class=\"callout-heading false\">\n        <span class=\"callout-icon\">💬</span>\n        <p>Support</p>\n    </h3>\n    <p>Email <a href=\"mailto:support@multisafepay.com\">support@multisafepay.com</a></p>\n</blockquote>\n"
}
[/block]