---
title: "Exact"
weight: 20
meta_title: "Exact - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: '/svgs/Exact.svg'
layout: 'single'
buttons_under_text: "Third-party integrations"
title_short: "Exact"
read_more: "."
short_description: "Read about how you can generate a MultiSafepay export and import to your Exact platform"
description_short: "Read about how you can generate a MultiSafepay Accountant Export for your Exact software platform."
extra_button:
    url: "https://www.exact.com/nl" 
    text: "Go to site" 
    type: "primary"
aliases:
    - /faq/finance/set-up-exact-online-platform
    - /faq/general/set-up-exact-globe-platform
    - /faq/finance/setting-up-exact-globe-and-exact-online
---

You can export MT940 accountant reports from your MultiSafepay account and import them into your Exact Globe or Exact Online account. 

You must first provide Exact with an additional international bank account number (IBAN). This can be a _dummy_, or placeholder, IBAN.  

## Generating dummy IBANs
To generate a dummy IBAN, follow these steps:

1. Go to IBAN Calculator – [Calculate an IBAN](https://www.ibancalculator.com/bic_und_iban.html). 
2. From the **Country** drop-down menu, select **The Netherlands**.
3. Under **Bank Code**, enter a bank, e.g. ING Group.
4. In the **Account number** field, enter any 7 digits.
5. Click **Calculate IBAN**.
6. A dummy IBAN and BIC code are generated.

## Providing dummy IBANs to Exact
To provide the dummy IBAN to Exact, follow these steps:

| Step  | Exact Globe   | Exact Online   |
|---|---|---|
| 1. | Sign in and go to **Bank accounts**. |  Sign in and go to **Financial** > **Banking & Cash** > **Bank accounts** > **Overview**. |
| 2. | Click **New**. | Click **New**. |
| 3. | Under **Type**, select **Payment service provider**. | Enter your dummy IBAN. |
| 4. | Enter the dummy IBAN and select the same bank as before, e.g. ING Group.  | Click **Save**.  |
| 5.  | Click **Save**.  |   |

You can now register all transactions linked to this IBAN.

## Exporting from your MultiSafepay account
To export MT940 reports from your MultiSafepay account, follow these steps:

1. Sign in to your MultiSafepay account.
2. Go to **Reports** > **Accountant Export**. 
3. In **Data Selection**, select a date range.
4. In the **Report Type** field, select **MT940**.
5. Click **Advanced options**.
6. In the **Bank Account / IBAN** field, enter the dummy IBAN.
7. In the **BIC** field, enter the dummy BIC code.

## Importing into Exact Online
To import an MT940 report into Exact Online, follow these steps:

1. Sign in to your Exact Online account.
2. Go to **Financial** > **Banking & Cash** > **Statements** > **Import**.
3. Click **Choose File**, and then select the MT940 file you want to upload.
4. Click **Import**.

Exact Globe and Exact Online both import and match MultiSafepay MT940 reports provided that:

- Your accounting package can process MT940 files.
- The order numbers in the MT940 files also appear in the correct invoice fields in your accounting platform.
- The customer's name and order amounts that appear in the exported MT940 files match your accounting platform.

**Note:** Exact Basic / Standard package doesn't support the MT940 import function. You need at least Exact Advanced.

**Note:** Lightspeed users must request Lightspeed to make an adjustment to make sure order numbers appear in the correct fields in Exact Online to successfully match the MultiSafepay MT940.

For any questions, email the Support Team at <support@multisafepay.com>
