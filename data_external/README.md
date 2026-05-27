# External Data Notes

SPARC public rotmod files were used in Phase 4AB and related internal SPARC diagnostics in the user's WSL environment. The full rotmod source data are not bundled here unless separately added by the user.

Suggested retrieval command used during development:

```bash
mkdir -p data_external/sparc_public_rotmod
cd data_external/sparc_public_rotmod
curl -L -o Rotmod_LTG.zip https://astroweb.case.edu/SPARC/Rotmod_LTG.zip
unzip -q Rotmod_LTG.zip -d Rotmod_LTG
```

The non-SPARC external residual-level validation branch remains HOLD until usable component-curve material arrives.
