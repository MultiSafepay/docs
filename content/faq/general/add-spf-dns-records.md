---
title : "Can I add SPF DNS records for the emails MultiSafepay sends?"
meta_title: "FAQ General - Add SPF DNS records - MultiSafepay Docs"
meta_description: "The MultiSafepay Documentation Center presents all relevant information about our Plugins and API. You can also find support pages for payment methods, tools and general questions as well as the contact details of our Support and Integration Teams."
read_more: "."
---

SPF stands for Sender Policy Framework. In an SPF record you can define which servers can send emails on behalf of your domain name. A receiving server can, among other things, decide on the basis of the SPF record to let an email pass, mark it as unsafe or refuse it altogether.

We do use an SPF record to prevent our emails from being marked as spam.

The following _TXT record_ can be added to the [DNS](https://nl.wikipedia.org/wiki/Domain_Name_System) of the customers:

* v = spf1 ip4: 213.189.0.0/23 mx

* v = spf1 ip4: 185.99.128.0/22 mx

Please not that the name of the file should be the name of your website.
