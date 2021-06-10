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
---

For generating MultiSafepay accounting reports, see [Accountant export](/tools/accounting/reports/accountant-export/).

{{< details title="Supported import formats" >}}  
&nbsp;  
Exact can import reports in MT940 format.

{{< /details >}}

{{< details title="Import instructions" >}}
&nbsp;  
To import a MultiSafepay Accountant export into [Exact Online](https://www.exact.com/software/exact-online) or [Exact Globe](https://www.exact.com/software/exact-globe), follow these steps:

1. Log in to your [Exact Online account](https://start.exactonline.nl/docs/Login.aspx?ReturnUrl=%2fdocs%2fMenuPortal.aspx#_ga=2.221698527.659438293.1581330144-1715983246.1581330144).
2. Go to **Financial** > **Banking & cash** > **Statements** > **Import**.
3. Click **Choose file**, and then select the relevant MT940 file.
4. Click **Import**.

**Requirements**:

- The order numbers in the Accountant export (e.g. 200160526) must also appear in the correct invoice fields in Exact.
- The customer’s name and the order amounts in the Accountant export must match those in Exact.
- Your Exact package must support MT940 format. Exact Basic / Standard package does not. At least Exact Advanced is required. 
- Lightspeed users must make sure that order numbers appear in the correct field in Exact to match the MT940 format.

{{< /details >}}

For any questions, email the Support Team at <support@multisafepay.com>
