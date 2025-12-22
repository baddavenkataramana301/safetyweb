from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from typing import Optional, List

from models import AssessmentResponse, ControlItem
from logic.hazard_engine import HazardEngine
from logic.risk_engine import RiskEngine
from logic.control_engine import ControlEngine
from logic.document_engine import DocumentEngine

app = FastAPI()

# Enable CORS for frontend - Move to top for best practice
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, replace with specific origins
    allow_credentials=False, # Credentials cannot be True when allow_origins is ["*"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Engines
hazard_engine = HazardEngine()
risk_engine = RiskEngine()
control_engine = ControlEngine()
document_engine = DocumentEngine()

@app.post("/report")
async def generate_report(assessment: AssessmentResponse):
    """
    Generates a downloadable DOCX report based on the provided assessment data.
    """
    # Convert Pydantic model to dict
    data = assessment.dict()
    
    file_stream = document_engine.generate_docx(data)
    
    return StreamingResponse(
        file_stream,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        headers={"Content-Disposition": "attachment; filename=safety_report.docx"}
    )

@app.post("/report/pdf")
async def generate_pdf_report(assessment: AssessmentResponse):
    """
    Generates a downloadable PDF report.
    """
    data = assessment.dict()
    file_stream = document_engine.generate_pdf(data)
    
    return StreamingResponse(
        file_stream,
        media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=safety_report.pdf"}
    )

@app.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    """
    Simulates speech-to-text transcription.
    """
    import time
    print(f"--- Transcription Request Received ---")
    print(f"File: {audio.filename}, Content-Type: {audio.content_type}")
    
    time.sleep(1) # Simulate processing
    
    # Generic default text
    text = "Activity involving heavy machinery and potential electrical hazards in a damp environment."
    
    filename = audio.filename.lower() if audio.filename else ""
    
    # Mock logic based on keywords in filename
    if "weld" in filename:
        text = "Welding steel beams in a confined space with poor ventilation and spark risks."
    elif "height" in filename:
        text = "Working at height on unstable scaffolding during high winds."
    elif "chemical" in filename:
        text = "Handling hazardous chemicals without proper PPE and ventilation."
    
    print(f"Transcribed Text: {text}")
    print(f"--- End Transcription ---")
    
    return {"text": text}



@app.post("/assess", response_model=AssessmentResponse)
async def assess_safety(
    text: str = Form(default=""),
    image: Optional[UploadFile] = File(default=None),
    audio: Optional[UploadFile] = File(default=None)
):
    """
    Main assessment endpoint.
    Orchestrates: Input -> Hazard ID -> Risk Calc -> Control Selection -> Response
    Addresses UAT feedback: Improved NLP, Better Vision simulation, Granular Confidence.
    """
    
    # 1. Vision AI Simulation (Improved for UAT)
    image_tags = []
    vision_confidence_boost = 0
    if image:
        print(f"--- Vision Analysis: {image.filename} ---")
        fname = image.filename.lower()
        # Mocking multi-hazard detection for specific scenarios
        if any(w in fname for w in ["fire", "weld", "spark"]):
            image_tags.extend(["Fire", "Smoke", "Sparks", "High Temperature"])
            vision_confidence_boost = 30
        elif any(w in fname for w in ["height", "scaffold", "ladder"]):
            image_tags.extend(["Height", "Open Edge", "Unstable Platform", "Fall Potential"])
            vision_confidence_boost = 25
        elif any(w in fname for w in ["chemical", "acid", "leak", "drum"]):
            image_tags.extend(["Chemical Spill", "Toxic Fumes", "Corrosive Material"])
            vision_confidence_boost = 20
        elif any(w in fname for w in ["clutter", "messy", "dirt", "construction"]):
            image_tags.extend(["Tripping Hazard", "Obstruction", "Poor Housekeeping"])
            vision_confidence_boost = 15
        elif "dark" in fname or "blur" in fname:
            # Simulate low quality image
            image_tags.extend(["Low Visibility", "Unclear Environment"])
            vision_confidence_boost = -10 # Low quality reduces overall confidence
        else:
            # Randomly pick some generic site tags if generic image
            image_tags.extend(["Site environment", "General workspace"])
            vision_confidence_boost = 5
        print(f"Detected Tags: {image_tags}")
    
    # 2. Hazard Identification & Normalization
    safe_text = text or ""
    # Process through the new engine
    hazard_analysis = hazard_engine.identify_hazards(safe_text, image_tags)
    
    hazards = hazard_analysis["hazards"]
    confidence_level = hazard_analysis["confidence_level"]
    # Final confidence score combines text analysis + vision boost
    confidence_score = min(99, hazard_analysis["confidence_score"] + vision_confidence_boost)

    # Audio fallback handling (if audio provided but not yet transcribed)
    if audio and not safe_text:
        hazards.append("Pending Voice Transcription Analysis")
        confidence_level = "Low"
        confidence_score = 30
    
    if not hazards:
        hazards = ["Unspecified Hazard (Further investigation required)"]
        confidence_level = "Low"
        confidence_score = 20

    # 3. Risk Analysis
    likelihood = 3
    severity = 3
    
    # Dynamic severity based on keywords
    if any(k in hazard_analysis["normalized_text"] for k in ["fatal", "death", "high voltage", "explosion", "crush"]):
        severity = 5
    elif any(k in hazard_analysis["normalized_text"] for k in ["cut", "bruise", "slip", "minor"]):
        likelihood = 4
        severity = 2
    
    risk_result = risk_engine.calculate_risk(
        likelihood=likelihood, 
        severity=severity, 
        missing_controls=False,
        fatal_potential=(severity == 5),
        unclear_info=(confidence_level == "Low")
    )

    # 4. Control Selection
    all_controls = []
    for hazard in hazards:
        controls = control_engine.select_controls(hazard, risk_result["level"])
        for c in controls:
            if c not in all_controls:
                all_controls.append(ControlItem(type=c["type"], description=c["description"]))

    return AssessmentResponse(
        risk_score=risk_result["score"],
        risk_level=risk_result["level"],
        hazards=hazards,
        controls=all_controls,
        confidence=confidence_level,
        confidence_score=confidence_score,
        reasoning=hazard_analysis.get("reasoning"),
        description=hazard_analysis["normalized_text"]
    )

@app.get("/")
def read_root():
    return {"status": "Safety System Backend Running"}
