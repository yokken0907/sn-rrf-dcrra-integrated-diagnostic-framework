# Restart Protocol If External Data Arrives

Use this only if a non-SPARC source provides usable radius-resolved baryonic component-curve material.

## First action

Do not jump to full validation. Start with manual source-material acceptance.

## Minimum acceptance checklist

- Provenance and permission to use the data are clear.
- Galaxy IDs are identifiable.
- Radius column exists and units are documented.
- Observed rotation curve exists.
- Gas component curve exists.
- Stellar disk component curve exists.
- Bulge component curve exists where applicable, or absence is explicitly documented.
- Units and sign conventions are documented.
- Missing values and uncertainty fields are documented.
- Use conditions and citation requirements are documented.

## Branch rule

If accepted, create a new external branch and keep it separate from the internal SPARC v3.0.0 synthesis until validation results are actually obtained.

## Possible outcomes

- PASS: external structure supports a subset of the internal diagnostic structure within tested scope.
- MIXED: partial agreement and partial failure; update failure-boundary ledger.
- FAIL: internal SPARC diagnostic structure does not generalize to the external component-curve table.
- HOLD: source material is incomplete, private, unusable, or not sufficiently documented.
