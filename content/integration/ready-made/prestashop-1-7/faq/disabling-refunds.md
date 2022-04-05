---
title : "Disabling refunds"
meta_title: "PrestaShop 1.7 - Disabling refunds - MultiSafepay Docs"
read_more: "."
url: '/prestashop-1-7/disable-refunds/'
---

By default, refunds initiated in your PrestaShop [backend](/glossaries/multisafepay-glossary/#backend) are automatically processed via our API.

 To disable this, follow these steps:

1. Sign in to your PrestaShop 1.7 backend.
2. Go to **MultiSafepay module** > **Manage hooks**.
3. Select **Display non-positionable hooks**.
4. For **actionOrderSlipAdd**, select the three dots, and then click **Unhook**.