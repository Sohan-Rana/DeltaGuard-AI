# Suggested Additions to the Idea

## Must-haves for the MVP
1. **Pilot-first approach:** start with 1–2 regions, not all of Bangladesh.
2. **Label strategy doc:** where the flood labels come from, and their limitations.
3. **Baseline first:** a simple model using only rainfall, elevation and distance to river.
4. **Prevent spatial leakage:** if neighboring grid cells are split across train/test, the accuracy will look falsely high.
5. **Class imbalance:** flood cells are rare and non-flood cells are many, so use PR-AUC and class weights.
6. **Data lineage and reproducibility:** tie every model run to a data version and git commit.
7. **Disclaimer in the UI:** "This is a historical risk assessment, not an official warning."

## Possible additions for Version 2
- Bangla + English language support (i18n)
- Location-wise PDF report export
- Climate trend / future scenario overlay (CMIP6, clearly labeled as a "scenario")
- Cyclone/storm surge, riverbank erosion and drought modules
- Population/infrastructure exposure (how many people, schools and roads are at risk)
- Uncertainty map (confidence, not just a score)
- Data drift monitoring and a model retraining pipeline
- Public API keys + rate limiting (commercial stage)
- Offline/low-bandwidth mode (for rural users)

## Commercial angle (later)
- Target users: NGOs, insurance companies, agricultural lenders, local government, infrastructure developers
- Products: location risk report, portfolio risk API
- Partnerships: data/validation with organizations such as BWDB/BMD, IWM, CEGIS and icddr,b

## Risks
- Ground-truth labels are hard to get; this is the project's biggest technical risk.
- Access to local government data may be slow, so the plan is satellite-first.
- Overclaiming: use the word "predict" carefully.
