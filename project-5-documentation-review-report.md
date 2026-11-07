# Documentation Review: Current Portfolio Samples

**Reviewed by:** Precious Apiri Dibagha  
**Review status:** Initial review  
**Scope:** The README and the four existing cloud AI assistant writing samples  
**Date:** 7 November 2026

## Why this review was written

I reviewed the documents currently in this repository to understand what is already useful, what needs more work and what should not yet be presented as finished professional work.

This is an initial review, not a formal certification or an independent technical audit. I have not tested a live cloud AI product, inspected its code or verified every technical statement against a vendor's documentation. The findings below are based on the content of the files in this repository.

## Documents reviewed

- `README.md`
- `project-1-software-overview.md`
- `project-2-faq-document.md`
- `project-3-user-guide.md`
- `project-4-research-brief.md`

The Talent Paradox is a separate research paper and needs its own review. It is not graded in this document.

## What is working so far

### 1. The documents have a clear starting structure

The overview, FAQ, user guide and research brief each have a recognisable purpose. Headings and lists make the content fairly easy to scan, including on a phone.

### 2. The writing is generally accessible

Most explanations avoid unnecessary technical detail. The samples try to explain AI assistants to people who may use the tools without building them.

### 3. The set shows different documentation tasks

Taken together, the files demonstrate an attempt to write a product overview, answer common user questions, explain a basic user journey and compare two broad types of AI systems. That is a useful foundation for a portfolio.

## What needs to improve

### 1. The product being documented is not clearly identified

The overview and user guide describe a general category of cloud AI assistants. They do not explain one named product, its actual interface, supported features, account requirements or known limitations.

That means the current user guide is closer to a general usage outline than a guide someone could follow to use a particular product. We should either choose a real product and verify its features, or clearly label the material as a general illustrative example.

### 2. Some security and privacy statements are too broad

The FAQ refers to encryption such as TLS and AES-256 and suggests that enterprise platforms use these protections. The research brief also describes local models as offering complete privacy and absolute data sovereignty.

These statements need qualification. Security controls differ between providers and deployment arrangements. Running a model locally can reduce some data-sharing risks, but it does not automatically make a device, application or network secure. We should name the exact product or deployment being discussed and link to reliable technical documentation before making specific claims.

### 3. The comparison in the research brief needs more careful treatment

The brief compares proprietary cloud models with open-weight or locally hosted models. This is a useful topic, but the current categories are too neat. Open-weight models are not all deployed locally, and local deployment does not automatically mean that every part of a system is open source.

Claims about hardware requirements, cost, privacy, offline access and customisation should be checked against specific examples. A comparison should also explain that performance and requirements vary by model and hardware.

### 4. The user guide does not yet guide a reader through a real task

The three steps—open the platform, write an instruction, review the answer—are understandable, but they do not cover account setup, attaching a file, managing a conversation, exporting work, reporting a problem or checking the product's current limitations.

We should not add instructions for features until they have been confirmed for the product selected.

### 5. The FAQ needs more useful, specific answers

The questions cover relevant themes, but some answers are broad. For example, the answer about integrations says that most modern platforms offer APIs, browser extensions or direct integrations. That is not true of every platform in the same way.

The revised FAQ should distinguish between what is generally possible and what a named product actually supports. It should also include practical questions a new user is likely to ask.

### 6. The research brief needs sources and a clearer method

The brief makes claims about model hosting, hardware, privacy, customisation and maintenance without citing sources. It also does not explain how the products or examples were selected.

A stronger version should state its research question, define the comparison criteria, identify the sources consulted and give the date those sources were checked. It should separate documented facts from the author's interpretation.

### 7. The README needs to work as a portfolio landing page

The current README combines the portfolio introduction with a long section about The Talent Paradox. It also contains placeholder links for reading and downloading the report, rather than working links. A note about the missing PDF link was accidentally left in the text.

The README should introduce the author and the focus of the portfolio, then direct readers to individual projects. The research paper should have its own project page and should only offer a PDF download if an actual PDF is present in the repository.

## Current assessment

I am not assigning letter grades or describing these files as fully verified. That would give readers more confidence than the current evidence supports.

At this stage, the files are **early portfolio samples**. They show a useful starting ability to organise information and explain general concepts, but they need more product-specific detail, source checking and practical examples before they can be treated as finished documentation.

## Recommended revision order

1. Decide whether the cloud AI assistant samples will document one real product or remain clearly labelled general examples.
2. Revise the product overview so that its scope, audience, features and limitations are precise.
3. Rework the FAQ using questions grounded in the chosen product and reliable sources.
4. Turn the user guide into a practical task-based guide, checking every instruction against the actual product.
5. Rebuild the research brief with a transparent method, specific examples and citations.
6. Rewrite this review after those changes and record what was actually checked.

## Review limitations

This review is based on the repository documents available at the time of writing. It is not a security assessment, product test, peer review or certification. No claim is made that the documents have been independently verified or that the described systems have been implemented.

The purpose is to be clear about the work completed so far and to give the next revision a practical direction.
