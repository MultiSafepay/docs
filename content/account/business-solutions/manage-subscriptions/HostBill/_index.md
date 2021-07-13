---
title: "HostBill"
weight: 20
meta_title: "HostBill - MultiSafepay Docs"
meta_description: "Sign up. Build and test your payments integration. Explore our products and services. Use our API Reference, SDKs, and wrappers. Get support."
logo: '/svgs/HostBill.svg'
layout: 'single'
title_short: "HostBill"
read_more: "."
short_description: "Subscription management by HostBill"
description_short: "Read about subscription management by HostBill."
extra_button:
    url: "https://hostbillapp.com/" 
    text: "Go to site" 
    type: "primary"
aliases:
    - /integrations/credit-and-subscription-management/hostbill/
---

Our partner HostBill's billing and automation software handles all aspects of running an online business, from client acquisition, invoicing, payments and management, to customer service and support.

To integrate MultiSafepay as your payment provider, follow these steps:

**Step 1.** Activate the MultiSafepay module in your HostBill account.

1. Sign in to your HostBill account.
2. Click **Extras** > **Plugins**.
3. From the left menu, select **Payment modules** > **MultiSafepay**.
4. Click **Edit general settings**, and then enter your [MultiSafepay API key](/getting-started/set-up-your-account/user-guide/viewing-your-api-key/).
5. Click **Save changes**.

**Step 2.** Configure the module as required, e.g. the [module name and callback URL](https://hostbill.atlassian.net/wiki/spaces/DOCS/pages/559120402/MultiSafepay).

**Step 3.** Perform a test transaction.

1. Go to the top menu and select **Clients** > **Manage clients**, and then click  the sample client account **John Doe**.
2. Click **Login as client**.  
    You are redirected to the client area
3. From the left menu, select **Billing** to view the client’s invoices. 
4. Choose an invoice and click **Pay selected invoices**.
5. Perform a test transaction.
6. When the transaction is complete, check its status under **Payments**.
