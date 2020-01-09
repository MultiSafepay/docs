---
title : "Automated Accountant Export"
weight: 61
meta_title: "Automated Accountant Export - MultiSafepay Support"
meta_description: "In the MultiSafepay Documentation Center all relevant information regarding our Plugins and API. As well as Support pages for Payment Method, Tools and General Questions. You can also find the contact details of our Support Team and Integration Team."
read_more: '.'
---

**_The Automated Accountant Export via SFTP is currently in Beta and is available for testing via [MultiSafepay Test Control](https://testmerchant.multisafepay.com/)_.**

## Accountant Export
An Accountant Export containing all successful incoming and outgoing transactions, as well as corresponding costs (where applicable), can be generated to serve your bookkeeping needs. 

## Sending an Automated Accountant Export
As a MultiSafepay client, you can benefit from three ways of accessing/receiving the automated accountant export:

1. Via email
2. Via SFTP - Pull request _(With this method you will receive access to an SFTP server from MultiSafepay)_
3. Via SFTP - Push request _(With this method MultiSafepay would like to receive access to an SFTP server from you)_.

We support SFTP by username/password and username/SSH keys.

_We only support port 22 & 2222 for SFTP connections_

## Frequency
MultiSafepay can send the Automated Accountant Export daily, weekly or monthly.  You have the option of choosing the frequency and time. Our reference time is Central Eastern Summer Time (CEST).

## Accountant Export format
The following formats are available for automatically generating an export:

1. CAMT053
2. CODA
3. CSV
4. MT940
5. XLS
6. XLSX

For information regarding the different exports, check out our [exports page](/tools/reports/).   

## How to request an Automated Accountant Export

Automated Accountant Export activation checklist:

* Choice of email, SFTP push or SFTP pull            
* Frequency - daily, weekly or monthly
* Desired file format: CAMT053, CODA, CSV, MT940, XLS or XLSX
* Desired time (_Please note our reference time is CEST_).
* Costs breakdown per transaction OR total costs 


Send the requested to our Integration Team via <integration@multisafepay.com> 

_Don't forget to add your MultiSafepay Control number_.

## Whitelisting

If your method of choice is via SFTP, please make sure our IP is whitelisted. For more information, please refer to our [IP ranges documentation](/faq/general/ip-ranges/).

