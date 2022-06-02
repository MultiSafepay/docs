---
title: "Yuki"
weight: 20
meta_title: "Yuki - MultiSafepay Docs"
logo: '/svgs/Yuki.svg'
layout: 'single'
title_short: "Yuki"
read_more: "."
short_description: "Read about how you can generate a MultiSafepay export and import to your Yuki platform"
description_short: "Read about how you can generate a MultiSafepay Accountant Export for your Yuki software platform."
aliases:
    - /tools/accounting/accounting-integrations/yuki/
    - /accounting/integrations/yuki/integrations/duopact/
---
This page sets out ways of integrating MultiSafepay with [Yuki](https://www.yuki.nl/nl/).

## Importing accountant exports

You can import MultiSafepay [accountant export](/accounting/reports/accountant-export/) reports (in MT940 format) into Yuki.

{{< details title="Importing accountant exports" >}}

1. Sign in to your Yuki domain ending in **@yukiworks.be**.
2. Go to **Yuki Postbus** > **Submit**.
3. Click **Upload**, and select the relevant MT940 file, or choose one of the other upload methods.

For more information, see Yuki - [Upload files from PO box](https://support.yuki.nl/en/support/solutions/articles/80000786497-upload-files-from-po-box).

{{< /details >}}

## Automating reconciliation

{{< details title="Automatically reconcile using bank recognition rules">}}

1. Go to **Bank transactions to be processed** > **(New) Processing rule**.
2. Create a new rule. 

For more information, see Yuki - [Create bank processing rule](https://support.yuki.nl/nl/support/solutions/articles/80000787813-bank-verwerkingsregel-aanmaken).

{{< /details >}}

## Duopact integration

You can also integrate with [Duopact](https://www.snelkoppeling.eu/productoverzicht/webwinkelkoppelingen). MultiSafepay transactions are automatically imported daily at midnight.

{{< details title="Connecting Duopact with MultiSafepay" >}}

To connect Duopact with your MultiSafepay account, see Duopact – [Contact](https://www.duopact.nl/nl/contact/).  

Provide Duopact with your MultiSafepay [site API key](/account/managing-websites/#viewing-the-site-id-api-key-and-secure-code). They will set up a Yuki account for you. 

{{< /details >}}

{{< details title="Manually importing transactions" >}}

1. Sign in to your [Duopact account](https://portal.yukiconnector.nl/).
2. If you operate multiple websites, select the relevant site from the top-left menu.
3. Go to **Bankmutaties** > **MultiSafepay**.
4. Click the green button under the **Status** tab.

**Note:** Manually importing transactions doesn't affect automatic imports.

{{< /details >}}

{{< blue-notice >}}**Support** <br> Email support@multisafepay.com {{< /blue-notice >}}

