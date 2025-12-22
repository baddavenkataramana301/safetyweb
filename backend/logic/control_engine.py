from typing import List, Dict

class ControlEngine:
    def __init__(self):
        pass

    def select_controls(self, hazard: str, risk_level: str) -> List[Dict[str, str]]:
        """
        Selects robust controls based on hazard type and risk level.
        Enforces a multi-layered hierarchy of controls approach.
        """
        controls = []
        h = hazard.lower()
        
        # --- FIRE & THERMAL ---
        if any(term in h for term in ["fire", "burn", "thermal", "explosion"]):
            controls.append({"type": "Engineering", "description": "Install fire-resistant barriers and automated suppression systems."})
            controls.append({"type": "Administrative", "description": "Implement Hot Work Permit system and continuous gas monitoring."})
            controls.append({"type": "Administrative", "description": "Designate a dedicated Fire Watcher with firefighting training."})
            controls.append({"type": "PPE", "description": "Flamretardant clothing (FRC), heat-resistant gloves, and face shield."})

        # --- MECHANICAL & MACHINERY ---
        elif any(term in h for term in ["mechanical", "machine", "moving", "grinding", "entrapment", "debris"]):
            controls.append({"type": "Engineering", "description": "Install fixed physical guards and emergency stop buttons."})
            controls.append({"type": "Administrative", "description": "Enforce Lock-Out Tag-Out (LOTO) procedures before maintenance."})
            controls.append({"type": "Administrative", "description": "Operator competency verification/certification check."})
            controls.append({"type": "PPE", "description": "Impact-resistant goggles, cut-resistant gloves, and steel-toed boots."})

        # --- CHEMICAL & TOXIC ---
        elif any(term in h for term in ["chemical", "toxic", "respiratory", "inhalation", "fumes", "gas"]):
            controls.append({"type": "Engineering", "description": "Ensure Local Exhaust Ventilation (LEV) is functioning at >0.5 m/s."})
            controls.append({"type": "Substitution", "description": "Evaluate non-hazardous or water-based alternatives to current solvents."})
            controls.append({"type": "Administrative", "description": "Ensure SDS (Safety Data Sheets) are accessible; perform spill response drill."})
            controls.append({"type": "PPE", "description": "Half-face respirator with P3/Multi-gas filters and chemical-resistant aprons/gloves."})

        # --- HEIGHTS & FALLS ---
        elif any(term in h for term in ["fall", "height", "scaffold", "ladder", "drop", "stability"]):
            controls.append({"type": "Engineering", "description": "Install certified collective protection (guardrails/toeboards)."})
            controls.append({"type": "Engineering", "description": "Use debris netting or exclusion zones with physical barriers below."})
            controls.append({"type": "Administrative", "description": "Daily inspection of scaffolding/ladders by a competent person."})
            controls.append({"type": "PPE", "description": "Class A full-body harness with shock-absorbing double lanyard attached to certified anchor points."})

        # --- ELECTRICAL ---
        elif any(term in h for term in ["electric", "voltage", "wire", "shock", "arc"]):
            controls.append({"type": "Engineering", "description": "Use Residual Current Devices (RCDs) or Ground Fault Circuit Interrupters (GFCIs)."})
            controls.append({"type": "Administrative", "description": "Verify zero-energy state via 'Test-Before-Touch' protocol."})
            controls.append({"type": "PPE", "description": "Arc-rated (AR) clothing, insulated tools, and dielectric boots/gloves."})

        # --- CONFINED SPACE ---
        elif any(term in h for term in ["confined", "asphyxiation", "oxygen", "air quality"]):
            controls.append({"type": "Engineering", "description": "Forced mechanical ventilation for at least 30 minutes prior to entry."})
            controls.append({"type": "Administrative", "description": "Pre-entry atmospheric testing; Standby Person/Attendant required at all times."})
            controls.append({"type": "PPE", "description": "Self-Contained Breathing Apparatus (SCBA) and tripod/winch for emergency retrieval."})

        # --- ENVIRONMENTAL (SLIPS, NOISE, TRIPS) ---
        elif any(term in h for term in ["slip", "trip", "noise", "vibration", "clutter"]):
            controls.append({"type": "Administrative", "description": "Implement 'Housekeeping First' policy; clear walkways of cables/debris."})
            controls.append({"type": "Administrative", "description": "Post 'Hearing Protection Required' signage; limit exposure time."})
            controls.append({"type": "PPE", "description": "High-grip footwear and dual hearing protection (earplugs + earmuffs)."})

        # --- GENERAL FALLBACK ---
        else:
            controls.append({"type": "Administrative", "description": "Conduct a pre-task Toolbox Talk (TBT) specifically for this activity."})
            controls.append({"type": "PPE", "description": "Mandatory Site PPE: High-visibility vest, hard hat, and safety glasses."})

        # Special augmentation for HIGH RISK level
        if risk_level == "High":
            controls.append({"type": "Administrative", "description": "⚠️ Stop Work Authority: Supervisor presence mandatory for the entire duration."})
            controls.append({"type": "Administrative", "description": "Emergency Response Plan (ERP) must be activated and verified before start."})

        return controls
