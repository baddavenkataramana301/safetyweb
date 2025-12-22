
class RiskEngine:
    def __init__(self):
        pass

    def calculate_risk(self, likelihood: int, severity: int, missing_controls: bool = False, fatal_potential: bool = False, unclear_info: bool = False) -> dict:
        """
        Calculates risk score based on Likelihood and Severity.
        Enforces conservative rules.
        """
        final_likelihood = likelihood
        final_severity = severity

        # Rule: Unclear info -> Conservative assumption
        # (Assuming conservative means bumping both or setting to high defaults if not specified, 
        # but here we follow specific rules if provided)
        if unclear_info:
            # If info is unclear, we might bump values or assume worst case if they are low.
            # Implementation choice: Bump likelihood and severity by 1 if possible.
            final_likelihood = min(5, final_likelihood + 1)
            final_severity = min(5, final_severity + 1)

        # Rule: Missing controls -> Likelihood increases
        if missing_controls:
            final_likelihood = min(5, final_likelihood + 1)

        # Rule: Fatal potential -> Severity = 5
        if fatal_potential:
            final_severity = 5

        risk_score = final_likelihood * final_severity
        
        risk_level = "Low"
        if risk_score >= 15:
            risk_level = "High"
        elif risk_score >= 8:
            risk_level = "Medium"
        
        return {
            "score": risk_score,
            "likelihood": final_likelihood,
            "severity": final_severity,
            "level": risk_level
        }
