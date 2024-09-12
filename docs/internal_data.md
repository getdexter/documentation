---
title: Integrating with Internal Data
description: How to integrate internal data sources with Dexter.
subtitle: Regardless of where your data is, you can access it in Dexter.
---

Regardless of where your data is, you can access it in Dexter. We offer multiple ways to integrate with your internal data sources:

- HTTP
- Database Apps
- Webhooks
- Custom Apps

# HTTP

HTTP is an app that enables you to make HTTP requests, download files, etc… You can configure all aspects of the request like the url, query parameters, method, headers, body and more.

The output of the step contains the request response and headers.

# Database Apps

We offer apps for all major databases like PostgreSQL, MySQL, BigQuery, SnowFlake, Redshift and more. If your database is not in the list [let us know] and we’ll add support for it.

Most databases support actions like adding a row, finding rows, updating a row, as well as custom queries.

Some databases like PostgreSQL support triggers like updated or added rows.

# Webhooks

You can trigger flows using webhooks. The body of the webhook request can be used to pass inputs to the flow.

# Custom Apps

In addition to built-in apps, you can create custom apps for your company by wrapping a built-in app with clearly defined inputs and outputs.

Let’s take the example of an HTTP app. A company has an internal api available at `https://api.example.com`, with an endpoint to get customer data at `https://api.example.com/customers/<id>`. The endpoint requires a bearer token. The endpoint returns data as JSON: `{"customer": {"id": 123, "name": "Foo"}}`

You can create a custom app that wraps our built-in HTTP app, defining the input as the customer id, and the output as the `customer` object. You can provide a bearer token using a secret.

Now, when using the custom app in a flow, a user just has to set the customer id input value and they are set. No need to dig in the details.

[let us know]: mailto:vincent@getdexter.co?subject=Add%20support%20for%20my%20database
