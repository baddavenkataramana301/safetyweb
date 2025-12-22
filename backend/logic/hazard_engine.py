from typing import List, Dict

class HazardEngine:
    def __init__(self):
        # Expanded knowledge base with categories and synonyms
        self.hazard_dictionary = {
            "fire_hot": {
                "keywords": ["fire", "spark", "flame", "heat", "hot", "welding", "grinding", "explosion", "burn"],
                "hazards": ["Fire Hazard", "Thermal Burn", "Explosion Risk"]
            },
            "mechanical": {
                "keywords": ["machinery", "equipment", "grinding", "sharp", "blade", "moving parts", "crush", "pinch"],
                "hazards": ["Mechanical Injury", "Entrapment", "Flying Debris"]
            },
            "chemical_tox": {
                "keywords": ["chemical", "acid", "toxic", "gas", "fumes", "solvent", "spill", "leak", "poison"],
                "hazards": ["Chemical Exposure", "Respiratory Irritation", "Toxic Inhalation"]
            },
            "height_fall": {
                "keywords": ["height", "ladder", "scaffold", "roof", "fall", "drop", "climb", "unstable"],
                "hazards": ["Fall from Height", "Falling Objects", "Structural Instability"]
            },
            "electrical": {
                "keywords": ["electrical", "wire", "shock", "voltage", "power", "circuit", "exposed", "cable"],
                "hazards": ["Electric Shock", "Arc Flash", "Electrical Fire"]
            },
            "confined": {
                "keywords": ["confined", "tank", "pit", "narrow", "enclosure", "ventilation", "oxygen", "trapped"],
                "hazards": ["Asphyxiation", "Restricted Movement", "Poor Air Quality"]
            },
            "environmental": {
                "keywords": ["lighting", "noise", "vibration", "slippery", "wet", "trip", "dust", "weather"],
                "hazards": ["Slip/Trip Hazard", "Noise Induced Hearing Loss", "Reduced Visibility"]
            }
        }

    def _normalize_text(self, text: str) -> str:
        """
        Simulates robust NLP normalization and basic grammar correction.
        """
        import re
        text = text.lower().strip()
        # Remove punctuation for matching
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Advanced replacements for broken speech/UAT scenarios
        replacements = {
            r"\bgoin\b": "going",
            r"\bweldin\b": "welding",
            r"\bn\b": "and",
            r"\bwat\b": "what",
            r"\bdoin\b": "doing",
            r"\bmessy\b": "cluttered",
            r"\bfixin\b": "repairing",
            r"\bno\b \bvent\b": "poor ventilation",
            r"\bhi\b \bvolt\b": "high voltage",
            r"\bstair\b": "staircase",
            r"\bwire\b": "electrical wiring"
        }
        for pattern, replacement in replacements.items():
            text = re.compile(pattern).sub(replacement, text)
            
        return " ".join(text.split())

    def identify_hazards(self, text_input: str, image_tags: List[str] = []) -> Dict:
        """
        Identifies hazards with detailed tracking for confidence explanation.
        """
        import difflib
        
        normalized_text = self._normalize_text(text_input)
        identified_hazards = set()
        evidence_matches = []
        
        # Merge text input and image tags
        search_terms = normalized_text.split() + [tag.lower() for tag in image_tags]
        
        for category, data in self.hazard_dictionary.items():
            category_match = False
            for keyword in data["keywords"]:
                # Direct check
                if keyword in normalized_text:
                    category_match = True
                    evidence_matches.append(f"Keyword '{keyword}' found in text")
                # Fuzzy check
                else:
                    fuzzy_matches = difflib.get_close_matches(keyword, search_terms, n=1, cutoff=0.8)
                    if fuzzy_matches:
                        category_match = True
                        evidence_matches.append(f"Fuzzy match '{fuzzy_matches[0]}' (for '{keyword}')")
                
                if category_match:
                    for h in data["hazards"]:
                        identified_hazards.add(h)
                    break # Category identified, move to next

        # Image-specific overrides
        for tag in image_tags:
            tag_l = tag.lower()
            if "fire" in tag_l: 
                identified_hazards.add("Fire Hazard")
                evidence_matches.append("Visual evidence of Fire/Sparks detected")
            if any(t in tag_l for t in ["trip", "clutter", "messy"]):
                identified_hazards.add("Slip/Trip Hazard")
                evidence_matches.append("Visual evidence of cluttered workspace")

        # Confidence calculation
        if not identified_hazards:
            confidence_score = 10
            confidence_level = "Low"
            reasoning = "No specific safety keywords or hazards identified in input."
        else:
            # Score based on number of evidence matches
            match_count = len(evidence_matches)
            base_score = 30 + (match_count * 15)
            # Add bonus for multi-modal (both text and image) overlap
            if text_input and image_tags:
                base_score += 15
            
            confidence_score = min(99, base_score)
            confidence_level = "High" if confidence_score > 75 else "Medium" if confidence_score > 40 else "Low"
            reasoning = f"Analysis based on {match_count} distinct hazard indicators: {', '.join(evidence_matches[:3])}..."

        return {
            "hazards": list(identified_hazards),
            "confidence_score": confidence_score,
            "confidence_level": confidence_level,
            "normalized_text": normalized_text,
            "evidence": evidence_matches,
            "reasoning": reasoning
        }
