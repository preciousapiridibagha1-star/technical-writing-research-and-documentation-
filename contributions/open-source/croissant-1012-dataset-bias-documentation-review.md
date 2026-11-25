# Candidate Contribution Review: MLCommons Croissant Issue #1012

**Issue:** [#1012 — Describing known biases/imbalances of a dataset](https://github.com/mlcommons/croissant/issues/1012)  
**Review date:** 25 November 2026  
**Candidate type:** Documentation guidance / worked example  
**Status:** Candidate screened and draft prepared; **not submitted upstream**.

## Why this issue fits

The issue asks how dataset publishers can document a known demographic imbalance, using a hypothetical 70% / 30% gender split. This connects directly to the portfolio's research on dataset documentation, evidence traceability, limitations and audience-specific explanations.

## Upstream material inspected

- [Issue discussion](https://github.com/mlcommons/croissant/issues/1012)
- [Croissant Responsible AI (RAI) specification](https://github.com/mlcommons/croissant/blob/main/docs/croissant-rai-spec.md)
- [DICES-350 dataset example](https://github.com/mlcommons/croissant/tree/main/datasets/1.0/dices-350)
- [BigCode The Stack example](https://github.com/mlcommons/croissant/tree/main/datasets/1.0/bigcode-the-stack)

The issue discussion already contains a maintainer response pointing to the RAI specification and a NOVA example. The inspected specification already provides **rai:dataBiases** (a text description of dataset biases, where applicable) and **rai:dataLimitations**. Repository examples also use rai:dataBiases for language overrepresentation and limits in demographic subgroup coverage. A new schema property does not appear necessary for the issue's basic example.

## Documentation opportunity

The more useful contribution may be a small worked example explaining how to make a percentage interpretable. A statement such as “70% / 30%” should identify, where responsibly disclosable:

- the subset measured and dataset version/date;
- numerator and denominator;
- how categories were collected or assigned;
- missing or unknown labels and whether they are excluded from the denominator;
- sampling, collection-period and category-definition limitations;
- whether sensitive small-group counts should be aggregated or suppressed.

This also avoids presenting dataset composition as an estimate of population prevalence.

### Illustrative wording — not an actual dataset

> In release 1.0, among 1,000 records with a non-missing self-reported gender label, 700 (70%) were labelled [category A] and 300 (30%) [category B]. A further 150 of the 1,150 total records had missing or unknown labels and are not included in this percentage. These figures describe the labelled subset of this dataset; they are not an estimate of the population distribution.

A corresponding rai:dataLimitations statement could explain the effect of sampling, missingness, the collection period and category definitions. This example must be adapted to the actual data and should not be published where it could expose individuals or small groups.

## Proposed change

Add a short authoring note or example to the RAI documentation using existing properties:
1. rai:dataBiases describes the observed imbalance and context.
2. rai:dataLimitations explains sampling, missingness and interpretation limits.
3. Percentages include a denominator and identify the measured subset.
4. Missing/unknown labels are not silently combined with known categories.
5. Dataset composition is not presented as population prevalence.
6. Sensitive small-cell information is protected.

This is a proposal for maintainer discussion, not an accepted change or claim that every item belongs in the schema.

## Draft upstream discussion comment — not submitted

I checked the current Croissant RAI specification and repository examples against the 70/30 case in this issue.

It appears the existing vocabulary can already express this at dataset level without introducing a new property: rai:dataBiases is defined as a text description of dataset biases, and rai:dataLimitations is available for limitations. Existing examples use rai:dataBiases for language overrepresentation and restricted demographic subgroup coverage.

The useful documentation addition may be a worked example explaining how to make a percentage interpretable: identify the measured subset and dataset version; state the numerator and denominator; explain how categories were obtained; report missing/unknown labels and whether they are excluded; and describe sampling and category-definition limitations. This helps avoid implying that a dataset's composition represents the wider population.

For sensitive attributes, exact counts should only be published where disclosure is appropriate; small groups may need aggregation or suppression. I would favour a concise authoring note using the existing RAI properties before proposing new vocabulary.

References: [RAI specification](https://github.com/mlcommons/croissant/blob/main/docs/croissant-rai-spec.md) · [DICES-350](https://github.com/mlcommons/croissant/tree/main/datasets/1.0/dices-350) · [BigCode The Stack](https://github.com/mlcommons/croissant/tree/main/datasets/1.0/bigcode-the-stack)

## Submission status and integrity

An attempt to post this comment through the connected GitHub integration was rejected with HTTP 403 (“Resource not accessible by integration”). No comment was created, no fork was created and no pull request was opened. This is **candidate research and a draft contribution**, not an upstream contribution, accepted proposal or merged documentation change.

