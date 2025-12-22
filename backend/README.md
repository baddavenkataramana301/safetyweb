# Safety Backend - VSMS API

FastAPI-based backend server for the Versatile Safety Management System with AI-powered safety analysis.

## Features

- **AI Safety Analysis**: Google Gemini AI integration for intelligent hazard identification
- **Multi-Modal Processing**: Handle text, images, and audio inputs
- **Voice-to-Text**: Automatic transcription of voice recordings
- **Image Analysis**: AI-powered image recognition for hazard detection
- **Report Generation**: Generate comprehensive safety reports in multiple formats
- **RESTful API**: Clean, well-documented API endpoints
- **CORS Support**: Configured for frontend-backend communication
- **Auto Documentation**: Interactive API docs with Swagger UI

## Tech Stack

- **Framework**: FastAPI
- **AI/ML**: Google Gemini AI (gemini-1.5-flash)
- **Image Processing**: PIL (Python Imaging Library)
- **Audio Processing**: Speech recognition
- **Server**: Uvicorn (ASGI server)
- **Language**: Python 3.8+

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Google Gemini API key

## Installation

1. Navigate to the backend directory:

```bash
cd backend
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set up environment variables:

Create a `.env` file in the backend directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

To get a Google Gemini API key:
- Visit: https://makersuite.google.com/app/apikey
- Sign in with your Google account
- Create a new API key
- Copy and paste it into your `.env` file

## Running the Server

### Development Mode (with auto-reload)

```bash
python -m uvicorn main:app --reload --port 8000
```

### Production Mode

```bash
python -m uvicorn main:app --port 8000
```

The server will be available at:
- **API**: `http://localhost:8000`
- **Interactive Docs**: `http://localhost:8000/docs`
- **Alternative Docs**: `http://localhost:8000/redoc`

## API Endpoints

### Health Check
- `GET /` - Check if the API is running

### AI Analysis
- `POST /assess` - Perform AI safety assessment
  - Accepts: text, image (multipart/form-data), audio
  - Returns: Comprehensive safety analysis with hazards, risks, and recommendations

### Voice Processing
- `POST /transcribe` - Transcribe audio to text
  - Accepts: audio file (multipart/form-data)
  - Returns: Transcribed text

### Report Generation
- `POST /report` - Generate safety report
  - Accepts: Assessment results (JSON)
  - Returns: Formatted report data

- `GET /report/pdf` - Download PDF report
  - Accepts: Assessment results (query params)
  - Returns: PDF file

## Request Examples

### AI Assessment with Text

```bash
curl -X POST "http://localhost:8000/assess" \
  -F "text=Working with electrical equipment in a wet environment"
```

### AI Assessment with Image

```bash
curl -X POST "http://localhost:8000/assess" \
  -F "image=@workplace_photo.jpg" \
  -F "text=Factory floor inspection"
```

### Voice Transcription

```bash
curl -X POST "http://localhost:8000/transcribe" \
  -F "audio=@voice_note.webm"
```

## Response Format

### Assessment Response

```json
{
  "hazards": [
    {
      "name": "Electrical Shock",
      "severity": "High",
      "likelihood": "Medium",
      "risk_level": "High",
      "description": "Risk of electrical shock in wet environment",
      "controls": [
        "Use GFCI protection",
        "Ensure proper grounding",
        "Keep work area dry"
      ]
    }
  ],
  "overall_risk": "High",
  "recommendations": [
    "Implement lockout/tagout procedures",
    "Provide PPE training",
    "Regular equipment inspection"
  ],
  "confidence": 0.92
}
```

## Project Structure

```
backend/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── .env                # Environment variables (not in git)
├── .gitignore          # Git ignore file
└── README.md           # This file
```

## Dependencies

Key Python packages:
- `fastapi` - Web framework
- `uvicorn` - ASGI server
- `google-generativeai` - Google Gemini AI SDK
- `python-multipart` - File upload support
- `pillow` - Image processing
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Google Gemini API key | Yes |
| `PORT` | Server port (default: 8000) | No |
| `HOST` | Server host (default: 0.0.0.0) | No |

## CORS Configuration

The API is configured to accept requests from:
- `http://localhost:3000` (Frontend dev server)
- `http://localhost:5173` (Alternative Vite port)

To add more origins, update the `allow_origins` list in `main.py`.

## Error Handling

The API returns standard HTTP status codes:
- `200` - Success
- `400` - Bad Request (invalid input)
- `422` - Unprocessable Entity (validation error)
- `500` - Internal Server Error

Error responses include detailed messages:

```json
{
  "detail": "Error description here"
}
```

## AI Model Configuration

The backend uses Google's Gemini 1.5 Flash model with:
- **Temperature**: 0.7 (balanced creativity/accuracy)
- **Max Tokens**: 2048
- **Safety Settings**: Configured for workplace safety analysis

## Performance Optimization

- Async/await for concurrent request handling
- Efficient image processing with PIL
- Streaming responses for large reports
- Request validation with Pydantic

## Security Considerations

- API key stored in environment variables
- Input validation on all endpoints
- File size limits for uploads
- CORS restrictions
- No sensitive data logging

## Deployment

### Heroku

1. Create `Procfile`:
```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. Deploy:
```bash
heroku create your-app-name
git push heroku main
heroku config:set GOOGLE_API_KEY=your_key
```

### Railway

1. Connect GitHub repository
2. Set environment variables in dashboard
3. Deploy automatically on push

### Render

1. Create new Web Service
2. Connect repository
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Add environment variables

## Testing

### Manual Testing

Use the interactive API docs at `http://localhost:8000/docs` to test endpoints.

### Using curl

```bash
# Test health check
curl http://localhost:8000/

# Test assessment
curl -X POST http://localhost:8000/assess \
  -F "text=Testing safety assessment"
```

### Using Postman

1. Import the OpenAPI schema from `/docs`
2. Set base URL to `http://localhost:8000`
3. Test endpoints with different inputs

## Troubleshooting

### API Key Issues
- Verify `GOOGLE_API_KEY` is set in `.env`
- Check API key is valid at Google AI Studio
- Ensure no extra spaces in the key

### Import Errors
- Reinstall dependencies: `pip install -r requirements.txt`
- Check Python version: `python --version`
- Use virtual environment

### CORS Errors
- Verify frontend URL in `allow_origins`
- Check browser console for exact error
- Ensure credentials are included in requests

### Port Already in Use
- Kill existing process: `lsof -ti:8000 | xargs kill -9` (Mac/Linux)
- Use different port: `--port 8001`

## Development Tips

1. **Use Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

2. **Auto-reload**: Use `--reload` flag during development

3. **Logging**: Check terminal output for request logs

4. **API Docs**: Always refer to `/docs` for latest endpoint info

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues or questions:
- Check the API documentation at `/docs`
- Review error messages in terminal
- Create an issue in the repository

---

**Built with FastAPI and Google Gemini AI for intelligent safety management**
